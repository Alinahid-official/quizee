# Generated by Django 4.0.1 on 2022-03-19 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_mcq_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='McqQuestions',
        ),
    ]
