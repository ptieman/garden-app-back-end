from django.contrib import admin
from .models import JournalEntry, SeedList, User, ToDoList, SupplyList
# Register your models here.

admin.site.register(JournalEntry)
admin.site.register(SeedList)
admin.site.register(User)
admin.site.register(ToDoList)
admin.site.register(SupplyList)
