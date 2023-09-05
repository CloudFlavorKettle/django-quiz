from django.urls import path

from roomapp import views
from roomapp.views import RoomsView

app_name = "roomapp"

urlpatterns = [
    path('', RoomsView.as_view(), name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
]