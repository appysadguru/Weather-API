from hw2.models import Book
from hw2.serializers import BookSerializer, BookSerializer2
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import datetime
#from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from django.shortcuts import render

@api_view(['GET', 'POST'])
def record_list(request):
    if request.method == 'GET':
        record = Book.objects.all()
        ser_record = BookSerializer2(record, many=True)
        return Response(ser_record.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        copy1 = request.data.copy()
        q1 = Book.objects.filter(DATE=copy1['DATE'])
        if q1:
            q1.delete()
           
        ser_record = BookSerializer(data=request.data)
        if ser_record.is_valid():
            ser_record.save()
            return Response(ser_record.data, status=status.HTTP_201_CREATED)
        return Response(ser_record.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE'])
def record_detail(request, dt):
    try:
        record = Book.objects.get(DATE=dt)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        ser_record = BookSerializer(record)
        return Response(ser_record.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 