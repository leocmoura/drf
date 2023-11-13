from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    header = request.headers
    body = request.body
    print(header)
    print('------------------------')
    print(body)
    return JsonResponse({'message': 'hello view'})
    