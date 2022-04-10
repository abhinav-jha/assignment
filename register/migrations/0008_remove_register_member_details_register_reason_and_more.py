# Generated by Django 4.0.3 on 2022-04-06 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_remove_member_details_full_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='Member_details',
        ),
        migrations.AddField(
            model_name='register',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='skill_set',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.DeleteModel(
            name='Member_details',
        ),
    ]
