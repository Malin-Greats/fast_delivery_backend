# Generated by Django 4.0.3 on 2022-03-25 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_emailcount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homevideo',
            name='text',
        ),
        migrations.RemoveField(
            model_name='homevideo',
            name='video',
        ),
        migrations.AddField(
            model_name='homevideo',
            name='link',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='emailcount',
            name='repliedMail',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='emailcount',
            name='totalMail',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='emailcount',
            name='unrepliedMail',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='homevideo',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
