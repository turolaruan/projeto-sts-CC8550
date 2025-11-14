"""Serialization helpers for Mongo documents."""

from __future__ import annotations

from typing import Any, Mapping

from bson import ObjectId


def serialize_document(document: Mapping[str, Any]) -> dict[str, Any]:
    """Transform Mongo documents into API friendly dicts."""

    payload = dict(document)
    if "_id" in payload:
        payload["id"] = str(payload.pop("_id"))
    for key, value in list(payload.items()):
        if isinstance(value, ObjectId):
            payload[key] = str(value)
    return payload
