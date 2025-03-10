# Generated by Django 5.1.5 on 2025-01-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('iconlink', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cvlink', models.CharField(max_length=250, null=True)),
                ('filename', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Frontend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('iconlink', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', models.CharField(max_length=150)),
                ('imagelink', models.CharField(max_length=250, null=True)),
                ('date', models.CharField(max_length=150)),
                ('skills', models.CharField(max_length=150)),
                ('link', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('iconlink', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
