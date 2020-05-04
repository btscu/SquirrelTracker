from django.db import models
from django.utils.translation import gettext as _

class SquirrelViewing(models.Model):
    longitude  = models.FloatField(
            help_text = _('Longitude'),)

    latitude = models.FloatField(
            help_text = _('Latitude'),)

    unique_squirrel_id = models.CharField(
            help_text = _('Unique Squirrel Identifier'),
            max_length = 50,
            )

    AM = 'AM'
    PM = 'PM'

    SIGHT_TIME  = (
            (AM,'AM'),
            (PM, 'PM'),
            )

    shift = models.CharField(
            help_text = _('Sighting: Morning or Night?'),
            max_length=50,
            choices=SIGHT_TIME,
            blank=True)
    
    date = models.DateField(
            help_text = _('Date in the format yyyy-mm-dd'),
            null = True,
            blank=True)

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Unknown = '?'
    
    AGE_CHOICE=(
            (Adult,'Adult'),
            (Juvenile, 'Juvenile'),
            (None, '')
            )


    age = models.CharField(
            help_text = _('Age of Squirrel'),
            max_length=50,
            choices = AGE_CHOICE,
            blank = True
            )
    

# Create your models here.
