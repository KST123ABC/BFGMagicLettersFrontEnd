# Generated by Django 2.1.3 on 2019-04-14 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0003_auto_20180328_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='letter',
            field=models.CharField(max_length=2),
        ),
    ]
