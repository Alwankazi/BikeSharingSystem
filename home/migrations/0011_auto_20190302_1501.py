# Generated by Django 2.1.5 on 2019-03-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190123_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactUs',
            fields=[
                ('mail_id', models.AutoField(primary_key=True, serialize=False)),
                ('fn', models.CharField(max_length=30)),
                ('ln', models.CharField(max_length=40)),
            ],
            options={
                'db_table': '#',
            },
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]