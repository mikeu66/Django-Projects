# Generated by Django 4.1.5 on 2023-07-15 19:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("football", "0003_player_defensive_career_player_receiving_career_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="created_date",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date created"
            ),
        ),
    ]
