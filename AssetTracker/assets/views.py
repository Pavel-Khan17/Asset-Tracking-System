from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from django.db import IntegrityError

# this class view for List all Companys, or create a new instence 
class CompanyListCreateView(APIView):
    def get(self, request):
        companies = CompanyModel.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# this class view for List all employee , or create a new instence 
class EmployeeListCreateView(APIView):
    def get(self, request):
        employees = EmployeeModel.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# this class view for List all asstes , or create a new instence 
class AssetsListCreateView(APIView):
    def get(self, request):
        assets = AssetsModel.objects.all()
        serializer = AssetsSerializer(assets, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        #  checking is the asset is already deleged to any employee by asset_issued status 
        asset_issued = request.data.get('asset_issued', False)
        if asset_issued:
            return Response({"detail": "Cannot delegate an already issued Assets."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = AssetsSerializer(data=request.data)
        if serializer.is_valid():
            if not asset_issued:
                serializer.save()
            else:
                serializer.save(asset_issued=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# this class view for Retrieve, update or delete a assets instance.
class AssetsUpdateDeleteView(APIView):
    def get_object(self, id):
        try:
            return AssetsModel.objects.get(pk=id)
        except AssetsModel.DoesNotExist:
            raise Http404

    def get(self, request, id):
        snippet = self.get_object(id)
        serializer = AssetsSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, id):
        snippet = self.get_object(id)
        serializer = AssetsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# this class view for List all asstes log , or create a new instence 
class AssetsLogListCreateView(APIView):
    
    def get(self, request):
        assets = AssetsLog.objects.all()
        serializer = AssetsLogGetSerializer(assets, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        
        # checking is the asset is already deleged to any employee by asset_issued status 
        asset_id = request.data.get('asset')
        assets = AssetsModel.objects.get(pk=asset_id)
        if assets.asset_issued:
            return Response({"detail": "Assets is already issued and cannot be delegated."}, status=status.HTTP_400_BAD_REQUEST)

        assets.asset_issued = True
        assets.save()

        serializer = AssetsLogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# this view is for to edit the log for returned asset 

@api_view(['PATCH','DELETE'])
def assets_log_detail(request,id):
    try:
        assets_log = AssetsLog.objects.get(pk=id)
    except AssetsLog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='PATCH':
        serializer = AssetsLogGetSerializer(assets_log, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        assets_log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# this view is for filter the assets log based on the company name (str)
class AssetsLogListByCompanyView(APIView):
    def get(self, request, company_name):
        company = get_object_or_404(CompanyModel, company_name=company_name)
        assets_logs = AssetsLog.objects.filter(employee__company=company)
        serializer = AssetsLogGetSerializer(assets_logs, many=True)
        return Response(serializer.data)

# this view is for filter the assets log based on the employee id
class AssetsLogListByEmployeeView(APIView):
    def get(self, request, employee_id):
        asset_logs = AssetsLog.objects.filter(employee__id=employee_id)
        serializer = AssetsLogGetSerializer(asset_logs, many=True)
        return Response(serializer.data)