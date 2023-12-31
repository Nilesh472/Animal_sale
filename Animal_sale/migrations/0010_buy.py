# Generated by Django 4.0.2 on 2023-03-25 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Animal_sale', '0009_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AnimalCategory', models.CharField(max_length=70)),
                ('AnimalBreed', models.CharField(max_length=70)),
                ('YourName', models.CharField(max_length=70)),
                ('Phone', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=70)),
                ('Quntity', models.CharField(max_length=9)),
                ('Pricepercattle', models.CharField(choices=[('1', '10000-20000'), ('2', '20000-40000'), ('3', '40000-80000'), ('4', '80000-100000'), ('5', '>120000')], default='1', max_length=20)),
                ('Pincode', models.CharField(max_length=100)),
                ('BuyWithin', models.CharField(choices=[('1', '10000-20000'), ('2', '20000-40000'), ('3', '40000-80000'), ('4', '80000-100000'), ('5', '>120000')], default='1', max_length=20)),
                ('description', models.TextField(max_length=500, unique=True)),
            ],
        ),
    ]
