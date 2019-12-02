from django.urls import path

from .views import *

urlpatterns = [
    path('', task_board, name='task_board_url'),
    path('task/create/', TaskCreate.as_view(), name='task_create_url'),
    path('task/<str:slug>/', TaskDetail, name='task_details_url'),
    path('task/<str:slug>/update/', TaskUpdate.as_view(), name='task_update_url'),
    path('task/<str:slug>/delete/', TaskDelete.as_view(), name='task_delete_url'),
    path('categories/', categories_list, name='categories_list_url'),
    path('category/create/', CategoryCreate.as_view(), name='category_create_url'),
    path('category/<str:slug>/', CategoryDetail.as_view(), name='category_details_url'),
    path('category/<str:slug>/update/', CategoryUpdate.as_view(), name='category_update_url'),
    path('category/<str:slug>/delete/', CategoryDelete.as_view(), name='category_delete_url'),
    path('main/', main_page, name='main_page_url'),
    path('bbp/', bbp, name='bbp_url'),
]
