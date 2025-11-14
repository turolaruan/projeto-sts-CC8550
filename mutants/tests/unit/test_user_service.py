"""Unit tests for UserService."""

import unittest

from src.models import UserUpdate
from src.services import BusinessRuleError, NotFoundError, UserService
from tests.fixtures.factories import make_user_create, make_user_model
from tests.fixtures.memory_repositories import MemoryUserRepository


class TestUserService(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.user_repository = MemoryUserRepository()
        self.service = UserService(repository=self.user_repository)

    async def test_create_user_persists_and_returns_user(self):
        payload = make_user_create(email="unique@example.com")

        user = await self.service.create_user(payload)

        self.assertEqual(user.email, payload.email)
        self.assertEqual(len(self.user_repository.storage), 1)

    async def test_create_user_with_duplicate_email_raises(self):
        existing = make_user_model(email="dup@example.com")
        self.user_repository.storage[existing.id] = existing.model_dump()

        with self.assertRaises(BusinessRuleError):
            await self.service.create_user(make_user_create(email="dup@example.com"))

    async def test_get_user_with_invalid_id_raises(self):
        for missing_id in ("missing-id", "ghost"):
            with self.subTest(missing_id=missing_id):
                with self.assertRaises(NotFoundError):
                    await self.service.get_user(missing_id)

    async def test_update_user_changes_fields(self):
        stored = make_user_model(name="Old Name")
        self.user_repository.storage[stored.id] = stored.model_dump()

        updated = await self.service.update_user(stored.id, UserUpdate(name="New Name"))

        self.assertEqual(updated.name, "New Name")

    async def test_update_user_not_found_raises(self):
        with self.assertRaises(NotFoundError):
            await self.service.update_user("missing", UserUpdate(name="Ghost"))

    async def test_delete_user_removes_entry(self):
        stored = make_user_model()
        self.user_repository.storage[stored.id] = stored.model_dump()

        result = await self.service.delete_user(stored.id)

        self.assertTrue(result)
        self.assertNotIn(stored.id, self.user_repository.storage)

    async def test_delete_user_missing_raises(self):
        for missing_id in ("ghost", "void"):
            with self.subTest(missing_id=missing_id):
                with self.assertRaises(NotFoundError):
                    await self.service.delete_user(missing_id)

    async def test_list_users_returns_all(self):
        stored = make_user_model()
        self.user_repository.storage[stored.id] = stored.model_dump()

        users = await self.service.list_users()

        self.assertEqual(len(users), 1)

    async def test_get_user_returns_entry(self):
        stored = make_user_model()
        self.user_repository.storage[stored.id] = stored.model_dump()

        user = await self.service.get_user(stored.id)

        self.assertEqual(user.id, stored.id)
