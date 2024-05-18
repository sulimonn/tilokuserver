# Generated by Django 5.0.6 on 2024-05-17 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="groupitem",
            options={
                "verbose_name": "Элемент группы",
                "verbose_name_plural": "Элементы группы",
            },
        ),
        migrations.AlterField(
            model_name="chapter",
            name="description",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="subchapter",
            name="description",
            field=models.TextField(null=True),
        ),
    ]