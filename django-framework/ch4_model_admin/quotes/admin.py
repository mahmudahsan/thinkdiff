from django.contrib import admin

from . models import QuoteCategory
from . models import Quote 

admin.site.register(QuoteCategory)
admin.site.register(Quote)
