from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Update

#def detial_view(request):
    #return render(request, template_name, context_in_dict_form) # return JSON data  --> JS Object Notion
    # example
        # return render(request, "detail_view.html", {"some_key": "some_value", "some_other_key": "some_other_value"})
            # the context gets converted to JSON data
    #return HttpResponse(get_template("template_path").render({},request)) --> does the same

def detail_view(request):

    data = {
        "count": 1000,
        "content": "Some new content",
        "boolean": True
    }
    return JsonResponse(data)