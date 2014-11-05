# coding: utf8

import json
from django.http import HttpResponse

class JsonResponse(HttpResponse):
    """
    JSon response for Django < 1.7
    """
    def __init__(self, content={}, mimetype=None, status=None,
             content_type='application/json'):
<<<<<<< HEAD
        super(JsonResponse, self).__init__(json.dumps(content), mimetype,status, content_type)
=======
        super(JsonResponse, self).__init__(json.dumps(content), mimetype=mimetype,
                                           status=status, content_type=content_type)
>>>>>>> 3bce64880d8dfd9f105a860adeaf501b714864dd
