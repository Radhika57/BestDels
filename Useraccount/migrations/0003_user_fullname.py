# Generated by Django 4.0.2 on 2023-04-13 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Useraccount', '0002_alter_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
