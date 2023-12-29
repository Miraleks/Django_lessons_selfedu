# Generated by Django 4.2.1 on 2023-10-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("women", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="women",
            options={"ordering": ["-date_created"]},
        ),
        migrations.AddField(
            model_name="women",
            name="slug",
            field=models.SlugField(blank=True, default="", max_length=255),
        ),
        migrations.AddIndex(
            model_name="women",
            index=models.Index(
                fields=["-date_created"], name="women_women_date_cr_3b3a41_idx"
            ),
        ),
    ]
