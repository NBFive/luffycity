from django.http import HttpResponse


class MiddlewareMixin:
    def __init__(self,get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin,self).__init__()

    def __call__(self,request):
        response = None
        if hasattr(self,'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self,'process_response'):
            response = self.process_response(request,response)
        return response

class M1(MiddlewareMixin):
    def process_request(self, request, *args, **kwargs):
        if request.method=='OPTIONS':
            response = HttpResponse()
            response['Access-Control-Allow-Origin'] = "*"
            response['Access-Control-Allow-Methods'] = "GET"
            response['Access-Control-Allow-Headers'] = "Content-Type"
            return response

    def process_response(self,request,response):
        response['Access-Control-Allow-Origin'] = '*'
        return response