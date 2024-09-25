from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .serializers import *
from django.core.mail import send_mail
from django.conf import settings

import random
from rest_framework import status
class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = []
        for user in User.objects.all():
            usernames.append(user.username )
        return Response(usernames)
    
from django.core.cache import cache
class PostBook(APIView):
    def send_email(self,subject, message, recipient_list):
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list,
            fail_silently=False,
        )
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        random_number = random.randint(1000, 9999)
        if serializer.is_valid():
            print(random_number)
            email = data['author_email']
            cache.add("otp", random_number, timeout = 300)
            cache.add('user', serializer)
            self.send_email("otp varification for post a book",
                            f"you otp for {data['name']} book is : {random_number}",
                            [email,])
            return Response(f"Otp has been send to {email}",status=status.HTTP_200_OK)
        else:
            return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)
        
class VerifyOTP(APIView):
    def post(self, request):
        import pdb;pdb.set_trace()
        data = request.data
        if data['otp'] == cache.get('otp'):
            cache.get('user').save()
            cache.clear()
            return Response("user saved", status=status.HTTP_201_CREATED)

