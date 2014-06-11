# coding: utf8

from django.db.models import get_model
from django.http import HttpResponse, JsonResponse
from django.utils.encoding import force_text, force_str


def filterchain_all(request, app_name, model_name, method_name, pk):
    Model = get_model(app_name, model_name)
    obj = Model.objects.get(pk=pk)
    qs = getattr(obj, method_name)()
    results = list(qs)

    final = {}
    for item in results:
        final[item.pk] = force_str(item)

    return JsonResponse(final)
