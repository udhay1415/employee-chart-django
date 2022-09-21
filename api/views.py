from curses import termname
import email
from re import template
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from api.models import *

def ping(request):
    response = {"data": "pong"}
    return JsonResponse(response, status=status.HTTP_200_OK)

@api_view(['POST'])
def seed(request):
    try:
        employees = [
            {
                "emp_id": 1001,
                "email": "mark@gmail.com",
                "name": "Mark Hill",
                "designation": "CEO",
                "team": "CXO",
                "x_coord": 250,
                "y_coord": 25
            },
            {
                "emp_id": 1002,
                "email": "joe@gmail.com",
                "name": "Joe Linux",
                "designation": "Officer",
                "team": "Manager",
                "x_coord": 100,
                "y_coord": 125
            },
            {
                "emp_id": 1003,
                "email": "linda@gmail.com",
                "name": "Linda May",
                "designation": "CBO",
                "team": "Manager",
                "x_coord": 350,
                "y_coord": 125
            },
            {
                "emp_id": 1004,
                "email": "john@gmail.com",
                "name": "John Green",
                "designation": "CAO",
                "team": "Manager",
                "x_coord": 550,
                "y_coord": 125
            },
            {
                "emp_id": 1005,
                "email": "ron@gmail.com",
                "name": "Ron Blomquist",
                "designation": "Security Officer",
                "team": "Officer",
                "x_coord": 0,
                "y_coord": 225
            },
            {
                "emp_id": 1006,
                "email": "michael@gmail.com",
                "name": "Michael Rubin",
                "designation": "CIO",
                "team": "Officer",
                "x_coord": 100,
                "y_coord": 225
            },
            {
                "emp_id": 1007,
                "email": "alice@gmail.com",
                "name": "Alice Lopex",
                "designation": "Chief Communications",
                "team": "Officer",
                "x_coord": 250,
                "y_coord": 225
            },
            {
                "emp_id": 1008,
                "email": "mary@gmail.com",
                "name": "Mary Johnson",
                "designation": "CBO",
                "team": "Officer",
                "x_coord": 250,
                "y_coord": 325
            },
            {
                "emp_id": 1009,
                "email": "kirk@gmail.com",
                "name": "Kirk Douglas",
                "designation": "Chief Business",
                "team": "Officer",
                "x_coord": 250,
                "y_coord": 425
            },
            {
                "emp_id": 1010,
                "email": "erica@gmail.com",
                "name": "Erica Reel",
                "designation": "CCO",
                "team": "Officer",
                "x_coord": 250,
                "y_coord": 425
            }
        ]
        for emp in employees:
            emp_obj = Employee(
                email = emp["email"],
                name = emp["name"],
                designation = emp["designation"],
                team = emp["team"],
                x_coord = emp["x_coord"],
                y_coord = emp["y_coord"],
                emp_id = emp["emp_id"]
            )
            emp_obj.save()
        
        employee_manager = [
            { id: 1, "source": 1001, "target": 1002 },
            { id: 2, "source": 1001, "target": 1003 },
            { id: 3, "source": 1001, "target": 1004 },
            { id: 4, "source": 1002, "target": 1005 },
            { id: 5, "source": 1002, "target": 1006 },
            { id: 6, "source": 1003, "target": 1007 },
            { id: 7, "source": 1003, "target": 1008 },
            { id: 8, "source": 1003, "target": 1009 },
            { id: 9, "source": 1004, "target": 1010 },
        ]
        for emp_m in employee_manager:
            manager_obj = Employee.objects.get(emp_id=emp_m["source"])
            employee_obj = Employee.objects.get(emp_id=emp_m["target"])
            emp_m_obj = Manager(
                employee = employee_obj,
                manager = manager_obj
            )
            emp_m_obj.save()
        return JsonResponse({"message":"success"})
    except Exception as e:
        print(e)
        return JsonResponse(
            {"status": "failure", "message": "Exception occured while seeding data"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )