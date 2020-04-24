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

    Hectare = models.CharField(
            help_text = ('Hectare of Sighting'),
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

    Hectare = models.IntegerField(
            help_text = ('Hectare Squirrel Number'),
            )
    
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

    Black = 'Black'
    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    COLOR=(
            (Black, 'Black'),
            (Gray, 'Gray'),
            (Cinnamon, 'Cinnamon'),
            (None, ''),
            )

    
    Primary_Fur_Color = models.CharField(
            help_text = ('Color of Fur'),
            max_length=50,
            choices = COLOR,
            blank = True
            )

    Ground_Plane = 'Ground Plane'
    Above_Ground = 'Above Ground'
    LOCATION=(
            (Ground_Plane, 'Ground Plane'),
            (Above_Ground, 'Above Ground'),
            (None, ''),
            )
    
    Location =  models.CharField(
            help_text = ('Location'),
            max_length=100,
            choices = LOCATION,
            blank = True
            )

    Specific_Location = models.CharField(
            help_text = ('Specific notes to this location'),
            max_length=100,
            blank = True,
            )

    Running = models.NullBooleanField(
            help_text = ('Running'),
            blank=True,
    )
    
    Chasing = models.NullBooleanField(
            help_text = ('Chasing'),
            blank=True,
    )

    Climbing = models.NullBooleanField(
            help_text = ('Climbing'),
            blank=True,
    )

    Eating = models.NullBooleanField(
            help_text = ('Eating'),
            blank=True,
    )

    Foraging = models.NullBooleanField(
            help_text = ('Foraging'),
            blank=True,
    )

    Other_Activities = models.CharField(
        help_text = ('Other Activities'),
        max_length = 128,
        null = True,
        blank = True
    )

    
    Kuks = models.NullBooleanField(
            help_text = ('Kuks'),
            blank=True,
    )

    Quaas = models.NullBooleanField(
            help_text = ('Quaas'),
            blank=True,
    )

    Moans = models.NullBooleanField(
            help_text = ('Moans'),
            blank=True,
    )

    Tail_Flags = models.NullBooleanField(
            help_text = ('Tail_Flags'),
            blank=True,
    )

    Tail_Twitches = models.NullBooleanField(
            help_text = ('Tail_Twitches'),
            blank=True,
    )

    Approaches = models.NullBooleanField(
            help_text = ('Approaches'),
            blank=True,
    )

    Indifferent = models.NullBooleanField(
            help_text = ('Indifferent'),
            blank=True,
    )
    
    Runs_From = models.NullBooleanField(
            help_text = ('Runs_From'),
            blank=True,
    )




    


# Create your models here.
