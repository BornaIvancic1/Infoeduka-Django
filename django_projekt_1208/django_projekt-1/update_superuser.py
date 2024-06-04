from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Updates the details of a superuser account'

    def handle(self, *args, **options):
        User = get_user_model()
        email = input('Enter the email of the superuser account you want to update: ')

        try:
            superuser = User.objects.get(email=email, is_superuser=True)
        except User.DoesNotExist:
            print('Superuser with the specified email does not exist.')
            return

        first_name = input('Enter the new first name: ')
        last_name = input('Enter the new last name: ')

        superuser.first_name = first_name
        superuser.last_name = last_name
        superuser.save()

        print('Superuser account updated successfully.')
