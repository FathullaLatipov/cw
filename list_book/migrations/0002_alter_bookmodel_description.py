# Generated by Django 3.2.5 on 2021-07-27 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='description',
            field=models.TextField(max_length=90),
        ),
    ]
