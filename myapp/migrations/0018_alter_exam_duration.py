# Generated by Django 4.0.1 on 2022-03-25 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_exam_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='duration',
            field=models.CharField(default='00:30:00', max_length=30),
        ),
    ]
