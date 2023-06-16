# Generated by Django 4.2.2 on 2023-06-06 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameEvent', models.CharField(max_length=40)),
                ('place', models.CharField(max_length=40)),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameParticipants', models.CharField(max_length=50)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.events')),
            ],
        ),
    ]
