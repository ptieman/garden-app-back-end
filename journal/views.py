
import datetime
from . serializer import *
from journal.models import JournalEntry, SeedList, User, ToDoList
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
# from .forms import SunRequirementsForm
from django.http import JsonResponse
from .forms import UserForm
# from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import requests
import os


# JOURNAL
class JournalViewSet(APIView):

    def get(self, request, format=None):
        queryset = JournalEntry.objects.values()
        return JsonResponse({"journals": list(queryset)})

    def post(self, request, format=None):
        data = request.data
        journal_entry = JournalEntry.objects.create(journal_title=data['title'], journal_body=data['text'], journal_time_stamp=datetime.datetime.now())
        return JsonResponse({"journal": journal_entry.to_dict()})

class JournalIDSet(APIView):
    def get(self, request, pk, format=None):
        journal_entry = get_object_or_404(JournalEntry, pk=pk)

        return JsonResponse({"journal": journal_entry.to_dict()})

class DeleteJournal(DestroyAPIView):
    def delete(self, request, pk):
        journal_entry = get_object_or_404(JournalEntry, pk=pk)
        journal_entry.delete()
        
        return JsonResponse({"message": "Journal entry deleted successfully"})


# SEED LIST

class SeedViewSet(APIView):
    def get(self, request, format=None):
        queryset = SeedList.objects.values()
        return JsonResponse({"seeds": list(queryset)})

    # def post(self, request, format=None):
    #     data = request.data
    #     seed_entry = SeedList.objects.create(seed_name=data["name"], seed_description=data['text'], days_till_harvest=data[int])

    def post(self, request, format=None):
        seed_name = request.data.get('seed_name')
        seed_description = request.data.get('seed_description')
        days_till_harvest = request.data.get('days_till_harvest')
        plant_spacing = request.data.get('plant_spacing')
        sun_requirements = request.data.get('sun_requirements')
        sow_method = request.data.get('sow_method')

        seed = SeedList.objects.create(
            seed_name=seed_name, 
            seed_description=seed_description, 
            days_till_harvest=days_till_harvest, 
            plant_spacing=plant_spacing,
            sun_requirements=','.join(sun_requirements),
            sow_method=sow_method)
        seed.save()

        return JsonResponse({"message": "Seed successfully added"})
 


    def put(self, request, seed_id, format=None):
        try:
            seed = SeedList.objects.get(id=seed_id)
            seed.seed_name = request.data.get('seed_name', seed.seed_name)
            seed.seed_description = request.data.get('seed_description', seed.seed_description)
            seed.days_till_harvest = request.data.get('days_till_harvest', seed.days_till_harvest)
            seed.plant_spacing = request.data.get('plant_spacing', seed.plant_spacing)
            seed.save()
            return JsonResponse({"message": "Seed successfully updated"})
        except SeedList.DoesNotExist:
            return JsonResponse({"message": "Seed not found"}, status=404)

class SeedIDSet(APIView):
    def get(self, request, id, format=None):
        seed = get_object_or_404(SeedList, pk=id)

        return JsonResponse({"seed": seed.to_dict()})

class DeleteSeed(DestroyAPIView):
    def delete(self, request, id):
        seed = get_object_or_404(SeedList, pk=id)
        seed.delete()

        return JsonResponse({'message': 'Seed successfully deleted'})



class CreateUser(APIView):
    def create_user_json(request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return JsonResponse({'message': f'User {user.email} created successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)




class GetUsers(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return JsonResponse(serializer.data, safe=False)

class ToDoListView(APIView):
    def get(self, request, format=None):
        tasks = ToDoList.objects.all()
        serializer = ToDoListSerializer(tasks, many=True)

        return JsonResponse(serializer.data, safe=False)

class GetTasks(APIView):
    def post(self, request, format=None):

        task_title = request.data('task_title')
        task_description = request.data('task_description')

        task = ToDoList.objects.create(
            task_title=task_title,
            task_description=task_description
        )
        task.save()

        return JsonResponse({"message": "Task successfully added"})

        # DISABLED BC OF CALLS

# def plant_hardiness_zone(request):
#     url = "https://plant-hardiness-zone.p.rapidapi.com/zipcodes/90210"
#     headers = {
#         "X-RapidAPI-Key": os.environ['API_KEY'],
#         "X-RapidAPI-Host": "plant-hardiness-zone.p.rapidapi.com"
#     }
#     response = requests.request("GET", url, headers=headers)
#     return JsonResponse(response.json(), safe=False)