# Generated by Django 4.0.1 on 2022-03-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_exam_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='qno',
            field=models.IntegerField(null=True),
        ),
    ]
