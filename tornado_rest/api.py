class Api:
    """
    Interface for namespaces collections with Tornado 
    """
    def __init__(self, app=None):
        if app:
            self.init_app(app)
        self._namespaces = []
 
    def add_namespace(self, namespace):
        self._namespaces.append(namespace)

    def init_app(self, app):
        for namespace in self._namespaces:
            for request_handler in namespace.request_handlers:
                app.add_handlers(r'.*', [request_handler])
