from django.urls import path

from . import views
app_name = 'meet'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('meet/new/', views.post_new, name='post_new'),
    path('liste/', views.liste, name='liste'),
    path('fiche/<int:pk>/', views.fiche, name='fiche'),
    path('meet/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('meet/<int:pk>/delete/', views.post_del, name='post_del'),
    path('contact/', views.contact, name='contact'),
    path('base_layout/',views.base_layout,name='base_layout'),
    path('getdata/',views.getdata,name='getdata'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    #path('new-meet/', views.new_meet, name='new-meet'),
    path('fiche/<int:pk>/', views.fiche, name='fiche'),
    path('guide/', views.guide, name='guide'),
    path('liste/', views.liste, name='liste'),
    path('contact/', views.contact, name='contact'),
    #path('login/', views.login, name='login'),
    #path('logout/', views.logout, name='logout'),
    path('base_layout/',views.base_layout,name='base_layout'),
    path('getdata/',views.getdata,name='getdata')

]
