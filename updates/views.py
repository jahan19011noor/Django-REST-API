import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from django.core.serializers import serialize
from .models import Update
from drf.mixins import JsonResponseMixin

#def detial_view(request):
    #return render(request, template_name, context_in_dict_form) # return JSON data  --> JS Object Notion
    # example
        # return render(request, "detail_view.html", {"some_key": "some_value", "some_other_key": "some_other_value"})
            # the context gets converted to JSON data
    #return HttpResponse(get_template("template_path").render({},request)) --> does the same
    # sent content type to specify type of context return:
        # HttpResponse("Text only, please.", content_type="text/plain")

def json_response_view(request):

    data = {
        "count": 1000,
        "content": "Some new content",
        "boolean": True
    }
    # If safe is set to False, any object can be passed for serialization (otherwise only dict instances are allowed)
        # example:
        # return JsonResponse("test string", safe=False)

    # default Content-Type header is set to application/json.
    return JsonResponse(data)


def http_response_view(request):
    data = {
        "count": 1000,
        "content": "Some new content",
        "boolean": True
    }

    json_data = json.dumps(data)

    # sent content_type to specify type of context return:
        # HttpResponse("Text only, please.", content_type="text/plain")

    return HttpResponse(json_data, content_type="application/json")

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content",
            "boolean": True
        }

        return JsonResponse(data)

class JsonResponseMixinView(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content",
            "boolean": True
        }

        # return self.render_to_json_response("test data", safe=False)
        return self.render_to_json_response(data)

class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = serialize('json', [obj, ], fields=('user', 'content'))

        return HttpResponse(json_data, content_type='application/json')

class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        obj_list = Update.objects.all()
        json_data = serialize("json", obj_list, fields=('user', 'content'))

        return HttpResponse(json_data, content_type="application/json")