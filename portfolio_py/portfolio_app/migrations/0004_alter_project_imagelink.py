# Generated by Django 5.1.5 on 2025-01-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_alter_backend_skill_iconlink_alter_file_cvlink_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='imagelink',
            field=models.ImageField(upload_to='media/images/%Y/%m/%d'),
        ),
    ]
