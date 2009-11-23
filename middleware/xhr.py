class XHRMiddleware(object):
    def process_request(self, request):
        request.is_xhr = request.REQUEST.has_key('xhr') and request.REQUEST['xhr'] == '1'
        return None
