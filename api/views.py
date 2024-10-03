from django.shortcuts import render
# myapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import ContactFormSerializer,ImageSerializer, AchivitaContactFormSerializer
from django.core.mail import send_mail
from .models import ImageModel


class ContactFormView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            # Example: Send an email with the form data
            # send_mail(
            #     'Contact Form Submission',
            #     serializer.data['message'],
            #     serializer.data['email'],
            #     ['chinecheremvalarian@gmail.com'],  # Replace with your email
            # )
            return Response({"message": "Form submitted successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AchivitaContactFormView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AchivitaContactFormSerializer(data=request.data)
        if serializer.is_valid():
            # Example: Send an email with the form data
            # send_mail(
            #     'Contact Form Submission',
            #     serializer.data['message'],
            #     serializer.data['email'],
            #     ['chinecheremvalarian@gmail.com'],  # Replace with your email
            # )
            return Response({"message": "Form submitted successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer


def index(request, resource=None):
    return render(request, 'index.html')

# index2 == achivita 
def index2(request, resource=None):
    return render(request, 'index2.html')