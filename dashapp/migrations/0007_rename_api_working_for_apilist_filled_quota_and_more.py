# Generated by Django 4.2.7 on 2023-11-16 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0006_alter_apilist_website_limit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apilist',
            old_name='api_working_for',
            new_name='filled_quota',
        ),
        migrations.RenameField(
            model_name='apilist',
            old_name='website_limit',
            new_name='website_quota_limit',
        ),
    ]
