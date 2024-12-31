from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):

    """
    Serializer for registering a new user.
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    
    def save(self):
        """
        Saves the validated user data and creates a new user account.
        Performs the following:
        - Validates if the email already exists.
        - Hashes the password using Django's built-in `set_password` method.
        - Creates and saves a new user instance.
        """
        password = self.validated_data['password']

        # Check if the email is already registered.
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists!'})

        # Create a new user instance without saving immediately.
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        
        # Hash the password before saving.
        account.set_password(password)
        account.save()

        return account