# Generated by Django 4.0.1 on 2022-03-20 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_exam_qno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='qno',
        ),
        migrations.AddField(
            model_name='exam',
            name='total_questions',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mcq',
            name='qno',
            field=models.IntegerField(null=True),
        ),
    ]
