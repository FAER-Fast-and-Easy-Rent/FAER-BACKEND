from api.tests.factories import seed_data
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
# from multiprocessing import Pool, cpu_count
# from tqdm import tqdm
User = get_user_model()


class Command(BaseCommand):
    help = 'Seed database'

    def handle(self, *args, **options):
        if User.objects.filter(email='test@email.com').exists():
            print("Test User already exists.")
        else:
            print("Creating a test User")
            User.objects.create_user(email='test@email.com', name='testuser', password='password')
            print("Test User created.")

        # with Pool(processes=1) as pool:
        #     pool.map(seed_data, tqdm(range(10), desc="Seeding Data :"))
        seed_data()
