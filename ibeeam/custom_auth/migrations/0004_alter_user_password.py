# Generated by Django 4.1.3 on 2022-12-02 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='6b\nk/\t|D; V<rkkh', max_length=128),
        ),
    ]
