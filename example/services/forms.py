from sumo_result.services import Service

class Result:
    def __init__(self, iid, completed_at, value):
        self.id = iid
        self.completed_at = completed_at
        self.value = value

  
class Question:
    def __init__(self, iid, answered_at, answer):
        self.field = iid
        self.answer = answer


class Form:
    def __init__(self, iid):
        self.iid = iid


class FormService(Service):
    async def get_all(self):
        return {"Forms": await self.repository.get_all()}

