from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^order/', views.order, name='order'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^sign_up/', views.sign_up, name='sign_up'),
    url(r'^task/', views.task_show, name='task_show'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^AddSkill/', views.AddSkill, name='AddSkill'),
    url(r'^EditProfile/', views.EditProfile, name='EditProfile'),
    url(r'^JobFind/', views.JobFind, name='JobFind'),

]