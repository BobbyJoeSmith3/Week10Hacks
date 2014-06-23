from django.contrib import admin
from polls.models import Poll
from polls.models import Choice


# Register your models here.
#class ChoiceInline(admin.StackedInline):
#Make the inline related objects tabular
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class PollAdmin(admin.ModelAdmin):
	#fields = ['pub_date', 'question']
	#create field sets to group forms together
	fieldsets = [
		(None,				{'fields': ['question']}),
		#('Date Information',{'fields': ['pub_date']}),
		#create a collapsable fieldset
		('Date Information',{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')
	#add a filter sidebar that let's people filter the change list by the pub_date field
	list_filter = ['pub_date']
	#add search capabilities, django will search the question field
	search_fields = ['question']


admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)
