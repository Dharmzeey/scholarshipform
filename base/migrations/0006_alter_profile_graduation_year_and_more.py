# Generated by Django 4.1.3 on 2022-12-04 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_alter_profile_date_of_birth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="graduation_year",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="profile",
            name="year_of_admission",
            field=models.IntegerField(),
        ),
    ]
