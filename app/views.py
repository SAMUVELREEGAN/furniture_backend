from django.shortcuts import render
from .models import AboutModel
from rest_framework import status
from .serializers import *
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.
class AboutModelView(APIView):
    def get(self, request):
        about_datas = AboutModel.objects.last()
        print(about_datas)
        
        if about_datas:
            about_data = {
                "id": about_datas.id,
                "about_story_img": about_datas.about_story_img.url if about_datas.about_story_img else None,
                "card_1_img": about_datas.card_1_img.url if about_datas.card_1_img else None,
                "card_2_img": about_datas.card_2_img.url if about_datas.card_2_img else None,
                "card_3_img": about_datas.card_3_img.url if about_datas.card_3_img else None,
                "card_4_img": about_datas.card_4_img.url if about_datas.card_4_img else None,
                "designer_img": about_datas.designer_img.url if about_datas.designer_img else None
            }
            print(about_data)
            return Response(about_data)
        else:
            return Response({"error": "No about data found."}, status=status.HTTP_404_NOT_FOUND)
        
class ContactUsModelView(APIView):
    
    def post (self,request):
        contact_serializer = ContactUsMessageSerializer(data = request.data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            
            # send email
            
            subject = contact_serializer.validated_data.get('subject')
            
            message = contact_serializer.validated_data.get('message')
            
            name = contact_serializer.validated_data.get('name')
            
            email = contact_serializer.validated_data.get('email')
            
            ph_number = contact_serializer.validated_data.get('ph_number')
            
            full_message = f"""
            Name:{name}
            Phone_number:{ph_number}
            Email:{email}
            
            Message:
            {message}
            """
            
            send_mail(
                
                f'Contact Us: {subject}',
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
                fail_silently=False
            )
            return Response({'message':'message sent succesfully'},status=status.HTTP_201_CREATED)
        return Response(contact_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactSettingModelView(APIView):
    
    def get(self, request):
        last_contact = ContactSettingModel.objects.last()
        if last_contact:
            contact_img = ContactSetiingSerializer(last_contact)
            print(contact_img.data)
            return Response(contact_img.data)
        else:
            return Response({"detail": "No contact settings found."}, status=404)