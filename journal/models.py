from django.db import models

# Create your models here.

class JournalEntry(models.Model):
    journal_title = models.CharField(max_length=50)
    journal_body = models.TextField()
    journal_time_stamp = models.DateField()

    def __str__(self):
        return self.journal_title

    def to_dict(self):
        return {
            "journal_title": self.journal_title,
            "journal_body": self.journal_body,
            "journal_time_stamp": self.journal_time_stamp.strftime("%Y-%m-%d"),
        }


class ToDoList(models.Model):
    task_title = models.CharField(max_length=50)
    # description = models.TextField()

    def __str__(self):
        return self.task_title

    


class SeedList(models.Model):
    SUN_CHOICES = (
        ('full-sun', 'Full Sun'),
        ('partial-sun', 'Partial Sun'),
        ('shade', 'Shade'),
    )
    sun_requirements = models.CharField(max_length=20, choices=SUN_CHOICES, default='full-sun')
    SOW_CHOICES = (
        ('start-indoors', 'Start Indoors'),
        ('sow-direct', 'Sow Directly')
    )
    sow_method = models.CharField(max_length=20, choices=SOW_CHOICES, default='sow-direct')
    seed_name = models.CharField(max_length=50)
    seed_description = models.TextField()
    days_till_harvest = models.PositiveSmallIntegerField()
    plant_spacing = models.CharField(max_length=10)

    def __str__(self):
        return self.seed_name

    def to_dict(self):
        return {
            "seed_name": self.seed_name,
            "seed_description": self.seed_description,
            "days_till_harvest": self.days_till_harvest,
            "plant_spacing": self.plant_spacing
        }

# class User(models.Model):


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def check_password(self, password):
        """
        Check if the provided password matches the stored password.
        """
        return self.password == password

    def set_password(self, password):
        """
        Set the user's password.
        """
        self.password = password

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email