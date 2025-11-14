"""Application settings definitions."""

from functools import lru_cache
from pathlib import Path
from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
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


class Settings(BaseSettings):
    """Holds configuration loaded from environment variables and files."""

    app_name: str = Field(
        default="Personal Finance Manager API",
        validation_alias="APP_NAME",
    )
    environment: str = Field(default="development", validation_alias="ENVIRONMENT")
    debug: bool = Field(default=True, validation_alias="DEBUG")
    mongodb_uri: str = Field(
        default="mongodb://localhost:27017",
        validation_alias="MONGODB_URI",
    )
    mongodb_db: str = Field(
        default="personal_finance_db",
        validation_alias="MONGODB_DB",
    )
    log_level: str = Field(default="INFO", validation_alias="LOG_LEVEL")
    log_config_path: str = Field(
        default="config/logging.yaml",
        validation_alias="LOG_CONFIG_PATH",
    )

    model_config = SettingsConfigDict(
        env_file=(".env",),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def is_production(self) -> bool:
        """Return True when running in production environment."""
        return self.environment.lower() == "production"

    @property
    def log_config_file(self) -> Path:
        """Return resolved path to logging configuration file."""
        path = Path(self.log_config_path)
        return path if path.is_absolute() else Path.cwd() / path

    def xǁSettingsǁmodel_dump_public__mutmut_orig(self) -> dict[str, Any]:
        """Return safe subset of settings for health endpoint responses."""
        return {
            "app_name": self.app_name,
            "environment": self.environment,
            "debug": self.debug,
            "mongodb_db": self.mongodb_db,
        }

    def xǁSettingsǁmodel_dump_public__mutmut_1(self) -> dict[str, Any]:
        """Return safe subset of settings for health endpoint responses."""
        return {
            "XXapp_nameXX": self.app_name,
            "environment": self.environment,
            "debug": self.debug,
            "mongodb_db": self.mongodb_db,
        }

    def xǁSettingsǁmodel_dump_public__mutmut_2(self) -> dict[str, Any]:
        """Return safe subset of settings for health endpoint responses."""
        return {
            "APP_NAME": self.app_name,
            "environment": self.environment,
            "debug": self.debug,
            "mongodb_db": self.mongodb_db,
        }

    def xǁSettingsǁmodel_dump_public__mutmut_3(self) -> dict[str, Any]:
        """Return safe subset of settings for health endpoint responses."""
        return {
            "app_name": self.app_name,
            "XXenvironmentXX": self.environment,
            "debug": self.debug,
            "mongodb_db": self.mongodb_db,
        }

    def xǁSettingsǁmodel_dump_public__mutmut_4(self) -> dict[str, Any]:
        """Return safe subset of settings for health endpoint responses."""
        return {
            "app_name": self.app_name,
            "ENVIRONMENT": self.environment,
            "debug": self.debug,
            "mongodb_db": self.mongodb_db,
        }

    def xǁSettingsǁmodel_dump_public__mutmut_5(self) -> dict[str, Any]:
        """Return safe subset of settings for health endpoint responses."""
        return {
            "app_name": self.app_name,
            "environment": self.environment,
            "XXdebugXX": self.debug,
            "mongodb_db": self.mongodb_db,
        }

    def xǁSettingsǁmodel_dump_public__mutmut_6(self) -> dict[str, Any]:
        """Return safe subset of settings for health endpoint responses."""
        return {
            "app_name": self.app_name,
            "environment": self.environment,
            "DEBUG": self.debug,
            "mongodb_db": self.mongodb_db,
        }

    def xǁSettingsǁmodel_dump_public__mutmut_7(self) -> dict[str, Any]:
        """Return safe subset of settings for health endpoint responses."""
        return {
            "app_name": self.app_name,
            "environment": self.environment,
            "debug": self.debug,
            "XXmongodb_dbXX": self.mongodb_db,
        }

    def xǁSettingsǁmodel_dump_public__mutmut_8(self) -> dict[str, Any]:
        """Return safe subset of settings for health endpoint responses."""
        return {
            "app_name": self.app_name,
            "environment": self.environment,
            "debug": self.debug,
            "MONGODB_DB": self.mongodb_db,
        }
    
    xǁSettingsǁmodel_dump_public__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSettingsǁmodel_dump_public__mutmut_1': xǁSettingsǁmodel_dump_public__mutmut_1, 
        'xǁSettingsǁmodel_dump_public__mutmut_2': xǁSettingsǁmodel_dump_public__mutmut_2, 
        'xǁSettingsǁmodel_dump_public__mutmut_3': xǁSettingsǁmodel_dump_public__mutmut_3, 
        'xǁSettingsǁmodel_dump_public__mutmut_4': xǁSettingsǁmodel_dump_public__mutmut_4, 
        'xǁSettingsǁmodel_dump_public__mutmut_5': xǁSettingsǁmodel_dump_public__mutmut_5, 
        'xǁSettingsǁmodel_dump_public__mutmut_6': xǁSettingsǁmodel_dump_public__mutmut_6, 
        'xǁSettingsǁmodel_dump_public__mutmut_7': xǁSettingsǁmodel_dump_public__mutmut_7, 
        'xǁSettingsǁmodel_dump_public__mutmut_8': xǁSettingsǁmodel_dump_public__mutmut_8
    }
    
    def model_dump_public(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSettingsǁmodel_dump_public__mutmut_orig"), object.__getattribute__(self, "xǁSettingsǁmodel_dump_public__mutmut_mutants"), args, kwargs, self)
        return result 
    
    model_dump_public.__signature__ = _mutmut_signature(xǁSettingsǁmodel_dump_public__mutmut_orig)
    xǁSettingsǁmodel_dump_public__mutmut_orig.__name__ = 'xǁSettingsǁmodel_dump_public'


@lru_cache
def get_settings() -> Settings:
    """Return cached application settings instance."""
    return Settings()
