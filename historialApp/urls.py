from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    # Propietarios
    path('propietarios/', views.lista_propietarios, name='lista_propietarios'),
    path('propietarios/crear/', views.crear_propietario, name='crear_propietario'),
    path('propietarios/editar/<int:id>/', views.editar_propietario, name='editar_propietario'),
    path('propietarios/eliminar/<int:id>/', views.eliminar_propietario, name='eliminar_propietario'),

    # Mascotas
    path('mascotas/', views.lista_mascotas, name='lista_mascotas'),
    path('mascotas/crear/', views.crear_mascota, name='crear_mascota'),
    path('mascotas/editar/<int:id>/', views.editar_mascota, name='editar_mascota'),
    path('mascotas/eliminar/<int:id>/', views.eliminar_mascota, name='eliminar_mascota'),

    # Consultas
    path('consultas/', views.lista_consultas, name='lista_consultas'),
    path('consultas/crear/', views.crear_consulta, name='crear_consulta'),
    path('consultas/<int:id>/editar/', views.editar_consulta, name='editar_consulta'),
    path('consultas/<int:id>/eliminar/', views.eliminar_consulta, name='eliminar_consulta'),

    # Logout
    path('logout/', views.logout_view, name='logout'),
]

    
    
    
    
    
    
    
    
    
    
    


