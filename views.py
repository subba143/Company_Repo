from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
import os
#import josn
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.
class Employee_APIview(APIView):
    def get(self, request, format=None):
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs, many=True)
        return Response(serializer.data)


    def get_id(self,request,pk = None):

        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs, many=True)
        return Response(serializer.data)
        def  serializer.object.get(id):
            if Employee.data():
                return response(serializer.data,'Employee Details Particularly Record Successfully Retrieve ',status = 204)
            else:
                Employee.data is None
                return response(serializer.data,'Employee Details Particularly Not_Successfully Delete,Plz Try Again',status = 500)



    def post(self,request,format=None):
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs, many=True)
        return Response(serializer.data)
        def serializer.object.get.method = 'post'
            if Employee.data():
                return response('Employee Details All Record Successfully Created', status=201)
            else:
                Employee.data is None
                return response('Employee Details All Records Not_Successfully Created,Plz Try Again', status=400)


    def put(self,request,format = None):
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs, many=True)
        return Response(serializer.data)
        def serializer.objects.all():
            if Employee.data():
                return response('Employee Details All Record Successfully Update', status=201)
            else:
                Employee.data is None
                return response('Employee Details All Records Not_Successfully Update,Plz Try Again', status=400)





    def patch(self,request,pk = None):
            qs = Employee.objects.all()
            serializer = EmployeeSerializer(qs, many=True)
            return Response(serializer.data)
            def serializer.object.get(id):
                if Employee.data():
                    return response('Employee Details Particularly Record Successfully Update', status=201)
                else:
                    Employee.data  is None
                    return response('Employee Details Particularly Record Not_Successfully Update,Plz Try Again', status=400)


    def delete(self,request,pk = None):
            qs = Employee.objects.all()
            serializer = EmployeeSerializer(qs, many=True)
            return Response(serializer.data)
            def  serializer.object.get(id):
                if Employee.data():
                    return response('Employee Details Record Successfully Delete',status = 204)
                else:
                    Employee.data is None
                    return response('Employee Details Record Not_Successfully Delete,Plz Try Again',status = 400)


















