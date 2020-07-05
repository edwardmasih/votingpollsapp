from django.contrib import admin

# Register your models here.

from .models import Question, Choice

# site-header
admin.site.site_header = 'Voting Admin'
admin.site.site_title = 'Voting Admin Area'
admin.site.index_title = 'Polls Admin'

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 5


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None,{'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInLine]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
