from django.db.migrations import serializer
from django.shortcuts import get_object_or_404
from .models import Alert
from .serializers import AlertSerializer
from rest_framework import viewsets, filters, generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.mail import send_mail
from django.conf import settings

class AlertList(generics.ListAPIView):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()


class AlertDetail(generics.RetrieveAPIView):
    serializer_class = AlertSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Alert, id=item)


class CreateAlert(APIView):

    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):

        serializer = AlertSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminAlertDetail(generics.RetrieveAPIView):

    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

    
class EditAlert(generics.UpdateAPIView):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()


class DeleteAlert(generics.RetrieveDestroyAPIView):
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()



