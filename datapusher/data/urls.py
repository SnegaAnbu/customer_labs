from django.urls import path, include
from rest_framework.routers import DefaultRouter # type: ignore
from .views import AccountViewSet, DestinationViewSet, get_destinations, incoming_data

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'destinations', DestinationViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('get_destinations/<uuid:account_id>/', get_destinations, name='get_destinations'),
    path('server/incoming_data/', incoming_data, name='incoming_data'),
]
