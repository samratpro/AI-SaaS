# Generated by Django 4.2.7 on 2023-11-16 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0009_website_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website_list',
            name='application_password',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='website_list',
            name='category_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='website_list',
            name='website_name',
            field=models.CharField(max_length=250),
        ),
    ]