from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({"message" : "Hi ther, this is your Django API response"})