# Generated by Django 4.2.7 on 2023-11-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiList',
            fields=[
                ('serial_number', models.AutoField(primary_key=True, serialize=False)),
                ('api_key', models.CharField(max_length=300)),
                ('api_running_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
