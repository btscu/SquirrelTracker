from django.core.management.base import BaseCommand
from sightings.models import Sight
import csv
import datetime


class Command(BaseCommand):
    def add(self,parser):
        parser.add_argument('squirrel_csv')

    def open_fp(self, *args, **kwargs):
        with open(options['squirrel_csv']) as fp:
            csv = csv.DictReader(fp)
            csv_data  = list(csv)

        def parse_boolean(str_):
            if str(str_) == 'TRUE':
                str_ = True
            elif str(str_) ==  'FALSE':
                str_ = False
            else:
                str_ = None
            return str_

        for i in csv_data:
            s = Sight(
                    Longitude = i['X'],
                    Latitude = i['Y'],
                    Unique_Squirrel_Id = i['Unique Squirrel ID'],
                    Hectare = i['Hectare']
                    Shift = i['Shift'],
                    Date = datetime.datetime.strptime(i['Date'],'%m%d%Y'),
                    Hectare_Squirrel_Number = i['Hectare Squirrel Number']
                    Age = i['Age'],
                    Primary_Fur_Color = i['Primary Fur Color'],
                    Location = i['Location'],
                    Specific_Location = i['Specific Location'],
                    Running = convertBool(i['Running']),
                    Chasing = convertBool(i['Chasing']),
                    Climbing = convertBool(i['Climbing']),
                    Eating = convertBool(i['Eating']),
                    Foraging = convertBool(i['Foraging']),
                    Other_Activities = i['Other Activities'],
                    Kuks = convertBool(i['Kuks']),
                    Quaas = convertBool(i['Quaas']),
                    Moans = convertBool(i['Moans']),
                    Tail_Flags = convertBool(i['Tail flags']),
                    Tail_Twitches = convertBool(i['Tail twitches']),
                    Approaches = convertBool(i['Approaches']),
                    Indifferent = convertBool(i['Indifferent']),
                    Runs_From = convertBool(i['Runs from']),
                    )
            s.save()

