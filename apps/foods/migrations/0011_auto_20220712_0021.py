# Generated by Django 3.2.13 on 2022-07-11 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0010_auto_20220527_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyuserfoodstatus',
            name='calories',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
