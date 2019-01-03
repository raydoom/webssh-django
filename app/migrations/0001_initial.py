# Generated by Django 2.1.3 on 2019-01-03 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, unique=True, verbose_name='hostname')),
                ('ip', models.GenericIPAddressField(verbose_name='server ip')),
                ('port', models.IntegerField(verbose_name='ssh port')),
                ('username', models.CharField(blank=True, default='', max_length=50, verbose_name='ssh username')),
                ('password', models.CharField(blank=True, default='', max_length=50, verbose_name='ssh password')),
                ('description', models.CharField(blank=True, default='', max_length=128, verbose_name='description')),
            ],
        ),
    ]