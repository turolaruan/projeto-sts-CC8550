"""Logging configuration utilities."""

from __future__ import annotations

import logging
import logging.config
from pathlib import Path
from typing import Any

import yaml

from src.config import Settings
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


def x_configure_logging__mutmut_orig(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_1(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = None
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_2(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_3(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=None)
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_4(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.lower())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_5(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            None,
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_6(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            None,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_7(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_8(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_9(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(None).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_10(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "XXLogging configuration file not found at %s. Using basicConfig.XX",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_11(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "logging configuration file not found at %s. using basicconfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_12(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "LOGGING CONFIGURATION FILE NOT FOUND AT %S. USING BASICCONFIG.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_13(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open(None, encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_14(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding=None) as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_15(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open(encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_16(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", ) as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_17(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("XXrtXX", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_18(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("RT", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_19(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="XXutf-8XX") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_20(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="UTF-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_21(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = None

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_22(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) and {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_23(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(None) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_24(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(None)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_25(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(None)
    logging.getLogger(__name__).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_26(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(None)


def x_configure_logging__mutmut_27(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(None).setLevel(settings.log_level.upper())


def x_configure_logging__mutmut_28(settings: Settings) -> None:
    """Load logging configuration from YAML file and apply it."""
    config_path = settings.log_config_file
    if not config_path.exists():
        logging.basicConfig(level=settings.log_level.upper())
        logging.getLogger(__name__).warning(
            "Logging configuration file not found at %s. Using basicConfig.",
            config_path,
        )
        return

    with config_path.open("rt", encoding="utf-8") as config_file:
        config: dict[str, Any] = yaml.safe_load(config_file) or {}

    _ensure_log_directories(config)
    logging.config.dictConfig(config)
    logging.getLogger(__name__).setLevel(settings.log_level.lower())

x_configure_logging__mutmut_mutants : ClassVar[MutantDict] = {
'x_configure_logging__mutmut_1': x_configure_logging__mutmut_1, 
    'x_configure_logging__mutmut_2': x_configure_logging__mutmut_2, 
    'x_configure_logging__mutmut_3': x_configure_logging__mutmut_3, 
    'x_configure_logging__mutmut_4': x_configure_logging__mutmut_4, 
    'x_configure_logging__mutmut_5': x_configure_logging__mutmut_5, 
    'x_configure_logging__mutmut_6': x_configure_logging__mutmut_6, 
    'x_configure_logging__mutmut_7': x_configure_logging__mutmut_7, 
    'x_configure_logging__mutmut_8': x_configure_logging__mutmut_8, 
    'x_configure_logging__mutmut_9': x_configure_logging__mutmut_9, 
    'x_configure_logging__mutmut_10': x_configure_logging__mutmut_10, 
    'x_configure_logging__mutmut_11': x_configure_logging__mutmut_11, 
    'x_configure_logging__mutmut_12': x_configure_logging__mutmut_12, 
    'x_configure_logging__mutmut_13': x_configure_logging__mutmut_13, 
    'x_configure_logging__mutmut_14': x_configure_logging__mutmut_14, 
    'x_configure_logging__mutmut_15': x_configure_logging__mutmut_15, 
    'x_configure_logging__mutmut_16': x_configure_logging__mutmut_16, 
    'x_configure_logging__mutmut_17': x_configure_logging__mutmut_17, 
    'x_configure_logging__mutmut_18': x_configure_logging__mutmut_18, 
    'x_configure_logging__mutmut_19': x_configure_logging__mutmut_19, 
    'x_configure_logging__mutmut_20': x_configure_logging__mutmut_20, 
    'x_configure_logging__mutmut_21': x_configure_logging__mutmut_21, 
    'x_configure_logging__mutmut_22': x_configure_logging__mutmut_22, 
    'x_configure_logging__mutmut_23': x_configure_logging__mutmut_23, 
    'x_configure_logging__mutmut_24': x_configure_logging__mutmut_24, 
    'x_configure_logging__mutmut_25': x_configure_logging__mutmut_25, 
    'x_configure_logging__mutmut_26': x_configure_logging__mutmut_26, 
    'x_configure_logging__mutmut_27': x_configure_logging__mutmut_27, 
    'x_configure_logging__mutmut_28': x_configure_logging__mutmut_28
}

def configure_logging(*args, **kwargs):
    result = _mutmut_trampoline(x_configure_logging__mutmut_orig, x_configure_logging__mutmut_mutants, args, kwargs)
    return result 

configure_logging.__signature__ = _mutmut_signature(x_configure_logging__mutmut_orig)
x_configure_logging__mutmut_orig.__name__ = 'x_configure_logging'


def x__ensure_log_directories__mutmut_orig(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_1(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = None
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_2(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get(None, {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_3(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", None)
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_4(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get({})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_5(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", )
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_6(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("XXhandlersXX", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_7(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("HANDLERS", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_8(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = None
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_9(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get(None)
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_10(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("XXfilenameXX")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_11(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("FILENAME")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_12(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_13(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            break
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_14(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = None
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_15(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(None)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_16(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = None
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_17(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if directory.exists():
            directory.mkdir(parents=True, exist_ok=True)


def x__ensure_log_directories__mutmut_18(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=None, exist_ok=True)


def x__ensure_log_directories__mutmut_19(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=None)


def x__ensure_log_directories__mutmut_20(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(exist_ok=True)


def x__ensure_log_directories__mutmut_21(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, )


def x__ensure_log_directories__mutmut_22(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=False, exist_ok=True)


def x__ensure_log_directories__mutmut_23(config: dict[str, Any]) -> None:
    """Create directories for log handlers that write to the file system."""
    handlers: dict[str, Any] = config.get("handlers", {})
    for handler in handlers.values():
        filename = handler.get("filename")
        if not filename:
            continue
        path = Path(filename)
        directory = path.parent
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=False)

x__ensure_log_directories__mutmut_mutants : ClassVar[MutantDict] = {
'x__ensure_log_directories__mutmut_1': x__ensure_log_directories__mutmut_1, 
    'x__ensure_log_directories__mutmut_2': x__ensure_log_directories__mutmut_2, 
    'x__ensure_log_directories__mutmut_3': x__ensure_log_directories__mutmut_3, 
    'x__ensure_log_directories__mutmut_4': x__ensure_log_directories__mutmut_4, 
    'x__ensure_log_directories__mutmut_5': x__ensure_log_directories__mutmut_5, 
    'x__ensure_log_directories__mutmut_6': x__ensure_log_directories__mutmut_6, 
    'x__ensure_log_directories__mutmut_7': x__ensure_log_directories__mutmut_7, 
    'x__ensure_log_directories__mutmut_8': x__ensure_log_directories__mutmut_8, 
    'x__ensure_log_directories__mutmut_9': x__ensure_log_directories__mutmut_9, 
    'x__ensure_log_directories__mutmut_10': x__ensure_log_directories__mutmut_10, 
    'x__ensure_log_directories__mutmut_11': x__ensure_log_directories__mutmut_11, 
    'x__ensure_log_directories__mutmut_12': x__ensure_log_directories__mutmut_12, 
    'x__ensure_log_directories__mutmut_13': x__ensure_log_directories__mutmut_13, 
    'x__ensure_log_directories__mutmut_14': x__ensure_log_directories__mutmut_14, 
    'x__ensure_log_directories__mutmut_15': x__ensure_log_directories__mutmut_15, 
    'x__ensure_log_directories__mutmut_16': x__ensure_log_directories__mutmut_16, 
    'x__ensure_log_directories__mutmut_17': x__ensure_log_directories__mutmut_17, 
    'x__ensure_log_directories__mutmut_18': x__ensure_log_directories__mutmut_18, 
    'x__ensure_log_directories__mutmut_19': x__ensure_log_directories__mutmut_19, 
    'x__ensure_log_directories__mutmut_20': x__ensure_log_directories__mutmut_20, 
    'x__ensure_log_directories__mutmut_21': x__ensure_log_directories__mutmut_21, 
    'x__ensure_log_directories__mutmut_22': x__ensure_log_directories__mutmut_22, 
    'x__ensure_log_directories__mutmut_23': x__ensure_log_directories__mutmut_23
}

def _ensure_log_directories(*args, **kwargs):
    result = _mutmut_trampoline(x__ensure_log_directories__mutmut_orig, x__ensure_log_directories__mutmut_mutants, args, kwargs)
    return result 

_ensure_log_directories.__signature__ = _mutmut_signature(x__ensure_log_directories__mutmut_orig)
x__ensure_log_directories__mutmut_orig.__name__ = 'x__ensure_log_directories'
