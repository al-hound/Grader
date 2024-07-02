from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index_view, name='index'),
    path('student/<int:student_id>/', views.student_detail_view, name='student_detail'),
]
