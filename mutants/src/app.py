"""Application factory for the FastAPI service."""

from fastapi import FastAPI

from src.config import Settings, get_settings
from src.controllers import register_controllers
from src.database.mongo import mongo_manager
from src.utils.logging_config import configure_logging
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


def x_create_app__mutmut_orig(settings: Settings | None = None) -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app_settings = settings or get_settings()
    configure_logging(app_settings)

    app = FastAPI(
        title=app_settings.app_name,
        debug=app_settings.debug,
        version="0.1.0",
    )
    app.state.settings = app_settings

    register_controllers(app)

    @app.on_event("startup")
    async def startup() -> None:
        await mongo_manager.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await mongo_manager.close()

    return app


def x_create_app__mutmut_1(settings: Settings | None = None) -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app_settings = None
    configure_logging(app_settings)

    app = FastAPI(
        title=app_settings.app_name,
        debug=app_settings.debug,
        version="0.1.0",
    )
    app.state.settings = app_settings

    register_controllers(app)

    @app.on_event("startup")
    async def startup() -> None:
        await mongo_manager.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await mongo_manager.close()

    return app


def x_create_app__mutmut_2(settings: Settings | None = None) -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app_settings = settings and get_settings()
    configure_logging(app_settings)

    app = FastAPI(
        title=app_settings.app_name,
        debug=app_settings.debug,
        version="0.1.0",
    )
    app.state.settings = app_settings

    register_controllers(app)

    @app.on_event("startup")
    async def startup() -> None:
        await mongo_manager.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await mongo_manager.close()

    return app


def x_create_app__mutmut_3(settings: Settings | None = None) -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app_settings = settings or get_settings()
    configure_logging(None)

    app = FastAPI(
        title=app_settings.app_name,
        debug=app_settings.debug,
        version="0.1.0",
    )
    app.state.settings = app_settings

    register_controllers(app)

    @app.on_event("startup")
    async def startup() -> None:
        await mongo_manager.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await mongo_manager.close()

    return app


def x_create_app__mutmut_4(settings: Settings | None = None) -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app_settings = settings or get_settings()
    configure_logging(app_settings)

    app = None
    app.state.settings = app_settings

    register_controllers(app)

    @app.on_event("startup")
    async def startup() -> None:
        await mongo_manager.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await mongo_manager.close()

    return app


def x_create_app__mutmut_5(settings: Settings | None = None) -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app_settings = settings or get_settings()
    configure_logging(app_settings)

    app = FastAPI(
        title=None,
        debug=app_settings.debug,
        version="0.1.0",
    )
    app.state.settings = app_settings

    register_controllers(app)

    @app.on_event("startup")
    async def startup() -> None:
        await mongo_manager.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await mongo_manager.close()

    return app


def x_create_app__mutmut_6(settings: Settings | None = None) -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app_settings = settings or get_settings()
    configure_logging(app_settings)

    app = FastAPI(
        title=app_settings.app_name,
        debug=None,
        version="0.1.0",
    )
    app.state.settings = app_settings

    register_controllers(app)

    @app.on_event("startup")
    async def startup() -> None:
        await mongo_manager.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await mongo_manager.close()

    return app


def x_create_app__mutmut_7(settings: Settings | None = None) -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app_settings = settings or get_settings()
    configure_logging(app_settings)

    app = FastAPI(
        title=app_settings.app_name,
        debug=app_settings.debug,
        version=None,
    )
    app.state.settings = app_settings

    register_controllers(app)

    @app.on_event("startup")
    async def startup() -> None:
        await mongo_manager.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await mongo_manager.close()

    return app


def x_create_app__mutmut_8(settings: Settings | None = None) -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app_settings = settings or get_settings()
    configure_logging(app_settings)

    app = FastAPI(
        debug=app_settings.debug,
        version="0.1.0",
    )
    app.state.settings = app_settings

    register_controllers(app)

    @app.on_event("startup")
    async def startup() -> None:
        await mongo_manager.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await mongo_manager.close()

    return app


def x_create_app__mutmut_9(settings: Settings | None = None) -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app_settings = settings or get_settings()
    configure_logging(app_settings)

    app = FastAPI(
        title=app_settings.app_name,
        version="0.1.0",
    )
    app.state.settings = app_settings

    register_controllers(app)

    @app.on_event("startup")
    async def startup() -> None:
        await mongo_manager.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await mongo_manager.close()

    return app


def x_create_app__mutmut_10(settings: Settings | None = None) -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app_settings = settings or get_settings()
    configure_logging(app_settings)

    app = FastAPI(
        title=app_settings.app_name,
        debug=app_settings.debug,
        )
    app.state.settings = app_settings

    register_controllers(app)

    @app.on_event("startup")
    async def startup() -> None:
        await mongo_manager.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await mongo_manager.close()

    return app


def x_create_app__mutmut_11(settings: Settings | None = None) -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app_settings = settings or get_settings()
    configure_logging(app_settings)

    app = FastAPI(
        title=app_settings.app_name,
        debug=app_settings.debug,
        version="XX0.1.0XX",
    )
    app.state.settings = app_settings

    register_controllers(app)

    @app.on_event("startup")
    async def startup() -> None:
        await mongo_manager.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await mongo_manager.close()

    return app


def x_create_app__mutmut_12(settings: Settings | None = None) -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app_settings = settings or get_settings()
    configure_logging(app_settings)

    app = FastAPI(
        title=app_settings.app_name,
        debug=app_settings.debug,
        version="0.1.0",
    )
    app.state.settings = None

    register_controllers(app)

    @app.on_event("startup")
    async def startup() -> None:
        await mongo_manager.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await mongo_manager.close()

    return app


def x_create_app__mutmut_13(settings: Settings | None = None) -> FastAPI:
    """Instantiate and configure FastAPI application."""
    app_settings = settings or get_settings()
    configure_logging(app_settings)

    app = FastAPI(
        title=app_settings.app_name,
        debug=app_settings.debug,
        version="0.1.0",
    )
    app.state.settings = app_settings

    register_controllers(None)

    @app.on_event("startup")
    async def startup() -> None:
        await mongo_manager.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        await mongo_manager.close()

    return app

x_create_app__mutmut_mutants : ClassVar[MutantDict] = {
'x_create_app__mutmut_1': x_create_app__mutmut_1, 
    'x_create_app__mutmut_2': x_create_app__mutmut_2, 
    'x_create_app__mutmut_3': x_create_app__mutmut_3, 
    'x_create_app__mutmut_4': x_create_app__mutmut_4, 
    'x_create_app__mutmut_5': x_create_app__mutmut_5, 
    'x_create_app__mutmut_6': x_create_app__mutmut_6, 
    'x_create_app__mutmut_7': x_create_app__mutmut_7, 
    'x_create_app__mutmut_8': x_create_app__mutmut_8, 
    'x_create_app__mutmut_9': x_create_app__mutmut_9, 
    'x_create_app__mutmut_10': x_create_app__mutmut_10, 
    'x_create_app__mutmut_11': x_create_app__mutmut_11, 
    'x_create_app__mutmut_12': x_create_app__mutmut_12, 
    'x_create_app__mutmut_13': x_create_app__mutmut_13
}

def create_app(*args, **kwargs):
    result = _mutmut_trampoline(x_create_app__mutmut_orig, x_create_app__mutmut_mutants, args, kwargs)
    return result 

create_app.__signature__ = _mutmut_signature(x_create_app__mutmut_orig)
x_create_app__mutmut_orig.__name__ = 'x_create_app'
