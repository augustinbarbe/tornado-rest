class Namespace:
    """
        Collection of resources sharing the same domain
        name : identifyer of the namespace. 
               Resources are adressed with 
    """
    def __init__(self, name, service, repository):
        self.name = name
        self._request_handlers = []
        self.service = service
        self.repository = repository

    @property
    def request_handlers(self):
        return self._request_handlers

    def route(self, url):
        """
        A decorator to link route to handler resources.
        """

        def wrapper(cls):
            self._add_request_handlers(cls, url)
            return cls

        return wrapper


    def marshal_with(self, model):
        """
            Decorate route to serialize and write response given a model
        """
        def decorator(function):
            def wrapper(*args, **kwargs):
                function()
                return result
            return wrapper
        return decorator


    
    def marshal_list_with(self, model, enveloppe):
        """
        A decorator to marshal entities returned as a list from service layer given a model.
        """
        def wrapper(fn, *args, **kwargs):
            import pdb; pdb.set_trace()
            fn(*args, **kwargs)

        return wrapper

    def _add_request_handlers(self, cls, url):
        if not url.startswith('/'):
            raise NamespaceError("url rule must start with '/'")
        
        self._request_handlers.append((f"/{self.name}{url}", cls, dict(service=self.service, repository=self.repository)))



class NamespaceError(Exception):
    pass
