from django.shortcuts import render
from .models import Course

# Create your views here.

def index(request):
    """Cria a página inicial do portal"""
    courses_list = Course.objects.order_by('-title')
    context = {'courses_list': courses_list}
    return render(request, 'index.html', context)