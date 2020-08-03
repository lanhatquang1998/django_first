from django.urls import path
from appTwo import views

#TEMPALTE TAGGING
app_name = 'appTwo'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
    path('registration/',views.register,name='registration'),
    path('user_login/',views.user_login,name='user_login'),
]
