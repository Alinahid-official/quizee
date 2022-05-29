# Generated by Django 4.0.1 on 2022-03-25 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_subanswer_registeredexam'),
    ]

    operations = [
        migrations.CreateModel(
            name='GivenExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
