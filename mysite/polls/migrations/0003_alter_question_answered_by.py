# Generated by Django 4.0.6 on 2022-08-14 00:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0002_question_answered_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answered_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
