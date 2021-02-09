# Generated by Django 3.1.4 on 2021-02-06 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('asked', models.DateTimeField(auto_now_add=True)),
                ('active', models.DateTimeField(auto_now=True)),
                ('view', models.IntegerField()),
                ('personid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.person')),
                ('topicid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topic')),
            ],
        ),
    ]