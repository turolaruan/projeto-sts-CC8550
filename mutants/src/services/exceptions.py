"""Custom exceptions raised by service layer."""


class ServiceError(Exception):
    """Base class for service level errors."""


class ValidationError(ServiceError):
    """Raised when provided data fails validation rules."""


class BusinessRuleError(ServiceError):
    """Raised when complex business constraints are violated."""


class NotFoundError(ServiceError):
    """Raised when an entity cannot be located."""
