from dataclasses import dataclass
from enum import Enum

from src.utils.db_operations.db_operations import BnFMongoManager


@dataclass
class CollectionAttributes:
    collection_name: str
    connection: BnFMongoManager


class Collections(Enum):
    theater: CollectionAttributes = CollectionAttributes(
        collection_name="Theatre", connection=None
    )
    slots: CollectionAttributes = CollectionAttributes(
        collection_name="Slots", connection=None
    )
    decorations: CollectionAttributes = CollectionAttributes(
        collection_name="Decorations", connection=None
    )
    addons: CollectionAttributes = CollectionAttributes(
        collection_name="Addons", connection=None
    )
    coupons: CollectionAttributes = CollectionAttributes(
        collection_name="Coupons", connection=None
    )
    bookings: CollectionAttributes = CollectionAttributes(
        collection_name="Bookings", connection=None
    )
    roles: CollectionAttributes = CollectionAttributes(
        collection_name="Roles", connection=None
    )
    packages: CollectionAttributes = CollectionAttributes(
        collection_name="Packages", connection=None
    )
    communications: CollectionAttributes = CollectionAttributes(
        collection_name="CommunicationTemplates", connection=None
    )
