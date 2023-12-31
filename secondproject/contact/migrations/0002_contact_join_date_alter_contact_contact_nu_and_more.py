# Generated by Django 4.2.4 on 2023-09-01 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='join_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_nu',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
