from django.contrib import admin
from .models import Question,Choise
# Register your models here.

class ChoiceInline(admin.TabularInline):
    '''One small problem, though. It takes a lot of screen space to display all the fields for entering related Choice objects. For that reason, Django offers a tabular way of displaying inline related objects. To use it, change the ChoiceInline declaration to read:'''
    model = Choise
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
     fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
     inlines = [ChoiceInline]
     '''By default, Django displays the str() of each object. But sometimes it’d be more helpful if we could display individual fields. To do that, use the list_display admin option, which is a tuple of field names to display, as columns, on the change list page for the object:
     '''
     list_display = ["question_text", "pub_date"]
     list_filter = ["pub_date"]


admin.site.register(Question,QuestionAdmin)
'''This is insufient to call choices bcoz it list out all choices in admin page but not load in question wise'''
# admin.site.register(Choise)
