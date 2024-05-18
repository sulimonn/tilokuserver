from django.urls import path
from api.views import *
app_name = 'api'

urlpatterns = [
    path('', index, name='index'),
    path('groups/', groups, name='groups'),
    path('groups/<int:pk>/', group, name='group'),
    path('chapters/<int:group_item>/', chapters, name='chapters'),
    path('chapters/all/<int:pk>/', chapter, name='chapter'),
    path('group-items/<int:pk>/', group_items, name='group_items'),
    path('group-items/item/<int:pk>/', group_item, name='group_item'),
    path('subchapters/<int:chapter>/', subchapters, name='subchapters'),
    path('subchapters/all/<int:pk>/', subchapter, name='subchapter'),
    path('search/', search, name='search'),
]
