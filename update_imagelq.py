from django.core.management.base import BaseCommand
from painting.models import Painting

class Command(BaseCommand):
    def handle(self, *args, **options):
        paintings = Painting.objects.all()
        for painting in paintings:
            painting.imagelq = 'default_value'  # Gán giá trị mặc định cho trường imagelq
            painting.save()
