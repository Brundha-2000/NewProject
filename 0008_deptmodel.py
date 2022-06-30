# Generated by Django 4.0.4 on 2022-06-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailapp', '0007_delete_deptmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='deptmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptname', models.CharField(max_length=100)),
                ('facultyname', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'deptmodel',
            },
        ),
    ]