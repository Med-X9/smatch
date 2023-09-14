from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('Apropos',AboutView.as_view(),name='about'),
    path('Contact',ContactView.as_view(),name='contact'),
    path('ERP',ErpView.as_view(),name='erp'),
    
    path('projets/', ListeProjetsView.as_view(), name='project'),
    path('projet/<slug:slug>/', ProjetDetailView.as_view(), name='detail_projet'),

    # URL pour afficher les détails d'un projet spécifique en fonction de son ID
    # path('projet/<slug:slug>/', views.detail_projet, name='detail_projet'),
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)