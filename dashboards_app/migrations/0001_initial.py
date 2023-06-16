# Generated by Django 3.2.19 on 2023-06-16 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('description', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'db_table': 'dashboards',
            },
        ),
    ]
