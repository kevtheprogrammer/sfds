# Generated by Django 4.2.3 on 2023-07-26 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoilNutrient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nitrogen', models.CharField(max_length=900)),
                ('phosphorous', models.CharField(max_length=900)),
                ('potasium', models.CharField(max_length=900)),
                ('is_fertile', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecommendedPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagev', models.ImageField(upload_to=None)),
                ('name', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('soil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soil', to='land.soilnutrient')),
            ],
        ),
    ]
