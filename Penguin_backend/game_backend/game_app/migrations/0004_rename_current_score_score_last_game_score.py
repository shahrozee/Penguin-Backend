# Generated by Django 5.2 on 2025-04-25 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0003_remove_score_score_score_current_score_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='current_score',
            new_name='last_game_score',
        ),
    ]
