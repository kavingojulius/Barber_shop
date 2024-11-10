from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from .views import *

######################################

urlpatterns =[

    path('', index_page , name='index'),
    path('form/', form_page , name='form'),
    path('details/', details , name='details'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete , name='delete'),
    path('sign', SignPage, name='signup'),
    path('login/', CustomLoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout')

]