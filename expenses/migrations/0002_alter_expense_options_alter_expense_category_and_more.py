# Generated by Django 4.0.3 on 2022-03-07 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ('-date',)},
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(default='missallenious', max_length=266),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
