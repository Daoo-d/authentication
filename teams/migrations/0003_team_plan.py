# Generated by Django 5.0.6 on 2024-05-28 23:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teams", "0002_plan"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="plan",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="teams",
                to="teams.plan",
            ),
            preserve_default=False,
        ),
    ]
