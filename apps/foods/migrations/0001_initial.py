# Generated by Django 3.2.12 on 2022-03-18 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20220302_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('brand', models.CharField(blank=True, max_length=70, null=True)),
                ('weight', models.IntegerField(default=100)),
                ('calories', models.IntegerField()),
                ('total_fat', models.IntegerField(blank=True, null=True)),
                ('carbs', models.IntegerField(blank=True, null=True)),
                ('fiber', models.IntegerField(blank=True, null=True)),
                ('protein', models.IntegerField(blank=True, null=True)),
                ('salt', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_foods', to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(choices=[('BKFT', 'Breakfast'), ('LNCH', 'Lunch'), ('DNNR', 'Dinner'), ('DSST', 'Dessert'), ('SNCK', 'Snack')], max_length=4)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registered_by_users', to='foods.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registered_foods', to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='BreakfastRegistered',
            fields=[
            ],
            options={
                'verbose_name': 'Breakfast registered',
                'verbose_name_plural': 'Breakfasts registered',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('foods.registeredfood',),
        ),
        migrations.CreateModel(
            name='DessertRegistered',
            fields=[
            ],
            options={
                'verbose_name': 'Dessert registered',
                'verbose_name_plural': 'Desserts registered',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('foods.registeredfood',),
        ),
        migrations.CreateModel(
            name='DinnerRegistered',
            fields=[
            ],
            options={
                'verbose_name': 'Dinner registered',
                'verbose_name_plural': 'Dinners registered',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('foods.registeredfood',),
        ),
        migrations.CreateModel(
            name='LunchRegistered',
            fields=[
            ],
            options={
                'verbose_name': 'Lunch registered',
                'verbose_name_plural': 'Lunches registered',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('foods.registeredfood',),
        ),
        migrations.CreateModel(
            name='SnacksRegisteredFood',
            fields=[
            ],
            options={
                'verbose_name': 'Snack registered',
                'verbose_name_plural': 'Snacks registered',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('foods.registeredfood',),
        ),
    ]