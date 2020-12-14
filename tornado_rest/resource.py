from tornado.web import RequestHandler

class Resource(RequestHandler):    
    def initialize(self, service, repository):
        repository = repository(self.settings.get("db", None))
        # self.repository = repository
        self.service = service(repository)
