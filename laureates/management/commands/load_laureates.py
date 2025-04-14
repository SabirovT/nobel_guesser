from django.core.management.base import BaseCommand
from laureates.models import Laureate

LAUREATES_DATA = [
    {
        'name': 'Мария Кюри',
        'fact': 'Первая женщина-лауреат Нобелевской премии и единственная женщина, получившая премию дважды.',
        'q1_answer': 'Физика',
        'q2_answer': '1900-1910',
        'q3_answer': 'Франция',
        'q4_answer': 'Женский'
    },
    {
        'name': 'Мария Кюри',
        'fact': 'Первая женщина-лауреат Нобелевской премии и единственная женщина, получившая премию дважды.',
        'q1_answer': 'Химия',
        'q2_answer': '1900-1910',
        'q3_answer': 'Франция',
        'q4_answer': 'Женский'
    },
    {
        'name': 'Альберт Эйнштейн',
        'fact': 'Получил премию за объяснение фотоэлектрического эффекта, а не за теорию относительности.',
        'q1_answer': 'Физика',
        'q2_answer': '1921-1930',
        'q3_answer': 'Германия',
        'q4_answer': 'Мужской'
    },
    {
        'name': 'Джон Бардин',
        'fact': 'Первый и пока единственный дважды лауреат Нобелевской премии по физике',
        'q1_answer': 'Физика',
        'q2_answer': '1951-1960',
        'q3_answer': 'США',
        'q4_answer': 'Мужской'
    },
    {
        'name': 'Джон Бардин',
        'fact': 'Первый и пока единственный дважды лауреат Нобелевской премии по физике',
        'q1_answer': 'Физика',
        'q2_answer': '1971-1980',
        'q3_answer': 'США',
        'q4_answer': 'Мужской'
    },
    {
        'name': 'Лев Ландау',
        'fact': 'Отец основатель Московского Физико-Технического Института',
        'q1_answer': 'Физика',
        'q2_answer': '1961-1970',
        'q3_answer': 'Россия/СССР',
        'q4_answer': 'Мужской'
    },
    {
        'name': 'Андрей Гейм',
        'fact': 'Единственный, кто кроме Нобелевской премии также получил и дуальную - Шнобелевскую премию',
        'q1_answer': 'Физика',
        'q2_answer': '2001-2010',
        'q3_answer': 'Россия/СССР',
        'q4_answer': 'Мужской'
    },
    # Добавьте еще 14 лауреатов по аналогии
]

class Command(BaseCommand):
    help = 'Load Nobel laureates into database'
    
    def handle(self, *args, **options):
        for data in LAUREATES_DATA:
            Laureate.objects.create(**data)
        self.stdout.write(self.style.SUCCESS('Successfully loaded laureates'))