# Generated by Django 4.1.2 on 2022-11-14 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_studentpersonalinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='registrationNumber',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='studentpersonalinfo',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.schoolinfo'),
        ),
    ]
