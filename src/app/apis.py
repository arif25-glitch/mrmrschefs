from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.BaseDirApi, name='base_api'),
    path('user', views.User),
    path('receipt', views.Receipt),
    path('transaction', views.Transaction),
]