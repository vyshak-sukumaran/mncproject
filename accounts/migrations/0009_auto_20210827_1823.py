# Generated by Django 3.1.7 on 2021-08-27 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210827_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(default='default.png', upload_to='companyprofile/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='default.png', upload_to='employeeprofile/'),
        ),
    ]
