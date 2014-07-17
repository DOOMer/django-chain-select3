# coding: utf8

import json
from django.http import HttpResponse

class JsonResponse(HttpResponse):
    """
    JSon response for Django < 1.7
    """
    def __init__(self, content={}, mimetype=None, status=None,
             content_type='application/json'):
        super(JsonResponse, self).__init__(json.dumps(content), mimetype=mimetype,
                                           status=status, content_type=content_type)