from mongoengine import Document
from pymongo import UpdateOne

from typing import List


class NoSqlRepository():
    document = Document

    def __init__(self, connection) -> None:
        self.connection = connection

    def upsert_one(self, object: dict, filter: dict):
        self.document.objects(**filter).update_one(**object, upsert=True)

    def upsert_many(self, objects: List[dict], filters: dict):
        operations = []

        for obj in objects:
            operations.append(UpdateOne(filter=filters, update=obj, upsert=True))

        self.document._get_collection().bulk_write(operations, ordered=False)
