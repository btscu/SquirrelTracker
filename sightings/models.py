from django.db import models


class SquirrelViewing(models.Model):
    Longitude  = models.FloatField(
            help_text = _('Longitude'),)

    Latitude = models.FloatField(
            help_text = _('Latitude'),)

    Unique_Squirrel_Id = models.CharField(
            help_text = _('Unique Squirrel Identifier'),
            max_length = 50,
            )

    Hectare = models.CharField(
            help_text = _('Hectare of Sighting'),
            max_length = 50,
            )

    AM = 'AM'
    PM = 'PM'

    SIGHT_TIME  = (
            (AM,'AM'),
            (PM, 'PM'),
            )

    Shift = models.CharField(
            help_text = _('Sighting: Morning or Night?'),
            max_length=50,
            choices=SIGHT_TIME,
            blank=True)
    
    Date = models.DateField(
            help_text = _('Date in yyyy-mm-dd'),
            null = True,
            blank=True)

    Hectare = models.IntegerField(
            help_text = _('Hectare Squirrel Number'),
            max_length = 50
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
            help_text = _('Age of Squirrel'),
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
            help_text = _('Color of Fur'),
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
            help_text = _('Location'),
            max_length=100,
            choices = LOCATION,
            blank = True
            )

    Specific_Location = models.CharField(
            help_text = _('Specific notes to this location'),
            max_length=100,
            blank = True,
            )

    Running = models.NullBooleanField(
            help_text = _('Running'),
            blank=True,
    )
    
    Chasing = models.NullBooleanField(
            help_text = _('Chasing'),
            blank=True,
    )

    Climbing = models.NullBooleanField(
            help_text = _('Climbing'),
            blank=True,
    )

    Eating = models.NullBooleanField(
            help_text = _('Eating'),
            blank=True,
    )

    Foraging = models.NullBooleanField(
            help_text = _('Foraging'),
            blank=True,
    )

    Other_Activities = models.CharField(
        help_text = _('Other Activities'),
        max_length = 128,
        null = True,
        blank = True
    )

    
    Kuks = models.NullBooleanField(
            help_text = _('Kuks'),
            blank=True,
    )

    Quaas = models.NullBooleanField(
            help_text = _('Quaas'),
            blank=True,
    )

    Moans = models.NullBooleanField(
            help_text = _('Moans'),
            blank=True,
    )

    Tail_Flags = models.NullBooleanField(
            help_text = _('Tail_Flags'),
            blank=True,
    )

    Tail_Twitches = models.NullBooleanField(
            help_text = _('Tail_Twitches'),
            blank=True,
    )

    Approaches = models.NullBooleanField(
            help_text = _('Approaches'),
            blank=True,
    )

    Indifferent = models.NullBooleanField(
            help_text = _('Indifferent'),
            blank=True,
    )
    
    Runs_From = models.NullBooleanField(
            help_text = _('Runs_From'),
            blank=True,
    )
(END)




    


# Create your models here.
