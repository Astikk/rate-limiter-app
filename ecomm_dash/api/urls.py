from django.urls import path
from dashboard.views import ExcelUploadAPI, OrderAPI

urlpatterns = [
    path('excel/', ExcelUploadAPI.as_view()),
    path('order/', OrderAPI.as_view()),
]
