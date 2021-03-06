# Generated by Django 4.0.3 on 2022-04-07 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='name',
            new_name='fullname',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='username',
        ),
        migrations.AddField(
            model_name='profiles',
            name='member_type',
            field=models.CharField(choices=[('Instructor', 'Instructor'), ('Attendee', 'Attendee')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='profiles',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='skill_set',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
