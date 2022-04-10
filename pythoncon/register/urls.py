from django.urls import path
from .import views

urlpatterns=[

    path('',views.view_workshop, name='view_workshop'),
    path('register/',views.register, name='register'),
    path('member_details/<str:pk>/', views.member_details,name='member_details'),
    path('create_member/', views.create_member, name='create_member'),
    path('update_member/<str:pk>/', views.update_member, name='update_member'),
    path('delete/<str:pk>/',views.delete_member,name='delete_member'),
    
    #workshop paths 
    path('create_workshop/',views.create_workshop,name='create_workshop'),
    path('workshop_details/<str:pk>/',views.workshop_details,name='workshop_details')



]