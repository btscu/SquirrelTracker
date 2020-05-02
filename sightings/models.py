from django.db import models


class SquirrelViewing(models.Model):
    Longitude  = models.FloatField(
            help_text = ('Longitude'),)

    Latitude = models.FloatField(
            help_text = ('Latitude'),)

    Unique_Squirrel_Id = models.CharField(
            help_text = ('Unique Squirrel Identifier'),
            max_length = 50,
            )

    AM = 'AM'
    PM = 'PM'

    SIGHT_TIME  = (
            (AM,'AM'),
            (PM, 'PM'),
            )

    Shift = models.CharField(
            help_text = ('Sighting: Morning or Night?'),
            max_length=50,
            choices=SIGHT_TIME,
            blank=True)
    
    Date = models.DateField(
            help_text = ('Date in yyyy-mm-dd'),
            null = True,
            blank=True)

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Unknown = '?'
    
    AGE_CHOICE=(
            (Adult,'Adult'),
            (Juvenile, 'Juvenile'),
            (None, ''),
            (Unknown, '?'),
            )


    Age = models.CharField(
            help_text = ('Age of Squirrel'),
            max_length=50,
            choices = AGE_CHOICE,
            blank = True
            )

# Create your models here.
