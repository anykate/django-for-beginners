from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('<int:post_id>/details/', views.BlogDetailView.as_view(), name='details'),
]
