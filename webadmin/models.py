from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    banner = models.ImageField(upload_to='course')

    def __str__(self):
        return self.title   
    

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course, through='CourseStudent')

    def clean(self):
        """Garante que idUnidadeSuperior não seja atribuída a sí mesma."""
        if self.name == self.email:
            raise ValidationError("Não é permitido email e nomes iguais")
    
    def __str__(self):
        return self.name

class Test(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)    
    description = models.TextField()
    grade = models.FloatField()
    completed = models.BooleanField()

    def __str__(self):
        return self.description[:50]

class CourseStudent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.DO_NOTHING)
    rate = models.IntegerField(null=True)
    comments = models.TextField(null=True)
    completed = models.BooleanField()
    grade = models.IntegerField()

class Module(models.Model):
    name = models.CharField(max_length=255)    
    completed = models.BooleanField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #topics = models.ManyToManyField(Topic, through='TopicModule')
    #questions = models.ManyToManyField(Question, through='QuestionModule')

    def __str__(self):
        return self.name

class Topic(models.Model):
    title = models.CharField(max_length=255)
    video = models.CharField(max_length=250)
    duration = models.IntegerField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Question(models.Model):
    description = models.TextField()
    comment = models.CharField(max_length=50)    
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class Choice(models.Model):
    description = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.BooleanField()

    def __str__(self):
        return self.description

class Resource(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    percent = models.FloatField()

    def __str__(self):
        return self.description

class Payment(models.Model):
    value = models.FloatField()
    paid = models.BooleanField(null=True)
    payment_date = models.DateField()
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)

    def __str__(self):
        return self.value

