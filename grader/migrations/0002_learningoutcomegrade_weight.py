# Generated by Django 4.2 on 2024-07-02 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningoutcomegrade',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=4),
        ),
    ]