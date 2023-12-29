# Generated by Django 4.2.1 on 2023-11-21 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("women", "0006_alter_women_cat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="women",
            name="cat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="posts",
                to="women.category",
            ),
        ),
        migrations.AlterField(
            model_name="women",
            name="date_update",
            field=models.DateTimeField(auto_now=True),
        ),
    ]