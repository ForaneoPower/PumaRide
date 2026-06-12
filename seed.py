import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PumaRide.settings')
django.setup()

from ride.models import User, Driver

passenger = User.objects.create_user(
    username='juan.perez',
    first_name='Juan',
    last_name='Pérez',
    email='juan.perez@enesmorelia.unam.mx',
    student_id='454324788',
    institution='ENES Morelia',
    campus='Morelia, Mich.',
    rides_taken=12,
    score=4.9,
    password='password123'
)

driver_user = User.objects.create_user(
    username='sofia.reyes',
    first_name='Sofía',
    last_name='Reyes',
    email='sofia.reyes@enesmorelia.unam.mx',
    student_id='423817905',
    institution='ENES Morelia',
    campus='Morelia, Mich.',
    password='password123'
)

Driver.objects.create(
    user=driver_user,
    license_number='MICH-2847-SR',
    driver_since='Marzo 2025',
    vehicle_plate='MHN-482-B',
    vehicle_capacity=4,
    rides_given=8,
    score=5.0
)