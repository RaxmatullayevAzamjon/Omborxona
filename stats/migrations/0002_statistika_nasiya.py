# Generated by Django 4.2.2 on 2023-10-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistika',
            name='nasiya',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
