from django.contrib import admin

# Register your models here.
from .models import (Course, CourseStudent, Student, Test,
    Module, Promotion, Payment, Topic, Question, Choice, Resource)




class TopicAdmin(admin.StackedInline):
    model = Topic
    extra = 1

class ResourceAdmin(admin.StackedInline):
    model = Resource
    extra = 1

class ChoiceAdmin(admin.StackedInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceAdmin,
    ]

class ModuleAdmin(admin.ModelAdmin):
    search_fields = ('name', 'course__name')
    list_filter = ('course',)
    list_display = ('name', 'course')
    inlines = [
        TopicAdmin,
        ResourceAdmin,        
    ]

class PaymentAdmin(admin.ModelAdmin):
    search_fields = ('student__name', 'course__name')
    list_filter = ('course',)
    list_display = ('student', 'course', 'value', 'paid',)

class CourseStudentAdmin(admin.ModelAdmin):
    search_fields = ('student__name', 'course__name')
    list_filter = ('course',)
    list_display = ('student', 'course', 'completed',)

admin.site.register(Course)
admin.site.register(CourseStudent, CourseStudentAdmin)
admin.site.register(Student)
admin.site.register(Test)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Promotion)
admin.site.register(Payment, PaymentAdmin)