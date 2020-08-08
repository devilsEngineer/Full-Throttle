from userActivity.models import User, ActivityPeriod
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of data to be created.')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for _ in range(total):
            user_id = get_random_string(length=5)         
            User(user_id=user_id,real_name=get_random_string(length=7),tz='Asia/Kolkata').save()
            ActivityPeriod(user_id=user_id, start_time=get_random_string(length=7), end_time=get_random_string(length=7)).save()