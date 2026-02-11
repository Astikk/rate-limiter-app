from django.urls import path
from dashboard.views import ExcelUploadAPI, OrderAPI, loginAPI

urlpatterns = [
    path('login/', loginAPI.as_view()),
    path('excel/', ExcelUploadAPI.as_view()),
    path('order/', OrderAPI.as_view()),
]
