# Generated by Django 4.1.2 on 2022-11-07 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_school_info_delete_item_delete_todolist'),
    ]

    operations = [
        migrations.CreateModel(
            name='department_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_id', models.CharField(max_length=20)),
                ('department_name', models.CharField(max_length=20)),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.student_info')),
            ],
        ),
    ]