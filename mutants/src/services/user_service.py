"""Business logic for managing users."""

from __future__ import annotations

from typing import List

from src.models.common import now_utc
from src.models.user import User, UserCreate, UserUpdate, build_user
from src.repositories.base import Repository
from src.utils.exceptions import (
    EntityAlreadyExistsError,
    EntityNotFoundError,
    ValidationAppError,
)
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


class UserService:
    """Encapsulates user-related operations and business rules."""

    def xǁUserServiceǁ__init____mutmut_orig(self, repository: Repository[User, str]) -> None:
        self._repository = repository

    def xǁUserServiceǁ__init____mutmut_1(self, repository: Repository[User, str]) -> None:
        self._repository = None
    
    xǁUserServiceǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserServiceǁ__init____mutmut_1': xǁUserServiceǁ__init____mutmut_1
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserServiceǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁUserServiceǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁUserServiceǁ__init____mutmut_orig)
    xǁUserServiceǁ__init____mutmut_orig.__name__ = 'xǁUserServiceǁ__init__'

    async def xǁUserServiceǁcreate_user__mutmut_orig(self, payload: UserCreate) -> User:
        """Create a new user ensuring email uniqueness."""
        await self._ensure_unique_email(payload.email)
        user = build_user(payload)
        await self._repository.create(user)
        return user

    async def xǁUserServiceǁcreate_user__mutmut_1(self, payload: UserCreate) -> User:
        """Create a new user ensuring email uniqueness."""
        await self._ensure_unique_email(None)
        user = build_user(payload)
        await self._repository.create(user)
        return user

    async def xǁUserServiceǁcreate_user__mutmut_2(self, payload: UserCreate) -> User:
        """Create a new user ensuring email uniqueness."""
        await self._ensure_unique_email(payload.email)
        user = None
        await self._repository.create(user)
        return user

    async def xǁUserServiceǁcreate_user__mutmut_3(self, payload: UserCreate) -> User:
        """Create a new user ensuring email uniqueness."""
        await self._ensure_unique_email(payload.email)
        user = build_user(None)
        await self._repository.create(user)
        return user

    async def xǁUserServiceǁcreate_user__mutmut_4(self, payload: UserCreate) -> User:
        """Create a new user ensuring email uniqueness."""
        await self._ensure_unique_email(payload.email)
        user = build_user(payload)
        await self._repository.create(None)
        return user
    
    xǁUserServiceǁcreate_user__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserServiceǁcreate_user__mutmut_1': xǁUserServiceǁcreate_user__mutmut_1, 
        'xǁUserServiceǁcreate_user__mutmut_2': xǁUserServiceǁcreate_user__mutmut_2, 
        'xǁUserServiceǁcreate_user__mutmut_3': xǁUserServiceǁcreate_user__mutmut_3, 
        'xǁUserServiceǁcreate_user__mutmut_4': xǁUserServiceǁcreate_user__mutmut_4
    }
    
    def create_user(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserServiceǁcreate_user__mutmut_orig"), object.__getattribute__(self, "xǁUserServiceǁcreate_user__mutmut_mutants"), args, kwargs, self)
        return result 
    
    create_user.__signature__ = _mutmut_signature(xǁUserServiceǁcreate_user__mutmut_orig)
    xǁUserServiceǁcreate_user__mutmut_orig.__name__ = 'xǁUserServiceǁcreate_user'

    async def xǁUserServiceǁlist_users__mutmut_orig(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        default_currency: str | None = None,
    ) -> List[User]:
        """Return users with optional filtering."""
        filters = {}
        if name:
            filters["name"] = name
        if email:
            filters["email"] = email
        if default_currency:
            filters["default_currency"] = default_currency

        users = await self._repository.list(**filters)
        return list(users)

    async def xǁUserServiceǁlist_users__mutmut_1(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        default_currency: str | None = None,
    ) -> List[User]:
        """Return users with optional filtering."""
        filters = None
        if name:
            filters["name"] = name
        if email:
            filters["email"] = email
        if default_currency:
            filters["default_currency"] = default_currency

        users = await self._repository.list(**filters)
        return list(users)

    async def xǁUserServiceǁlist_users__mutmut_2(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        default_currency: str | None = None,
    ) -> List[User]:
        """Return users with optional filtering."""
        filters = {}
        if name:
            filters["name"] = None
        if email:
            filters["email"] = email
        if default_currency:
            filters["default_currency"] = default_currency

        users = await self._repository.list(**filters)
        return list(users)

    async def xǁUserServiceǁlist_users__mutmut_3(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        default_currency: str | None = None,
    ) -> List[User]:
        """Return users with optional filtering."""
        filters = {}
        if name:
            filters["XXnameXX"] = name
        if email:
            filters["email"] = email
        if default_currency:
            filters["default_currency"] = default_currency

        users = await self._repository.list(**filters)
        return list(users)

    async def xǁUserServiceǁlist_users__mutmut_4(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        default_currency: str | None = None,
    ) -> List[User]:
        """Return users with optional filtering."""
        filters = {}
        if name:
            filters["NAME"] = name
        if email:
            filters["email"] = email
        if default_currency:
            filters["default_currency"] = default_currency

        users = await self._repository.list(**filters)
        return list(users)

    async def xǁUserServiceǁlist_users__mutmut_5(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        default_currency: str | None = None,
    ) -> List[User]:
        """Return users with optional filtering."""
        filters = {}
        if name:
            filters["name"] = name
        if email:
            filters["email"] = None
        if default_currency:
            filters["default_currency"] = default_currency

        users = await self._repository.list(**filters)
        return list(users)

    async def xǁUserServiceǁlist_users__mutmut_6(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        default_currency: str | None = None,
    ) -> List[User]:
        """Return users with optional filtering."""
        filters = {}
        if name:
            filters["name"] = name
        if email:
            filters["XXemailXX"] = email
        if default_currency:
            filters["default_currency"] = default_currency

        users = await self._repository.list(**filters)
        return list(users)

    async def xǁUserServiceǁlist_users__mutmut_7(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        default_currency: str | None = None,
    ) -> List[User]:
        """Return users with optional filtering."""
        filters = {}
        if name:
            filters["name"] = name
        if email:
            filters["EMAIL"] = email
        if default_currency:
            filters["default_currency"] = default_currency

        users = await self._repository.list(**filters)
        return list(users)

    async def xǁUserServiceǁlist_users__mutmut_8(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        default_currency: str | None = None,
    ) -> List[User]:
        """Return users with optional filtering."""
        filters = {}
        if name:
            filters["name"] = name
        if email:
            filters["email"] = email
        if default_currency:
            filters["default_currency"] = None

        users = await self._repository.list(**filters)
        return list(users)

    async def xǁUserServiceǁlist_users__mutmut_9(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        default_currency: str | None = None,
    ) -> List[User]:
        """Return users with optional filtering."""
        filters = {}
        if name:
            filters["name"] = name
        if email:
            filters["email"] = email
        if default_currency:
            filters["XXdefault_currencyXX"] = default_currency

        users = await self._repository.list(**filters)
        return list(users)

    async def xǁUserServiceǁlist_users__mutmut_10(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        default_currency: str | None = None,
    ) -> List[User]:
        """Return users with optional filtering."""
        filters = {}
        if name:
            filters["name"] = name
        if email:
            filters["email"] = email
        if default_currency:
            filters["DEFAULT_CURRENCY"] = default_currency

        users = await self._repository.list(**filters)
        return list(users)

    async def xǁUserServiceǁlist_users__mutmut_11(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        default_currency: str | None = None,
    ) -> List[User]:
        """Return users with optional filtering."""
        filters = {}
        if name:
            filters["name"] = name
        if email:
            filters["email"] = email
        if default_currency:
            filters["default_currency"] = default_currency

        users = None
        return list(users)

    async def xǁUserServiceǁlist_users__mutmut_12(
        self,
        *,
        name: str | None = None,
        email: str | None = None,
        default_currency: str | None = None,
    ) -> List[User]:
        """Return users with optional filtering."""
        filters = {}
        if name:
            filters["name"] = name
        if email:
            filters["email"] = email
        if default_currency:
            filters["default_currency"] = default_currency

        users = await self._repository.list(**filters)
        return list(None)
    
    xǁUserServiceǁlist_users__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserServiceǁlist_users__mutmut_1': xǁUserServiceǁlist_users__mutmut_1, 
        'xǁUserServiceǁlist_users__mutmut_2': xǁUserServiceǁlist_users__mutmut_2, 
        'xǁUserServiceǁlist_users__mutmut_3': xǁUserServiceǁlist_users__mutmut_3, 
        'xǁUserServiceǁlist_users__mutmut_4': xǁUserServiceǁlist_users__mutmut_4, 
        'xǁUserServiceǁlist_users__mutmut_5': xǁUserServiceǁlist_users__mutmut_5, 
        'xǁUserServiceǁlist_users__mutmut_6': xǁUserServiceǁlist_users__mutmut_6, 
        'xǁUserServiceǁlist_users__mutmut_7': xǁUserServiceǁlist_users__mutmut_7, 
        'xǁUserServiceǁlist_users__mutmut_8': xǁUserServiceǁlist_users__mutmut_8, 
        'xǁUserServiceǁlist_users__mutmut_9': xǁUserServiceǁlist_users__mutmut_9, 
        'xǁUserServiceǁlist_users__mutmut_10': xǁUserServiceǁlist_users__mutmut_10, 
        'xǁUserServiceǁlist_users__mutmut_11': xǁUserServiceǁlist_users__mutmut_11, 
        'xǁUserServiceǁlist_users__mutmut_12': xǁUserServiceǁlist_users__mutmut_12
    }
    
    def list_users(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserServiceǁlist_users__mutmut_orig"), object.__getattribute__(self, "xǁUserServiceǁlist_users__mutmut_mutants"), args, kwargs, self)
        return result 
    
    list_users.__signature__ = _mutmut_signature(xǁUserServiceǁlist_users__mutmut_orig)
    xǁUserServiceǁlist_users__mutmut_orig.__name__ = 'xǁUserServiceǁlist_users'

    async def xǁUserServiceǁget_user__mutmut_orig(self, user_id: str) -> User:
        """Retrieve user by identifier or raise error."""
        user = await self._repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return user

    async def xǁUserServiceǁget_user__mutmut_1(self, user_id: str) -> User:
        """Retrieve user by identifier or raise error."""
        user = None
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return user

    async def xǁUserServiceǁget_user__mutmut_2(self, user_id: str) -> User:
        """Retrieve user by identifier or raise error."""
        user = await self._repository.get(None)
        if user is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return user

    async def xǁUserServiceǁget_user__mutmut_3(self, user_id: str) -> User:
        """Retrieve user by identifier or raise error."""
        user = await self._repository.get(user_id)
        if user is not None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return user

    async def xǁUserServiceǁget_user__mutmut_4(self, user_id: str) -> User:
        """Retrieve user by identifier or raise error."""
        user = await self._repository.get(user_id)
        if user is None:
            raise EntityNotFoundError(None, context={"id": user_id})
        return user

    async def xǁUserServiceǁget_user__mutmut_5(self, user_id: str) -> User:
        """Retrieve user by identifier or raise error."""
        user = await self._repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context=None)
        return user

    async def xǁUserServiceǁget_user__mutmut_6(self, user_id: str) -> User:
        """Retrieve user by identifier or raise error."""
        user = await self._repository.get(user_id)
        if user is None:
            raise EntityNotFoundError(context={"id": user_id})
        return user

    async def xǁUserServiceǁget_user__mutmut_7(self, user_id: str) -> User:
        """Retrieve user by identifier or raise error."""
        user = await self._repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", )
        return user

    async def xǁUserServiceǁget_user__mutmut_8(self, user_id: str) -> User:
        """Retrieve user by identifier or raise error."""
        user = await self._repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("XXUser not foundXX", context={"id": user_id})
        return user

    async def xǁUserServiceǁget_user__mutmut_9(self, user_id: str) -> User:
        """Retrieve user by identifier or raise error."""
        user = await self._repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("user not found", context={"id": user_id})
        return user

    async def xǁUserServiceǁget_user__mutmut_10(self, user_id: str) -> User:
        """Retrieve user by identifier or raise error."""
        user = await self._repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("USER NOT FOUND", context={"id": user_id})
        return user

    async def xǁUserServiceǁget_user__mutmut_11(self, user_id: str) -> User:
        """Retrieve user by identifier or raise error."""
        user = await self._repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"XXidXX": user_id})
        return user

    async def xǁUserServiceǁget_user__mutmut_12(self, user_id: str) -> User:
        """Retrieve user by identifier or raise error."""
        user = await self._repository.get(user_id)
        if user is None:
            raise EntityNotFoundError("User not found", context={"ID": user_id})
        return user
    
    xǁUserServiceǁget_user__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserServiceǁget_user__mutmut_1': xǁUserServiceǁget_user__mutmut_1, 
        'xǁUserServiceǁget_user__mutmut_2': xǁUserServiceǁget_user__mutmut_2, 
        'xǁUserServiceǁget_user__mutmut_3': xǁUserServiceǁget_user__mutmut_3, 
        'xǁUserServiceǁget_user__mutmut_4': xǁUserServiceǁget_user__mutmut_4, 
        'xǁUserServiceǁget_user__mutmut_5': xǁUserServiceǁget_user__mutmut_5, 
        'xǁUserServiceǁget_user__mutmut_6': xǁUserServiceǁget_user__mutmut_6, 
        'xǁUserServiceǁget_user__mutmut_7': xǁUserServiceǁget_user__mutmut_7, 
        'xǁUserServiceǁget_user__mutmut_8': xǁUserServiceǁget_user__mutmut_8, 
        'xǁUserServiceǁget_user__mutmut_9': xǁUserServiceǁget_user__mutmut_9, 
        'xǁUserServiceǁget_user__mutmut_10': xǁUserServiceǁget_user__mutmut_10, 
        'xǁUserServiceǁget_user__mutmut_11': xǁUserServiceǁget_user__mutmut_11, 
        'xǁUserServiceǁget_user__mutmut_12': xǁUserServiceǁget_user__mutmut_12
    }
    
    def get_user(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserServiceǁget_user__mutmut_orig"), object.__getattribute__(self, "xǁUserServiceǁget_user__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_user.__signature__ = _mutmut_signature(xǁUserServiceǁget_user__mutmut_orig)
    xǁUserServiceǁget_user__mutmut_orig.__name__ = 'xǁUserServiceǁget_user'

    async def xǁUserServiceǁupdate_user__mutmut_orig(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_1(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_2(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=None, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_3(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=None):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_4(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_5(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, ):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_6(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=False, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_7(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=False):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_8(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                None,
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_9(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context=None,
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_10(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_11(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_12(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "XXNo data provided to update userXX",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_13(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "no data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_14(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "NO DATA PROVIDED TO UPDATE USER",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_15(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"XXidXX": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_16(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"ID": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_17(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = None
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_18(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            None,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_19(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            None,
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_20(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_21(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_22(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=None, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_23(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=None),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_24(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_25(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, ),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_26(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=False, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_27(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=False),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_28(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "XXupdated_atXX": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_29(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "UPDATED_AT": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_30(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is not None:
            raise EntityNotFoundError("User not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_31(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError(None, context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_32(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context=None)
        return result

    async def xǁUserServiceǁupdate_user__mutmut_33(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError(context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_34(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", )
        return result

    async def xǁUserServiceǁupdate_user__mutmut_35(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("XXUser not foundXX", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_36(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("user not found", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_37(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("USER NOT FOUND", context={"id": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_38(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"XXidXX": user_id})
        return result

    async def xǁUserServiceǁupdate_user__mutmut_39(self, user_id: str, payload: UserUpdate) -> User:
        """Update an existing user."""
        if not payload.model_dump(exclude_unset=True, exclude_none=True):
            raise ValidationAppError(
                "No data provided to update user",
                context={"id": user_id},
            )

        result = await self._repository.update(
            user_id,
            {
                **payload.model_dump(exclude_unset=True, exclude_none=True),
                "updated_at": now_utc(),
            },
        )
        if result is None:
            raise EntityNotFoundError("User not found", context={"ID": user_id})
        return result
    
    xǁUserServiceǁupdate_user__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserServiceǁupdate_user__mutmut_1': xǁUserServiceǁupdate_user__mutmut_1, 
        'xǁUserServiceǁupdate_user__mutmut_2': xǁUserServiceǁupdate_user__mutmut_2, 
        'xǁUserServiceǁupdate_user__mutmut_3': xǁUserServiceǁupdate_user__mutmut_3, 
        'xǁUserServiceǁupdate_user__mutmut_4': xǁUserServiceǁupdate_user__mutmut_4, 
        'xǁUserServiceǁupdate_user__mutmut_5': xǁUserServiceǁupdate_user__mutmut_5, 
        'xǁUserServiceǁupdate_user__mutmut_6': xǁUserServiceǁupdate_user__mutmut_6, 
        'xǁUserServiceǁupdate_user__mutmut_7': xǁUserServiceǁupdate_user__mutmut_7, 
        'xǁUserServiceǁupdate_user__mutmut_8': xǁUserServiceǁupdate_user__mutmut_8, 
        'xǁUserServiceǁupdate_user__mutmut_9': xǁUserServiceǁupdate_user__mutmut_9, 
        'xǁUserServiceǁupdate_user__mutmut_10': xǁUserServiceǁupdate_user__mutmut_10, 
        'xǁUserServiceǁupdate_user__mutmut_11': xǁUserServiceǁupdate_user__mutmut_11, 
        'xǁUserServiceǁupdate_user__mutmut_12': xǁUserServiceǁupdate_user__mutmut_12, 
        'xǁUserServiceǁupdate_user__mutmut_13': xǁUserServiceǁupdate_user__mutmut_13, 
        'xǁUserServiceǁupdate_user__mutmut_14': xǁUserServiceǁupdate_user__mutmut_14, 
        'xǁUserServiceǁupdate_user__mutmut_15': xǁUserServiceǁupdate_user__mutmut_15, 
        'xǁUserServiceǁupdate_user__mutmut_16': xǁUserServiceǁupdate_user__mutmut_16, 
        'xǁUserServiceǁupdate_user__mutmut_17': xǁUserServiceǁupdate_user__mutmut_17, 
        'xǁUserServiceǁupdate_user__mutmut_18': xǁUserServiceǁupdate_user__mutmut_18, 
        'xǁUserServiceǁupdate_user__mutmut_19': xǁUserServiceǁupdate_user__mutmut_19, 
        'xǁUserServiceǁupdate_user__mutmut_20': xǁUserServiceǁupdate_user__mutmut_20, 
        'xǁUserServiceǁupdate_user__mutmut_21': xǁUserServiceǁupdate_user__mutmut_21, 
        'xǁUserServiceǁupdate_user__mutmut_22': xǁUserServiceǁupdate_user__mutmut_22, 
        'xǁUserServiceǁupdate_user__mutmut_23': xǁUserServiceǁupdate_user__mutmut_23, 
        'xǁUserServiceǁupdate_user__mutmut_24': xǁUserServiceǁupdate_user__mutmut_24, 
        'xǁUserServiceǁupdate_user__mutmut_25': xǁUserServiceǁupdate_user__mutmut_25, 
        'xǁUserServiceǁupdate_user__mutmut_26': xǁUserServiceǁupdate_user__mutmut_26, 
        'xǁUserServiceǁupdate_user__mutmut_27': xǁUserServiceǁupdate_user__mutmut_27, 
        'xǁUserServiceǁupdate_user__mutmut_28': xǁUserServiceǁupdate_user__mutmut_28, 
        'xǁUserServiceǁupdate_user__mutmut_29': xǁUserServiceǁupdate_user__mutmut_29, 
        'xǁUserServiceǁupdate_user__mutmut_30': xǁUserServiceǁupdate_user__mutmut_30, 
        'xǁUserServiceǁupdate_user__mutmut_31': xǁUserServiceǁupdate_user__mutmut_31, 
        'xǁUserServiceǁupdate_user__mutmut_32': xǁUserServiceǁupdate_user__mutmut_32, 
        'xǁUserServiceǁupdate_user__mutmut_33': xǁUserServiceǁupdate_user__mutmut_33, 
        'xǁUserServiceǁupdate_user__mutmut_34': xǁUserServiceǁupdate_user__mutmut_34, 
        'xǁUserServiceǁupdate_user__mutmut_35': xǁUserServiceǁupdate_user__mutmut_35, 
        'xǁUserServiceǁupdate_user__mutmut_36': xǁUserServiceǁupdate_user__mutmut_36, 
        'xǁUserServiceǁupdate_user__mutmut_37': xǁUserServiceǁupdate_user__mutmut_37, 
        'xǁUserServiceǁupdate_user__mutmut_38': xǁUserServiceǁupdate_user__mutmut_38, 
        'xǁUserServiceǁupdate_user__mutmut_39': xǁUserServiceǁupdate_user__mutmut_39
    }
    
    def update_user(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserServiceǁupdate_user__mutmut_orig"), object.__getattribute__(self, "xǁUserServiceǁupdate_user__mutmut_mutants"), args, kwargs, self)
        return result 
    
    update_user.__signature__ = _mutmut_signature(xǁUserServiceǁupdate_user__mutmut_orig)
    xǁUserServiceǁupdate_user__mutmut_orig.__name__ = 'xǁUserServiceǁupdate_user'

    async def xǁUserServiceǁdelete_user__mutmut_orig(self, user_id: str) -> None:
        """Delete a user ensuring existence."""
        deleted = await self._repository.delete(user_id)
        if not deleted:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁUserServiceǁdelete_user__mutmut_1(self, user_id: str) -> None:
        """Delete a user ensuring existence."""
        deleted = None
        if not deleted:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁUserServiceǁdelete_user__mutmut_2(self, user_id: str) -> None:
        """Delete a user ensuring existence."""
        deleted = await self._repository.delete(None)
        if not deleted:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁUserServiceǁdelete_user__mutmut_3(self, user_id: str) -> None:
        """Delete a user ensuring existence."""
        deleted = await self._repository.delete(user_id)
        if deleted:
            raise EntityNotFoundError("User not found", context={"id": user_id})

    async def xǁUserServiceǁdelete_user__mutmut_4(self, user_id: str) -> None:
        """Delete a user ensuring existence."""
        deleted = await self._repository.delete(user_id)
        if not deleted:
            raise EntityNotFoundError(None, context={"id": user_id})

    async def xǁUserServiceǁdelete_user__mutmut_5(self, user_id: str) -> None:
        """Delete a user ensuring existence."""
        deleted = await self._repository.delete(user_id)
        if not deleted:
            raise EntityNotFoundError("User not found", context=None)

    async def xǁUserServiceǁdelete_user__mutmut_6(self, user_id: str) -> None:
        """Delete a user ensuring existence."""
        deleted = await self._repository.delete(user_id)
        if not deleted:
            raise EntityNotFoundError(context={"id": user_id})

    async def xǁUserServiceǁdelete_user__mutmut_7(self, user_id: str) -> None:
        """Delete a user ensuring existence."""
        deleted = await self._repository.delete(user_id)
        if not deleted:
            raise EntityNotFoundError("User not found", )

    async def xǁUserServiceǁdelete_user__mutmut_8(self, user_id: str) -> None:
        """Delete a user ensuring existence."""
        deleted = await self._repository.delete(user_id)
        if not deleted:
            raise EntityNotFoundError("XXUser not foundXX", context={"id": user_id})

    async def xǁUserServiceǁdelete_user__mutmut_9(self, user_id: str) -> None:
        """Delete a user ensuring existence."""
        deleted = await self._repository.delete(user_id)
        if not deleted:
            raise EntityNotFoundError("user not found", context={"id": user_id})

    async def xǁUserServiceǁdelete_user__mutmut_10(self, user_id: str) -> None:
        """Delete a user ensuring existence."""
        deleted = await self._repository.delete(user_id)
        if not deleted:
            raise EntityNotFoundError("USER NOT FOUND", context={"id": user_id})

    async def xǁUserServiceǁdelete_user__mutmut_11(self, user_id: str) -> None:
        """Delete a user ensuring existence."""
        deleted = await self._repository.delete(user_id)
        if not deleted:
            raise EntityNotFoundError("User not found", context={"XXidXX": user_id})

    async def xǁUserServiceǁdelete_user__mutmut_12(self, user_id: str) -> None:
        """Delete a user ensuring existence."""
        deleted = await self._repository.delete(user_id)
        if not deleted:
            raise EntityNotFoundError("User not found", context={"ID": user_id})
    
    xǁUserServiceǁdelete_user__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserServiceǁdelete_user__mutmut_1': xǁUserServiceǁdelete_user__mutmut_1, 
        'xǁUserServiceǁdelete_user__mutmut_2': xǁUserServiceǁdelete_user__mutmut_2, 
        'xǁUserServiceǁdelete_user__mutmut_3': xǁUserServiceǁdelete_user__mutmut_3, 
        'xǁUserServiceǁdelete_user__mutmut_4': xǁUserServiceǁdelete_user__mutmut_4, 
        'xǁUserServiceǁdelete_user__mutmut_5': xǁUserServiceǁdelete_user__mutmut_5, 
        'xǁUserServiceǁdelete_user__mutmut_6': xǁUserServiceǁdelete_user__mutmut_6, 
        'xǁUserServiceǁdelete_user__mutmut_7': xǁUserServiceǁdelete_user__mutmut_7, 
        'xǁUserServiceǁdelete_user__mutmut_8': xǁUserServiceǁdelete_user__mutmut_8, 
        'xǁUserServiceǁdelete_user__mutmut_9': xǁUserServiceǁdelete_user__mutmut_9, 
        'xǁUserServiceǁdelete_user__mutmut_10': xǁUserServiceǁdelete_user__mutmut_10, 
        'xǁUserServiceǁdelete_user__mutmut_11': xǁUserServiceǁdelete_user__mutmut_11, 
        'xǁUserServiceǁdelete_user__mutmut_12': xǁUserServiceǁdelete_user__mutmut_12
    }
    
    def delete_user(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserServiceǁdelete_user__mutmut_orig"), object.__getattribute__(self, "xǁUserServiceǁdelete_user__mutmut_mutants"), args, kwargs, self)
        return result 
    
    delete_user.__signature__ = _mutmut_signature(xǁUserServiceǁdelete_user__mutmut_orig)
    xǁUserServiceǁdelete_user__mutmut_orig.__name__ = 'xǁUserServiceǁdelete_user'

    async def xǁUserServiceǁ_ensure_unique_email__mutmut_orig(self, email: str) -> None:
        """Ensure no other user is registered with the same email."""
        existing = list(await self._repository.list(email=email))
        if existing:
            raise EntityAlreadyExistsError(
                "Email already registered",
                context={"email": email},
            )

    async def xǁUserServiceǁ_ensure_unique_email__mutmut_1(self, email: str) -> None:
        """Ensure no other user is registered with the same email."""
        existing = None
        if existing:
            raise EntityAlreadyExistsError(
                "Email already registered",
                context={"email": email},
            )

    async def xǁUserServiceǁ_ensure_unique_email__mutmut_2(self, email: str) -> None:
        """Ensure no other user is registered with the same email."""
        existing = list(None)
        if existing:
            raise EntityAlreadyExistsError(
                "Email already registered",
                context={"email": email},
            )

    async def xǁUserServiceǁ_ensure_unique_email__mutmut_3(self, email: str) -> None:
        """Ensure no other user is registered with the same email."""
        existing = list(await self._repository.list(email=None))
        if existing:
            raise EntityAlreadyExistsError(
                "Email already registered",
                context={"email": email},
            )

    async def xǁUserServiceǁ_ensure_unique_email__mutmut_4(self, email: str) -> None:
        """Ensure no other user is registered with the same email."""
        existing = list(await self._repository.list(email=email))
        if existing:
            raise EntityAlreadyExistsError(
                None,
                context={"email": email},
            )

    async def xǁUserServiceǁ_ensure_unique_email__mutmut_5(self, email: str) -> None:
        """Ensure no other user is registered with the same email."""
        existing = list(await self._repository.list(email=email))
        if existing:
            raise EntityAlreadyExistsError(
                "Email already registered",
                context=None,
            )

    async def xǁUserServiceǁ_ensure_unique_email__mutmut_6(self, email: str) -> None:
        """Ensure no other user is registered with the same email."""
        existing = list(await self._repository.list(email=email))
        if existing:
            raise EntityAlreadyExistsError(
                context={"email": email},
            )

    async def xǁUserServiceǁ_ensure_unique_email__mutmut_7(self, email: str) -> None:
        """Ensure no other user is registered with the same email."""
        existing = list(await self._repository.list(email=email))
        if existing:
            raise EntityAlreadyExistsError(
                "Email already registered",
                )

    async def xǁUserServiceǁ_ensure_unique_email__mutmut_8(self, email: str) -> None:
        """Ensure no other user is registered with the same email."""
        existing = list(await self._repository.list(email=email))
        if existing:
            raise EntityAlreadyExistsError(
                "XXEmail already registeredXX",
                context={"email": email},
            )

    async def xǁUserServiceǁ_ensure_unique_email__mutmut_9(self, email: str) -> None:
        """Ensure no other user is registered with the same email."""
        existing = list(await self._repository.list(email=email))
        if existing:
            raise EntityAlreadyExistsError(
                "email already registered",
                context={"email": email},
            )

    async def xǁUserServiceǁ_ensure_unique_email__mutmut_10(self, email: str) -> None:
        """Ensure no other user is registered with the same email."""
        existing = list(await self._repository.list(email=email))
        if existing:
            raise EntityAlreadyExistsError(
                "EMAIL ALREADY REGISTERED",
                context={"email": email},
            )

    async def xǁUserServiceǁ_ensure_unique_email__mutmut_11(self, email: str) -> None:
        """Ensure no other user is registered with the same email."""
        existing = list(await self._repository.list(email=email))
        if existing:
            raise EntityAlreadyExistsError(
                "Email already registered",
                context={"XXemailXX": email},
            )

    async def xǁUserServiceǁ_ensure_unique_email__mutmut_12(self, email: str) -> None:
        """Ensure no other user is registered with the same email."""
        existing = list(await self._repository.list(email=email))
        if existing:
            raise EntityAlreadyExistsError(
                "Email already registered",
                context={"EMAIL": email},
            )
    
    xǁUserServiceǁ_ensure_unique_email__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserServiceǁ_ensure_unique_email__mutmut_1': xǁUserServiceǁ_ensure_unique_email__mutmut_1, 
        'xǁUserServiceǁ_ensure_unique_email__mutmut_2': xǁUserServiceǁ_ensure_unique_email__mutmut_2, 
        'xǁUserServiceǁ_ensure_unique_email__mutmut_3': xǁUserServiceǁ_ensure_unique_email__mutmut_3, 
        'xǁUserServiceǁ_ensure_unique_email__mutmut_4': xǁUserServiceǁ_ensure_unique_email__mutmut_4, 
        'xǁUserServiceǁ_ensure_unique_email__mutmut_5': xǁUserServiceǁ_ensure_unique_email__mutmut_5, 
        'xǁUserServiceǁ_ensure_unique_email__mutmut_6': xǁUserServiceǁ_ensure_unique_email__mutmut_6, 
        'xǁUserServiceǁ_ensure_unique_email__mutmut_7': xǁUserServiceǁ_ensure_unique_email__mutmut_7, 
        'xǁUserServiceǁ_ensure_unique_email__mutmut_8': xǁUserServiceǁ_ensure_unique_email__mutmut_8, 
        'xǁUserServiceǁ_ensure_unique_email__mutmut_9': xǁUserServiceǁ_ensure_unique_email__mutmut_9, 
        'xǁUserServiceǁ_ensure_unique_email__mutmut_10': xǁUserServiceǁ_ensure_unique_email__mutmut_10, 
        'xǁUserServiceǁ_ensure_unique_email__mutmut_11': xǁUserServiceǁ_ensure_unique_email__mutmut_11, 
        'xǁUserServiceǁ_ensure_unique_email__mutmut_12': xǁUserServiceǁ_ensure_unique_email__mutmut_12
    }
    
    def _ensure_unique_email(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserServiceǁ_ensure_unique_email__mutmut_orig"), object.__getattribute__(self, "xǁUserServiceǁ_ensure_unique_email__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ensure_unique_email.__signature__ = _mutmut_signature(xǁUserServiceǁ_ensure_unique_email__mutmut_orig)
    xǁUserServiceǁ_ensure_unique_email__mutmut_orig.__name__ = 'xǁUserServiceǁ_ensure_unique_email'
