# Generated by Django 2.2.3 on 2019-08-29 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20190829_0613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postfile',
            old_name='feed',
            new_name='post',
        ),
        migrations.AlterField(
            model_name='postfile',
            name='file',
            field=models.FileField(upload_to='files/%Y/%m/%d', verbose_name='فایل ها'),
        ),
    ]