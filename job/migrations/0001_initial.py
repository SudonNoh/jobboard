# Generated by Django 3.2.7 on 2021-10-05 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('company_email', models.EmailField(max_length=255)),
                ('job_title', models.CharField(max_length=50)),
                ('job_description', models.TextField(max_length=500)),
                ('salary', models.FloatField()),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
