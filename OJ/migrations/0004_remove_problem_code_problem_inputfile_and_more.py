# Generated by Django 4.0.5 on 2022-07-09 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OJ', '0003_alter_solution_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='code',
        ),
        migrations.AddField(
            model_name='problem',
            name='inputFile',
            field=models.FileField(default='/Devesh/input.txt', max_length=254, upload_to=''),
        ),
        migrations.AddField(
            model_name='problem',
            name='outputFile',
            field=models.FileField(default='/Devesh/acc_out.txt', max_length=254, upload_to=''),
        ),
    ]