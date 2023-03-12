from django.urls import path
from product_info_wb import views


urlpatterns = [
    path("upload/", views.FileUploadView.as_view()),
]
