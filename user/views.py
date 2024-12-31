from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegistrationSerializer


@api_view(['POST',])
def registration_view(request):
    """
        API endpoint for user registration.
        Handles user account creation, validation, and token generation.
    """
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        # Dictionary to store the response data
        data = {}
       
        # Check if the provided data is valid based on the serializer's rules.
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email

            # Generate JWT tokens for the newly registered user.
            refresh = RefreshToken.for_user(account)
            
            data['token'] = {
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                            }
       
        else:
            # If the serializer data is invalid, include the errors in the response
            data = serializer.errors
        
        # Return the response with a status of 201 (Created) for valid registration.
        return Response(data, status=status.HTTP_201_CREATED)