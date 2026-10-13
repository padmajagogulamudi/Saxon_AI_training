import asyncio
from dataclasses import dataclass
from typing import Annotated

from semantic_kernel.connectors.in_memory import InMemoryCollection
from semantic_kernel.data.vector import VectorStoreField, vectorstoremodel


@vectorstoremodel(collection_name="employee_handbook")
@dataclass
class HandbookRecord:
    record_id: Annotated[str, VectorStoreField("key")]
    topic: Annotated[str, VectorStoreField("data")]
    content: Annotated[str, VectorStoreField("data")]
    embedding: Annotated[list[float], VectorStoreField("vector", dimensions=3)]


async def main():
    async with InMemoryCollection(record_type=HandbookRecord) as collection:   
        await collection.ensure_collection_exists()

        record = HandbookRecord(
            record_id="HR001",
            topic="Sick Leave",
            content="Employees can take sick leave when they are unwell.",
            embedding=[0.2, 0.5, 0.8]
        )

        await collection.upsert(record)

        retrieved_record = await collection.get("HR001", include_vectors=True)

        print("Topic:", retrieved_record.topic)
        print("Embedding:", retrieved_record.embedding)


if __name__ == "__main__":
    asyncio.run(main())