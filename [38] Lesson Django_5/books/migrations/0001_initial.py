# Generated by Django 4.2.19 on 2025-02-19 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=100)),
                ('publication', models.CharField(max_length=15)),
                ('isbn', models.CharField(max_length=11)),
            ],
        ),
    ]
