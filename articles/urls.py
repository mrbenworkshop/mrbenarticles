from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create_article, name="create"),
    path('check-slug/', views.check_slug, name='check_slug'),
    path('<str:slug>', views.article_details, name='details'),
]
