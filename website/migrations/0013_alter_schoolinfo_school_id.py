# Generated by Django 4.1.2 on 2022-11-07 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_rename_registration_number_studentinfo_registrationnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolinfo',
            name='school_id',
            field=models.IntegerField(),
        ),
    ]