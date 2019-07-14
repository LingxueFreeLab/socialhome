# Generated by Django 2.0.8 on 2019-02-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0032_make_content_uuid_editable_false'),
        ('users', '0032_remove_user_relationship_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followed_tags',
            field=models.ManyToManyField(related_name='following_profiles', to='content.Tag', verbose_name='Followed tags'),
        ),
    ]