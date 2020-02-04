# Generated by Django 3.0.3 on 2020-02-03 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20200203_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='student',
            name='state',
            field=models.CharField(choices=[('andhrapradesh', 'Andhrapradesh'), ('karnataka', 'Karnataka'), ('tamilnadu', 'Tamilnadu'), ('kerala', 'Kerala')], max_length=120),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
