# Generated by Django 4.1.3 on 2022-11-17 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('drinkId', models.CharField(max_length=200)),
                ('imageUrl', models.TextField(max_length=500)),
                ('instructions', models.TextField(max_length=3000)),
                ('ingredients', models.TextField(max_length=2000)),
                ('ingredientPortions', models.TextField(max_length=2000)),
                ('note', models.TextField(blank=True, max_length=2000)),
            ],
        ),
    ]