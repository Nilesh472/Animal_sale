# Generated by Django 4.0.6 on 2023-03-22 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Animal_sale', '0005_alter_species2_categoryid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='species2',
            name='categoryid',
        ),
        migrations.DeleteModel(
            name='Species1',
        ),
        migrations.DeleteModel(
            name='Species2',
        ),
    ]
