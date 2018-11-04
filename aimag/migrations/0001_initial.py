# Generated by Django 2.1.3 on 2018-11-04 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aimag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sum_count', models.IntegerField(default=0)),
                ('hun_am', models.IntegerField(default=0)),
                ('talbai', models.IntegerField(default=0)),
                ('nyagtarshil', models.FloatField(default=0)),
                ('aimag_tuv', models.CharField(max_length=50)),
                ('hursh_aimag', models.ManyToManyField(blank=True, related_name='_aimag_hursh_aimag_+', to='aimag.Aimag')),
            ],
        ),
        migrations.CreateModel(
            name='Sum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bag_count', models.IntegerField(default=0)),
                ('hun_am', models.IntegerField(default=0)),
                ('talbai', models.IntegerField(default=0)),
                ('nyagtarshil', models.FloatField(default=0)),
                ('aimag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aimag.Aimag')),
                ('hursh_sum', models.ManyToManyField(blank=True, related_name='_sum_hursh_sum_+', to='aimag.Sum')),
            ],
        ),
    ]