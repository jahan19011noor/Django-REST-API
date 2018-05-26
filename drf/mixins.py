from django.http import JsonResponse

class JsonResponseMixin(object):
    def render_to_json_response(self, context, **kwargs):
        return JsonResponse(self.get_context(context), **kwargs)

    def get_context(self, context):
        return context