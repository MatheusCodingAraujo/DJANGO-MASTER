"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Contato.views import ContatoListView, ContatoCreateView, ContatoDetailView, ContatoUpdateView, ContatoDeleteView
from Accounts.views import Register_View, Login_View, Logout_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', Register_View, name='register'),
    path('login/', Login_View, name='login'),
    path('logout/', Logout_View, name='logout'),
    path('', ContatoListView.as_view(), name='Contatos_list'),
    path('Contato/', ContatoListView.as_view(), name='Contatos_list'),
    path('New_Contato/', ContatoCreateView.as_view(), name='New_Contato'),
    path('Contato/<int:pk>/', ContatoDetailView.as_view(), name='Contato_Detail'),
    path('Contato/<int:pk>/update', ContatoUpdateView.as_view(), name='Contato_update'),
    path('Contato/<int:pk>/delete', ContatoDeleteView.as_view(), name='Contato_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
