# Generated by Django 3.2.3 on 2021-09-10 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210906_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
    ]