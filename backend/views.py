from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'index.html')

def second_page(request):
    return render(request, 'template/temp1.html')


def my_get_view(request):
    data = {'shri': 'radheKrishna'}
    return JsonResponse(data)


@csrf_exempt  # Use this decorator for simplicity in this example; consider CSRF protection in production.
def my_post_view(request):
    if request.method == 'POST':
        received_data = json.loads(request.body.decode('utf-8'))
        # Process the data as needed
        response_data = {'radhe': 'krishna'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid method'})
    
    

@csrf_exempt
def add_numbers(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        num1 = int(data.get('num1', 0))  # Parse num1 as an integer
        num2 = int(data.get('num2', 0))
        
        result = num1 + num2

        response_data = {'result': result}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid method'})