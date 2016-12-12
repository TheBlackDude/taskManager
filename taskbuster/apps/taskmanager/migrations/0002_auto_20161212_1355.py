# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the project name', verbose_name='name', max_length=100)),
                ('color', models.CharField(help_text='Enter the hex color code, like #ccc or #cccccc', verbose_name='color', max_length=7, default='#fff', validators=[django.core.validators.RegexValidator('(^#[0-9a-fA-F]{3}$)|(^#[0-9a-fA-F]{6}$)')])),
                ('user', models.ForeignKey(related_name='projects', to='taskmanager.Profile', verbose_name='user')),
            ],
            options={
                'ordering': ('user', 'name'),
                'verbose_name_plural': 'Projects',
                'verbose_name': 'Project',
            },
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('user', 'name')]),
        ),
    ]
