from django.urls import path

from .views import QuoteAPIView
from .views import QuoteCategoryAPIView
from .views import QuoteAPIDetailView
from .views import QuoteAPINewView

urlpatterns = [
    path('', QuoteCategoryAPIView.as_view()),
    path('quotes/', QuoteAPIView.as_view()),
    path('quotes/<int:pk>/', QuoteAPIDetailView.as_view()),
    path('quotes/new/', QuoteAPINewView.as_view()),
]