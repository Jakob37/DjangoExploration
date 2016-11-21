from django.contrib import admin

from .models import Choice, Question

# admin.site.register(Question)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# Common pattern: Create admin class and pass it as second argument to register method
class QuestionAdmin(admin.ModelAdmin):
    # Adjusting order of the fields
    # fields = ['pub_date', 'question_text']

    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

