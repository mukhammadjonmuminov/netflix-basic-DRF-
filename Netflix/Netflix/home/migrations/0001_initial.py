# Generated by Django 4.1.1 on 2022-09-09 11:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        # migrations.RunSQL('CREATE EXTENSION pg_trgm'),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('year', models.DateField()),
                ('imdb', models.IntegerField()),
                ('genre', models.CharField(choices=[('g1', 'Comedy'), ('g2', 'Drama'), ('g3', 'Epics'), ('g4', 'Serial'), ('g5', 'Documentary'), ('g6', 'Dedective'), ('g7', 'Fantastic'), ('g8', 'Scientific'), ('g9', 'Artistic'), ('g10', 'Historical')], max_length=150)),
                ('watched', models.IntegerField(default=0)),
                ('actor', models.ManyToManyField(to='home.actor')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=120)),
                ('created_date', models.DateField(default=datetime.datetime.today)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
