# Generated by Django 4.0.1 on 2022-03-25 01:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_subjective'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.FileField(null=True, upload_to='')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.exam')),
                ('qno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.mcq')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredExam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
