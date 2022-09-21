from django.urls import path
from .views.employee_views import *

urlpatterns = [
  path("employees/", EmployeeV1View.as_view({ "get": "get_list_employees" })),
  path("employees/<int:employee_id>/", EmployeeV1View.as_view({ "post": "post_employee_manager" })),
  path("employees/<int:employee_id>/coords/", EmployeeV1View.as_view({ "post": "post_employee_coords" })),
  path("managers/", EmployeeManagerV1View.as_view()),
]