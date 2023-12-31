# Generated by Django 4.2.6 on 2023-11-16 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='p_endOfWork',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='p_idLine',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='p_position',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='p_salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='p_startOfWork',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='p_status',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_firstname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_lastname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
