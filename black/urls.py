"""black URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from listing import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.DashboardHome.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('opportunity-upload/', views.OpportunityUploadView.as_view(), name='upload'),
    # path('search/', views.SearchView.as_view(), name='search'),
    path('opportunity-detail/<int:pk>/', views.OpportunityDetailView.as_view(), name='opportunity-detail-view'),
    # path('mandate-detail/<int:pk>/', views.MandateDetailView.as_view(), name='mandate-detail-view'),
    path('mandate-upload/', views.MandateUploadView.as_view(), name='mandate_upload'),
    # path('fund-seeking/', views.AllMandate.as_view(), name='mandate-all'),
    # path('opportunity/', views.AllOpportunity.as_view(), name='opportunity-all'),

    path('ajax/load-geography/', views.load_cities, name='ajax_load_geography'),
    path('ajax/load-sector/', views.load_sectors, name='ajax_load_sector'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
