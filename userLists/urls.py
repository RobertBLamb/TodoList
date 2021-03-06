from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='List-home'),
    path('about/', views.about, name='List-about'),
    path('delete/<list_id>', views.delete, name="delete"),
    path('cross_off/<list_id>/<freq>', views.cross_off, name="cross_off"),
    path('uncross/<list_id>/<freq>', views.uncross, name="uncross"),
    path('edit/<list_id>', views.edit, name="edit"),
    path('daily/', views.daily, name="daily"),
    path('once/', views.once, name="once"),
    path('weekly/', views.weekly, name="weekly"),
    path('monthly/', views.monthly, name="monthly"),
]