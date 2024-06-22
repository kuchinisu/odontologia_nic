from django.urls import path
from .views import ComparadorModelosModeloDentales

urlpatterns = [
    path('comparar/modelos_dentales/', ComparadorModelosModeloDentales.as_view()),
]
