# Generated by Django 3.2.6 on 2021-08-07 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('firstpassword', models.CharField(max_length=50)),
                ('confirmpassword', models.CharField(max_length=50)),
            ],
        ),
    ]