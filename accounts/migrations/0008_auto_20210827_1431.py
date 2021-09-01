# Generated by Django 3.1.7 on 2021-08-27 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210821_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='companyprofile/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='employeeprofile/'),
        ),
    ]