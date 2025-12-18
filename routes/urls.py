from django.urls import path
from . import views

urlpatterns = [
    path('add-airport/', views.add_airport),
    path('add-route/', views.add_airport_route),
    path('nth-node/', views.nth_node_view),
    path('longest-node/', views.longest_node_view),
    path('shortest-path/', views.shortest_path_view),
]
