from rest_framework import serializers

from quotes.models import Quote
from quotes.models import QuoteCategory 

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote 
        # ('__all__')  for all fields
        # ['quote', 'author']
        fields = ['quote', 'author']

class QuoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteCategory 
        # ('__all__')  for all fields
        # ['title']
        fields = ('__all__')