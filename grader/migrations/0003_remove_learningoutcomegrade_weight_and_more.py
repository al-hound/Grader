# Generated by Django 4.2 on 2024-07-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0002_learningoutcomegrade_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learningoutcomegrade',
            name='weight',
        ),
        migrations.AddField(
            model_name='learningoutcome',
            name='weight',
            field=models.FloatField(default=1.0),
        ),
    ]