from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.livros, name='livros'),
    path('valores/<int:id>/', views.valores, name='valores'),
    path('cadastro_livro/', views.salvar_livro, name='salvar_livro'),
    path('cadastro_valor/<int:id>/', views.salvar_valor, name='salvar_valor'),
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)