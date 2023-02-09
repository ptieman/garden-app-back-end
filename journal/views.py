
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


# HomePage

class HomepageView(APIView):
    def get(self, request):
        latest_journal_entry = JournalEntry.objects.order_by('-journal_time_stamp')[0]

        data = {
            'latest_journal_entry' : {
                'journal_title': latest_journal_entry.journal_title,
                'journal_body': latest_journal_entry.journal_body,
                'journal_time_stamp': latest_journal_entry.journal_time_stamp
            },
        }

        return JsonResponse(data)


# JOURNAL
class JournalViewSet(APIView):

    def get(self, request, format=None):
        queryset = JournalEntry.objects.values()
        return JsonResponse({"journals": list(queryset)})

    def post(self, request, format=None):
        data = request.data
        journal_entry = JournalEntry.objects.create(journal_title=data['journal_title'], journal_body=data['journal_body'], journal_time_stamp=datetime.datetime.now())
        return JsonResponse({"journal": journal_entry.to_dict()})

class JournalIDSet(APIView):
    def get(self, request, pk, format=None):
        journal_entry = get_object_or_404(JournalEntry, pk=pk)

        return JsonResponse({"journal": journal_entry.to_dict()})

class DeleteJournal(DestroyAPIView):
    def delete(self, request, id):
        journal_entry = get_object_or_404(JournalEntry, pk=id)
        journal_entry.delete()
        
        return JsonResponse({"message": "Journal entry deleted successfully"})


# SEED LIST

class SeedViewSet(APIView):
    # def get(self, request, format=None):
    #     queryset = SeedList.objects.values()
    #     return JsonResponse({"seeds": list(queryset)})

    def get(self, request, format=None):

        seeds = SeedList.objects.all()

        serializer = SeedSerializer(seeds, many=True)

        return JsonResponse(serializer.data, safe=False)


    def post(self, request, format=None):

        seed_name = request.data['seed_name']
        seed_description = request.data['seed_description']
        days_till_harvest = request.data['days_till_harvest']
        plant_spacing = request.data['plant_spacing']
        sun_requirements = request.data['sun_requirements']
        sow_method = request.data['sow_method']

        seed = SeedList.objects.create(
            seed_name=seed_name,
            seed_description=seed_description,
            days_till_harvest=days_till_harvest,
            plant_spacing=plant_spacing,
            sun_requirements=sun_requirements,
            sow_method=sow_method
        )

        serializer = SeedSerializer(seed)
        seed.save()

        return JsonResponse(serializer.data, safe=False)


        # seed_name = request.data.get('seed_name')
        # seed_description = request.data.get('seed_description')
        # days_till_harvest = request.data.get('days_till_harvest')
        # plant_spacing = request.data.get('plant_spacing')
        # sun_requirements = request.data.get('sun_requirements')
        # sow_method = request.data.get('sow_method')

        # seed = SeedList.objects.create(
        #     seed_name=seed_name, 
        #     seed_description=seed_description, 
        #     days_till_harvest=days_till_harvest, 
        #     plant_spacing=plant_spacing,
        #     sun_requirements=','.join(sun_requirements),
        #     sow_method=sow_method)
        # seed.save()

        # return JsonResponse({"message": "Seed successfully added"})


class DeleteSeed(DestroyAPIView):
    def delete(self, request, pk):
        print(f'Deleting seed with id {id}')
        seed = get_object_or_404(SeedList, pk=pk)
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
        # data = {
        #     'tasks' :  [
        #         item for item in tasks]
        # }
    

        return JsonResponse(serializer.data, safe=False)
    def post(self, request, format=None):

        task_title = request.data['task_title']
       

        task = ToDoList.objects.create(
            task_title=task_title
        )
        serializer = ToDoListSerializer(task)
        task.save()

        return JsonResponse(serializer.data, safe=False)
    

class DeleteTask(DestroyAPIView):
    def delete(self, request, pk):
        print(f'Deleting task with id {id}')
        task = get_object_or_404(ToDoList, pk=pk)
        task.delete()

        return JsonResponse({'message': 'Task successfully deleted'})

# class GetTasks(APIView):
    

        # DISABLED BC OF CALLS

# def plant_hardiness_zone(request):
#     url = "https://plant-hardiness-zone.p.rapidapi.com/zipcodes/90210"
#     headers = {
#         "X-RapidAPI-Key": os.environ['API_KEY'],
#         "X-RapidAPI-Host": "plant-hardiness-zone.p.rapidapi.com"
#     }
#     response = requests.request("GET", url, headers=headers)
#     return JsonResponse(response.json(), safe=False)