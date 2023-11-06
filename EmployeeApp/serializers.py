from rest_framework import serializers
from EmployeeApp.models import Departments,Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        filds = ('DepartmentId', 
                 'DepartmentName')
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        filds = ('EmployeeId', 
                 'EmployeeName', 
                 'Department',
                 'DateOfJoin',
                 'PhotFileName')