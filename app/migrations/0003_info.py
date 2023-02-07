# Generated by Django 3.1.7 on 2021-03-30 09:48

import app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_delete_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('video', models.FileField(upload_to='video/', validators=[app.validators.validate_file_extension])),
            ],
        ),
    ]