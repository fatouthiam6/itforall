# your_app/management/commands/update_image_paths.py
import os
from django.core.management.base import BaseCommand
from your_app.models import Question

class Command(BaseCommand):
    help = 'Met à jour les chemins d\'accès des images pour ne garder que le nom du fichier'

    def handle(self, *args, **kwargs):
        questions = Question.objects.all()
        for question in questions:
            if question.image_path:
                # Extrait le nom du fichier
                image_name = os.path.basename(question.image_path)
                # Met à jour le champ image_path
                question.image_path = image_name
                question.save()
                self.stdout.write(self.style.SUCCESS(f'Image path updated for question {question.id}: {image_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'No image path for question {question.id}'))
