import django
import random
from first_app.models import  AccesRecord, Topic, Webpage
from faker import Faker
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()


fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace','News','Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        # pega o topicoi
        top = add_topic()
        # cria os dados frios
        fake_url = fakegen.url()
        fake_data = fakegen.date()
        fake_name = fakegen.company()

        # cria  Webpage data
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Cria o fake acces
        acc_rec = AccesRecord.objects.get_or_create(name=webpg,date=fake_data)[0]


if __name__ == '__main__':
    print("Populating Script!")
    populate(20)
    print("Populating complete!")
