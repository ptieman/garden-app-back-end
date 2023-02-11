from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
# from django.conf.urls import urls
from journal.views import JournalViewSet, DeleteJournal, SeedViewSet
from journal.views import DeleteSeed, CreateUser, GetUsers, ToDoListView, DeleteTask
# plant_hardiness_zone
from journal.views import HomepageView

# router = routers.DefaultRouter()
# router.register(r'journal', JournalViewSet, basename='journal')

urlpatterns = [
    path('', HomepageView.as_view()),
    path('admin/', admin.site.urls),
    path('create-user/', CreateUser.as_view()),
    path('users/', GetUsers.as_view()),
    path('seedlist/', SeedViewSet.as_view()),
    path('journal/', JournalViewSet.as_view()),
    # path('journal/<int:pk>/', JournalIDSet.as_view()),
    path('journal/<int:pk>/', DeleteJournal.as_view()),
    # path('seedlist/<int:id>/get/', SeedIDSet.as_view()),
    # path('seedlist/<int:seed_id>/edit/', SeedViewSet.as_view()),
    path('seedlist/<int:pk>/', DeleteSeed.as_view()),
    path('tasks/', ToDoListView.as_view()),
    path('tasks/<int:pk>/', DeleteTask.as_view()),
    # path('tasks/<int:pk>', GetTasks.as_view()),
    # path('plant-hardiness/', PlantLibrary.as_view())
    
]