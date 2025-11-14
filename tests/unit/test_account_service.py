"""Unit tests for AccountService."""

import unittest

from src.models import AccountUpdate
from src.services import AccountService, NotFoundError
from tests.fixtures.factories import make_account_create, make_account_model, make_user_model
from tests.fixtures.memory_repositories import MemoryAccountRepository, MemoryUserRepository


class TestAccountService(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.user_repository = MemoryUserRepository()
        self.account_repository = MemoryAccountRepository()
        self.service = AccountService(repository=self.account_repository, user_repository=self.user_repository)

    async def test_create_account_requires_existing_user(self):
        user = make_user_model()
        self.user_repository.storage[user.id] = user.model_dump()
        payload = make_account_create(user_id=user.id)

        account = await self.service.create_account(payload)

        self.assertEqual(account.user_id, user.id)

    async def test_create_account_missing_user_raises(self):
        with self.assertRaises(NotFoundError):
            await self.service.create_account(make_account_create())

    async def test_update_nonexistent_account_raises(self):
        with self.assertRaises(NotFoundError):
            await self.service.update_account("invalid", AccountUpdate(name="New"))

    async def test_get_account_returns_entry(self):
        account = make_account_model()
        self.account_repository.storage[account.id] = account.model_dump()

        result = await self.service.get_account(account.id)

        self.assertEqual(result.id, account.id)

    async def test_get_account_missing_raises(self):
        for missing_id in ("ghost", "invalid"):
            with self.subTest(missing_id=missing_id):
                with self.assertRaises(NotFoundError):
                    await self.service.get_account(missing_id)

    async def test_update_account_success(self):
        account = make_account_model(name="Old")
        self.account_repository.storage[account.id] = account.model_dump()

        updated = await self.service.update_account(account.id, AccountUpdate(name="New"))

        self.assertEqual(updated.name, "New")

    async def test_list_accounts_returns_only_user_entries(self):
        user = make_user_model()
        self.user_repository.storage[user.id] = user.model_dump()
        owned = make_account_model(user_id=user.id)
        external = make_account_model(user_id="other")
        self.account_repository.storage[owned.id] = owned.model_dump()
        self.account_repository.storage[external.id] = external.model_dump()

        accounts = await self.service.list_accounts(user.id)

        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0].user_id, user.id)

    async def test_delete_account_removes_entry(self):
        account = make_account_model()
        self.account_repository.storage[account.id] = account.model_dump()

        result = await self.service.delete_account(account.id)

        self.assertTrue(result)
        self.assertNotIn(account.id, self.account_repository.storage)

    async def test_delete_account_missing_raises(self):
        for missing_id in ("ghost", "orphan"):
            with self.subTest(missing_id=missing_id):
                with self.assertRaises(NotFoundError):
                    await self.service.delete_account(missing_id)
