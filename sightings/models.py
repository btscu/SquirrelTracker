from django.db import models


class SquirrelViewing(models.Model):
    longitude  = models.FloatField(
            help_text = ('Longitude'),)

    latitude = models.FloatField(
            help_text = ('Latitude'),)

    unique_squirrel_id = models.CharField(
            help_text = ('Unique Squirrel Identifier'),
            max_length = 50,
            )

    AM = 'AM'
    PM = 'PM'

    SIGHT_TIME  = (
            (AM,'AM'),
            (PM, 'PM'),
            )

    shift = models.CharField(
            help_text = ('Sighting: Morning or Night?'),
            max_length=50,
            choices=SIGHT_TIME,
            blank=True)
    
    date = models.DateField(
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


    age = models.CharField(
            help_text = ('Age of Squirrel'),
            max_length=50,
            choices = AGE_CHOICE,
            blank = True
            )
    

# Create your models here.
