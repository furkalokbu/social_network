# Generated by Django 4.2 on 2023-10-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requesthistory',
            name='browser',
        ),
        migrations.RemoveField(
            model_name='requesthistory',
            name='ip',
        ),
        migrations.AddField(
            model_name='requesthistory',
            name='method',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='requesthistory',
            name='path',
            field=models.CharField(default='', max_length=255),
        ),
    ]