# Generated by Django 2.2.20 on 2021-04-26 10:38

from django.db import migrations


def define_default_plans(apps, schema_editor):
    Plan = apps.get_model("dashboard.Plan")
    Plan.objects.all().delete()  # ensure no plans exist
    plans = [
        {
            "name": "Free",
            "description": "Free plan",
            "price": "$0",
        },
        {
            "name": "Standard",
            "description": "Standard plan",
            "price": "$10",
        },
        {
            "name": "Pro",
            "description": "Pro plan",
            "price": "$25",
        }
    ]
    for plan in plans:
        Plan.objects.create(**plan)


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_dashboard')
    ]

    operations = [
        migrations.RunPython(
            define_default_plans,
            migrations.RunPython.noop
        )
    ]
