# Generated by Django 4.2.2 on 2023-10-09 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('manzil', models.CharField(max_length=30)),
                ('ism', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=20)),
                ('qarz', models.PositiveSmallIntegerField()),
                ('ombor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Maxsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('narx', models.PositiveSmallIntegerField()),
                ('miqdor', models.PositiveSmallIntegerField()),
                ('olchov', models.CharField(choices=[('Kg', 'Kg'), ('dona', 'dona'), ('litr', 'litr')], max_length=30)),
                ('brend', models.CharField(blank=True, max_length=20, null=True)),
                ('ombor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
