# Generated by Django 3.0.4 on 2020-03-30 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
