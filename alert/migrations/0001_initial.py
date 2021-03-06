# Generated by Django 4.0.5 on 2022-06-03 17:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('symbol', models.CharField(max_length=10)),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('active', 'Active'), ('Waiting', 'Waiting'), ('Passed', 'Passed')], default='active', max_length=10)),
                ('high_price', models.PositiveIntegerField()),
                ('low_price', models.PositiveIntegerField()),
            ],
        ),
    ]
