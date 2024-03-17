# Set the SECRET_KEY environment variable for Django
import os

from backend.listings.models import Ad

os.environ['DJANGO_SECRET_KEY'] = 'your-secret-key-here'

# Import the Django settings module
import django

django.setup()

# Import the Django database settings

# Set the DATABASES environment variable for Django
os.environ['DATABASE_URL'] = 'postgres://user:password@localhost/dbname'


# Import the Django models


# Example function to create a new Ad object
def create_ad():
    ad = Ad(title='Example Ad', description='This is an example ad.', price=100.00, is_active=True)
    ad.save()


# Example usage of the create_ad function
create_ad()
