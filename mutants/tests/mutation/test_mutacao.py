"""High-value tests intended to aid mutation testing runs."""

from unittest.mock import AsyncMock

import pytest

from src.models import TransactionType
from src.services import BusinessRuleError
from tests.fixtures.factories import (
    make_account_model,
    make_budget_model,
    make_goal_model,
    make_transaction_create,
    make_user_model,
)


@pytest.mark.asyncio
async def test_goal_completion_releases_locked_amount(goal_service, goal_repository, account_repository):
    account = make_account_model(balance=500, goal_locked_amount=100)
    goal = make_goal_model(
        account_id=account.id,
        user_id=account.user_id,
        lock_funds=True,
        current_amount=900,
        reserved_amount=100,
        target_amount=1000,
    )
    account_repository.storage[account.id] = account.model_dump()
    goal_repository.storage[goal.id] = goal.model_dump()

    updated = await goal_service.apply_contribution(goal.id, amount=100)

    assert updated.status.value == "completed"
    assert account_repository.storage[account.id]["goal_locked_amount"] == 0


def test_budget_status_thresholds_are_enforced():
    budget = make_budget_model(limit_amount=100, amount_spent=79)
    assert budget.status.value == "healthy"
    warning_budget = make_budget_model(limit_amount=100, amount_spent=90)
    assert warning_budget.status.value == "warning"
    exceeded_budget = make_budget_model(limit_amount=100, amount_spent=150)
    assert exceeded_budget.status.value == "exceeded"


@pytest.mark.asyncio
async def test_budget_apply_expense_allows_exact_limit(budget_service, budget_repository):
    budget = make_budget_model(limit_amount=120, amount_spent=80)
    budget_repository.storage[budget.id] = budget.model_dump()

    updated = await budget_service.apply_expense(budget, amount=40)

    assert updated.amount_spent == 120


@pytest.mark.asyncio
async def test_goal_contribution_requires_expense(transaction_service, user_repository, account_repository, goal_repository):
    user = make_user_model()
    account = make_account_model(user_id=user.id, balance=400)
    goal = make_goal_model(account_id=account.id, user_id=user.id)
    user_repository.storage[user.id] = user.model_dump()
    account_repository.storage[account.id] = account.model_dump()
    goal_repository.storage[goal.id] = goal.model_dump()

    payload = make_transaction_create(
        user_id=user.id,
        account_id=account.id,
        goal_id=goal.id,
        type=TransactionType.INCOME,
        amount=50,
    )

    with pytest.raises(BusinessRuleError):
        await transaction_service.create_transaction(payload)


@pytest.mark.asyncio
async def test_goal_contribution_skips_budget_but_updates_goal(
    transaction_service,
    user_repository,
    account_repository,
    goal_repository,
    budget_service,
):
    user = make_user_model()
    account = make_account_model(user_id=user.id, balance=500)
    goal = make_goal_model(account_id=account.id, user_id=user.id, lock_funds=False)
    user_repository.storage[user.id] = user.model_dump()
    account_repository.storage[account.id] = account.model_dump()
    goal_repository.storage[goal.id] = goal.model_dump()

    payload = make_transaction_create(
        user_id=user.id,
        account_id=account.id,
        goal_id=goal.id,
        amount=60,
    )
    budget_service.apply_expense = AsyncMock()
    transaction_service.goal_service.apply_contribution = AsyncMock()

    await transaction_service.create_transaction(payload)

    budget_service.apply_expense.assert_not_awaited()
    transaction_service.goal_service.apply_contribution.assert_awaited_once_with(goal.id, payload.amount)
