# Generated by Django 5.0.7 on 2024-08-01 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Date', models.CharField(max_length=15)),
                ('Description', models.CharField(max_length=10000)),
            ],
        ),
    ]
