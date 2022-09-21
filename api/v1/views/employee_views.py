from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status, viewsets
from django.db.models import F
from api.models import *

class EmployeeV1View(viewsets.ViewSet):
  def get_list_employees(self, request):
    '''GET - returns employee list'''

    try:
      employee_list = list(Employee.objects.all().values("id", "emp_id", "name", "designation", "team", "x_coord", "y_coord"))
      return JsonResponse(
        {"status":"success", "message": "Successfully fetched the employee list", "results": employee_list},
        status=status.HTTP_200_OK
      )
    except Exception as e:
      print(e)
      return JsonResponse(
          {"status": "failure", "message": "Exception occured while fetching the employee list"},
          status=status.HTTP_500_INTERNAL_SERVER_ERROR,
      )
  
  def post_employee_manager(self, request, employee_id):
    '''POST - Updates manager for employee'''

    try:
      manager_id = request.data.get("manager_id")
      manager_obj = Employee.objects.get(emp_id=manager_id)
      employee_manager_obj = Manager.objects.get(employee_id__emp_id=employee_id)
      employee_manager_obj.manager = manager_obj
      employee_manager_obj.save()
      return JsonResponse(
        {"status":"success", "message": "Successfully updated the manager"},
        status=status.HTTP_200_OK
      )
    except Exception as e:
      print(e)
      return JsonResponse(
          {"status": "failure", "message": "Exception occured while updating the manager"},
          status=status.HTTP_500_INTERNAL_SERVER_ERROR,
      )

  def post_employee_coords(self, request, employee_id):
    '''POST - Updates employee coordinates'''

    try:
      x_coord = request.data.get("x_coord")
      y_coord = request.data.get("y_coord")
      employee_obj = Employee.objects.get(emp_id=employee_id)
      employee_obj.x_coord = x_coord
      employee_obj.y_coord = y_coord
      employee_obj.save()
      return JsonResponse(
        {"status":"success", "message": "Successfully updated employee node coordinates"},
        status=status.HTTP_200_OK
      )
    except Exception as e:
      print(e)
      return JsonResponse(
          {"status": "failure", "message": "Exception occured while updating employee node coordinates"},
          status=status.HTTP_500_INTERNAL_SERVER_ERROR,
      )

class EmployeeManagerV1View(APIView):
  '''GET - returns manager list'''

  def get(self, request):
    try:
      employee_manager_list = list(Manager.objects.all().annotate(employee_=F("employee_id__emp_id"), manager_=F("manager_id__emp_id")).values("id", "employee_", "manager_"))
      return JsonResponse(
        {"status":"success", "message": "Successfully fetched the manager list", "results": employee_manager_list},
        status=status.HTTP_200_OK
      )
    except Exception as e:
      print(e)
      return JsonResponse(
          {"status": "failure", "message": "Exception occured while fetching the manager list"},
          status=status.HTTP_500_INTERNAL_SERVER_ERROR,
      )