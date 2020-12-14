

from sumo_result.apis.api import Namespace, Resource
from sumo_result.services.forms import FormService
from sumo_result.repositories.forms import FormRepository

from sumo_result.services.forms import Form

api = Namespace("forms", FormService, FormRepository)


@api.route("/")
class Results(Resource):
    async def get(self):
        self.write(await self.service.get_all())


@api.route("/create")
class ResultCreate(Resource):

    @api.marshal_with(Form)
    async def get(self):
        created = await self.service.create(iid="test")
        self.write(created.__dict__)
