from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer
# Create your views here.

@csrf_exempt
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        department_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(department_serializer.data, safe=False)
    
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("CADASTRO REALIZADO COM SUCESSO", safe=False)
        return JsonResponse("Não foi possivel cadastrar este funcionario", safe=False)
    
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        departments = Departments.objects.get(DepartmentId=department_data['departmentId'])
        department_serializer = DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("CADASTRO ATUALIZADO COM SUCESSO", safe=False)
        return JsonResponse("Não foi possivel ATUALIZAR este funcionario", safe=False)
    
    elif request.method == 'DELET':
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Cadastro Deletado Com Sucesso", safe=False)
        