# Generated by Django 3.1.6 on 2021-02-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Yfcase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yfcaseCaseNumber', models.CharField(max_length=100, verbose_name='案號(*)')),
            ],
        ),
    ]
