# Generated by Django 4.1.1 on 2022-10-01 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_ph_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='website',
            field=models.URLField(blank=True, default=''),
        ),
    ]
