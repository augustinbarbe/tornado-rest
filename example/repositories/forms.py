from sumo_result.services.forms import Result, Question, Form
from sumo_result.repositories import MotorRepository

class FormRepository(MotorRepository):
    async def create(self, iid):
        form = Form(iid=iid)
        created =  await self.collection.insert_one(form.__dict__)
        return form

    @property
    def collection(self):
        return self._db.results

    async def get_all(self, limit=100, page=1):
        form_collection = self.collection.find({})
        return [ Form(iid=form.get("iid")) for form in await form_collection.to_list(length=limit)]


    def get(self, id):
        return None
