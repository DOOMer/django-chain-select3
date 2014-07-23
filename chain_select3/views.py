# coding: utf8

import json
from django import get_version
from django.db.models import get_model
from django.http import HttpResponse
from django.utils.encoding import force_text, force_str

try:
    from django.hhtp import JsonResponse
except ImportError:
    from .http import JsonResponse


def filterchain_all(request, app_name, model_name, method_name, pk):
    Model = get_model(app_name, model_name)
    obj = Model.objects.get(pk=pk)
    qs = getattr(obj, method_name)()
    results = list(qs)

    final = {}
    for item in results:
        final[item.pk] = force_str(item)

    if int(get_version().split(".")[1][0]) < 7:
        return JsonResponse(content=final)
    else:
        return JsonResponse(final)


