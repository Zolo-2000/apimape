from django.shortcuts import render
from django.http import JsonResponse


def Index(request):
    return render(request, 'jsolorzano/index.html')