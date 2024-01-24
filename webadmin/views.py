from django.shortcuts import render
from .models import Course, Module, CourseStudent, Payment, Promotion, Student
from django.http import HttpResponse

# Create your views here.

def index(request):
    """Cria a página inicial do portal"""
    courses_list = Course.objects.order_by('-title')
    context = {'courses_list': courses_list}
    return render(request, 'index.html', context)

def course(request, slug):
    """Cria a página de um curso"""

    course = Course.objects.get(slug=slug)
    modules = Module.objects.filter(course=course)
    context = {'course': course,
               'modules': modules
               }
        
    if request.method == 'POST':
        email = request.session.get('email', None)

        if email is None:
            return render(request, 'login.html', context)

        student = Student.objects.get(email=email)
        zero_promotion = Promotion.objects.get(description='zero')
        
        payment = Payment(
            value = course.price,
            paid = False,
            promotion = zero_promotion,
            student = student,
            course = course,
            recurrent = False,
        )
        if request.POST.get('promotion', None) is not None:
            promotion = Promotion.objects.get(description=request.POST.get('promotion'))
            payment.promotion = promotion
            payment.value = payment.value - (payment.value * promotion.percent / 100)
        payment.save()
        
    
    return render(request, 'course.html', context)


def my_courses(request):
    """Cria a página de meus cursos"""
    email = request.session.get('email', None)
    if email is None:
        return render(request, 'login.html', {})
    
    student = Student.objects.get(email=email)
    courses = CourseStudent.objects.filter(student=student)
    context = {'courses_list': courses}
    return render(request, 'my_courses.html', context)


def lessons(request, slug):
    """Cria a página de um curso"""

    email = request.session.get('email', None)
    if email is None:
        return render(request, 'login.html', {})

    course = Course.objects.get(slug=slug)
    modules = Module.objects.filter(course=course)
    context = {'course': course,
               'modules': modules
               }
        
    
    return render(request, 'lesson.html', context)


## Authentication methods

def login(request):
    """Cria a página de login"""
    if request.method == 'POST':
        user = Student.objects.get(email=request.POST.get('email'))
        if user.password == request.POST.get('password'):
            request.session['username'] = user.name
            request.session['email'] = user.email
            if not request.POST.get('remember_me', False):
                request.session.set_expiry(0)
            return render(request, 'index.html', {'courses_list': Course.objects.order_by('-title')})
        else:
            return render(request, 'login.html', {'error_message': 'Senha inválida'})
    else:
        return render(request, 'login.html', {})


def logout(request):
    """Cria a página de logout"""
    request.session['username'] = None
    request.session['email'] = None
    return render(request, 'index.html', {'courses_list': Course.objects.order_by('-title')})


def register(request):
    """Cria a página de registro"""
    if request.method == 'POST':
        if request.POST.get('password1') != request.POST.get('password2'):
            return render(request, 'register.html', {'error_message': 'Senhas não conferem'})
        
        user = Student(
            name = request.POST.get('nome'),
            email = request.POST.get('email'),
            password = request.POST.get('password1'),
            phone = request.POST.get('telefone'),
            address = request.POST.get('endereco'),
        )
        try:
            user.save()
            request.session['username'] = user.name
            request.session['email'] = user.email
            return render(request, 'index.html', {'courses_list': Course.objects.order_by('-title'), 'success_message': 'Usuário cadastrado com sucesso'})
        except:
            return render(request, 'register.html', {'error_message': 'Email já cadastrado'})
    else:
        return render(request, 'register.html', {})