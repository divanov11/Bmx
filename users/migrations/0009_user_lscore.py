# Generated by Django 4.2.3 on 2023-07-31 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_pscore_user_total_user_winrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lscore',
            field=models.IntegerField(default=0),
        ),
    ]