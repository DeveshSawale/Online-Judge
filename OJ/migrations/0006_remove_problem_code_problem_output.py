# Generated by Django 4.0.5 on 2022-07-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OJ', '0005_remove_problem_inputfile_remove_problem_outputfile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='code',
        ),
        migrations.AddField(
            model_name='problem',
            name='output',
            field=models.FileField(default='/Devesh/acc_out.txt', max_length=1000, upload_to=''),
        ),
    ]
