# Generated by Django 2.1.5 on 2019-03-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weapon',
            old_name='v_max',
            new_name='r_max',
        ),
        migrations.RenameField(
            model_name='weapon',
            old_name='v_min',
            new_name='r_min',
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]