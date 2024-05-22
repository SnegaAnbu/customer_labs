from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer
import requests 

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

@api_view(['GET'])
def get_destinations(request, account_id):
    try:
        account = Account.objects.get(account_id=account_id)
        destinations = account.destinations.all()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)
    except Account.DoesNotExist:
        return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def incoming_data(request):
    app_secret_token = request.headers.get('CL-X-TOKEN')
    
    if not app_secret_token:
        return Response({"message": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        account = Account.objects.get(app_secret_token=app_secret_token)
    except Account.DoesNotExist:
        return Response({"message": "Unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'POST':
        data = request.data
        destinations = account.destinations.all()
        
        for destination in destinations:
            headers = destination.headers
            if destination.http_method == 'GET':
                response = requests.get(destination.url, headers=headers, params=data)
            else:
                response = requests.request(method=destination.http_method, url=destination.url, headers=headers, json=data)
            
            # Optionally, you can log or handle the response from each destination.
            # Example: print(response.status_code, response.text)

        return Response({"message": "Data sent to destinations"}, status=status.HTTP_200_OK)
    
    return Response({"message": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST)