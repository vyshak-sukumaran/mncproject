# Generated by Django 3.1.7 on 2021-08-20 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_companyprofile'),
    ]

    operations = [
        migrations.RenameModel('CompanyProfile', 'Company')
    ]
