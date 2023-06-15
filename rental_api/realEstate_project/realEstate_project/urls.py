"""realEstate_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from api.views import UserViewSet, CreatePropertyView, UpdatePropertyView, DeletePropertyView, PropertyViewSet, PropertySearchViewSet,PropertyListViewSet, AgentNameViewSet, AgentDetailsViewSet, AgentPropertiesView, AgentCommentView, AgentRatingCreateView
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register(r'agent-details', AgentDetailsViewSet, basename='agent details')
router.register(r'agents', AgentNameViewSet, basename='agents')
router.register(r'properties-list', PropertyListViewSet, basename='properties')
router.register(r'properties', PropertyViewSet, basename='properties')
router.register(r'properties-search',PropertySearchViewSet, basename='properties-search')

urlpatterns = [
    # ...
    path('api/auth/', include('djoser.urls')),
    path('api/agents/<int:agent_id>/properties/', AgentPropertiesView.as_view(), name='agent-properties'),
    path('agents/<int:agent_id>/rate/', AgentRatingCreateView.as_view(), name='rate-agent'),
    path('api/agents/<int:agent_id>/comments/', AgentCommentView.as_view(), name='agent-comments'),
    path('api/auth/', include('djoser.urls.authtoken')),
    path('api/', include(router.urls)),
    path('properties/', CreatePropertyView.as_view(),  name='create-property'),
    path('properties/<int:pk>/', UpdatePropertyView.as_view(), name='update-property'),
    path('properties/<int:pk>/delete/', DeletePropertyView.as_view(), name='delete-property')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


