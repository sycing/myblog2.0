# Generated by Django 2.2 on 2023-05-05 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190427_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='hide',
            field=models.BooleanField(default=False),
        ),
    ]
