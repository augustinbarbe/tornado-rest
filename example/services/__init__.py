from abc import ABC, abstractmethod

class Service(ABC):
    def __init__(self, repository):
        self.repository = repository

    def get_by_id(self, entity_id):
        return self.repository.get(entity_id)


    def edit(self, entity_id, **entity_update):
        entity_update.pop("iid", None)
        return self.repository.edit(entity_id, **entity_update)

    def delete(self, entity_id):
        return self.repository.delete(entity_id)

    async def create(self, **entity):
        return  await self.repository.create(**entity)

