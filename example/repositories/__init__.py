from abc import ABC, abstractmethod

class AbstractRepository(ABC):
    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def get(self, id):
        raise NotImplementedError


class MotorRepository(AbstractRepository):
    def __init__(self, db):
        if not db:
            raise MotorRepositoryError("Must provide a db instance")
        self._db = db

    @property
    @abstractmethod
    def collection(self):
        raise NotImplementedError



class MotorRepositoryError(Exception):
    pass