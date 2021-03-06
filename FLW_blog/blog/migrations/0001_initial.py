# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-12 06:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('dname', models.CharField(max_length=20, verbose_name='文档名称')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='描述信息')),
            ],
            options={
                'db_table': 'doc_info',
                'verbose_name': '文档信息',
            },
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('tname', models.CharField(max_length=20, verbose_name='文档类型 名称')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='描述信息')),
                ('did', models.ManyToManyField(to='blog.DocInfo')),
            ],
            options={
                'db_table': 'type_info',
                'verbose_name': '类型信息',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='主键')),
                ('uname', models.CharField(max_length=20, verbose_name='用户昵称')),
            ],
            options={
                'db_table': 'user_info',
                'verbose_name': '用户表',
            },
        ),
        migrations.AddField(
            model_name='docinfo',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='docs', to='blog.UserInfo', verbose_name='文档外键'),
        ),
    ]
