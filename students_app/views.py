from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import studentSerializers
from.models import Students
from rest_framework.response import Response
from rest_framework import status



class StudentsList(APIView):
    def authenticate(self, request):
        username = request.headers.get('Username')
        password = request.headers.get('Password')
        return username == 'admin' and password == 'PWD'
    def get(self,request):

        students = Students.objects.all()
        serializer= studentSerializers(students,many=True)
        return Response(serializer.data)

    def post(self,request):
        if not self.authenticate(request):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        serializer  = studentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentByID(APIView):

    def authenticate(self, request):
        username = request.headers.get('Username')
        password = request.headers.get('Password')
        return username == 'admin' and password == 'PWD'

    def get_object(self,pk):
        return Students.objects.get(pk=pk)

    def get(self,request,pk):
        students_obj = self.get_object(pk)
        serializer_obj = studentSerializers(students_obj)
        return Response(serializer_obj.data)

    def put(self,request,pk):

        if not self.authenticate(request):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        students_obj = self.get_object(pk)
        serializer_obj = studentSerializers(students_obj,data=request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return  Response(serializer_obj.data,status=status.HTTP_200_OK)
        return Response(serializer_obj.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):

        if not self.authenticate(request):
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

        students_obj=self.get_object(pk)
        students_obj.delete()
        return  Response( status=status.HTTP_204_NO_CONTENT)

    def tried(self):
        print('ggggggg')