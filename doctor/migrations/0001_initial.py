# Generated by Django 4.0 on 2021-12-16 11:00

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.user')),
                ('specialisation', models.CharField(choices=[('MBBS', 'MBBS'), ('MS', 'MS'), ('MD', 'MD'), ('BAMS', 'BAMS'), ('BPT', 'BPT'), ('BUMS', 'BUMS')], max_length=100, null=True)),
                ('experience', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('user.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
