# Generated by Django 3.0.3 on 2020-02-03 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(choices=[('andhrapradesh', 'Andhrapradesh'), ('karnataka', 'Karnataka'), ('tamilnadu', 'Tamilnadu'), ('kerala', 'Kerala')], max_length=120)),
            ],
        ),
    ]