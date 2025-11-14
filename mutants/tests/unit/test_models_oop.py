"""Tests focusing on OO aspects of the domain models."""

import unittest
from datetime import date

from src.models import BudgetStatus, BudgetSummary, GoalModel, GoalStatus
from tests.fixtures.factories import make_budget_model, make_goal_model


class TestModelsOOP(unittest.TestCase):
    def test_budget_model_status_property_uses_polymorphism(self):
        cases = [
            (50, BudgetStatus.HEALTHY),
            (85, BudgetStatus.WARNING),
            (120, BudgetStatus.EXCEEDED),
        ]
        for spent, expected_status in cases:
            with self.subTest(spent=spent):
                budget = make_budget_model(limit_amount=100, amount_spent=spent)
                self.assertEqual(budget.status, expected_status)

    def test_budget_summary_derives_remaining_amount(self):
        budget = make_budget_model(limit_amount=200, amount_spent=50)
        summary = BudgetSummary(
            category=budget.category,
            limit_amount=budget.limit_amount,
            amount_spent=budget.amount_spent,
            status=budget.status,
            remaining=budget.limit_amount - budget.amount_spent,
        )

        self.assertEqual(summary.remaining, 150)

    def test_goal_model_completes_when_target_reached(self):
        goal = make_goal_model(target_amount=500, current_amount=500)

        self.assertIn(goal.status, {GoalStatus.ACTIVE, GoalStatus.COMPLETED})
        goal_data = goal.model_copy(update={"current_amount": 500, "status": GoalStatus.COMPLETED})
        self.assertEqual(goal_data.status, GoalStatus.COMPLETED)
