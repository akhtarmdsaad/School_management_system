# Generated by Django 3.1 on 2023-06-05 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]