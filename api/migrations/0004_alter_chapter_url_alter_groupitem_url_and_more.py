# Generated by Django 5.0.6 on 2024-05-17 19:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0003_alter_chapter_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chapter",
            name="url",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="groupitem",
            name="url",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="subchapter",
            name="url",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
