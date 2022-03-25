# Generated by Django 3.2.12 on 2022-03-25 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220302_2320'),
        ('foods', '0003_alter_registeredfood_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeredfood',
            name='date',
        ),
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='food',
            name='carbs',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_foods', to='accounts.profile'),
        ),
        migrations.AlterField(
            model_name='food',
            name='fiber',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='salt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='total_fat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='registeredfood',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registered_by_users', to='foods.food'),
        ),
    ]