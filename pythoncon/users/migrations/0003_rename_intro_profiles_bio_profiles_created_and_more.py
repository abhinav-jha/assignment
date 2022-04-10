# Generated by Django 4.0.3 on 2022-04-07 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_name_profiles_fullname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='intro',
            new_name='bio',
        ),
        migrations.AddField(
            model_name='profiles',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='short_intro',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='social_github',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='social_linkedin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='social_twitter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='social_website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='social_youtube',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
