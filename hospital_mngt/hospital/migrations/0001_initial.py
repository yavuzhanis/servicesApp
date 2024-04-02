# Generated by Django 4.2.1 on 2023-08-17 20:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Drıver",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("surname", models.CharField(max_length=40)),
                ("mobile", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vehicle_model", models.IntegerField(null=True)),
                ("vehicle_inspection", models.DateField()),
                ("car_plaka", models.CharField(max_length=40)),
                ("adress", models.TextField(max_length=200)),
                ("vehicle_maintenance", models.DateField(default=datetime.date.today)),
                ("vehicle_tire", models.DateField(default=datetime.date.today)),
                ("car_battery", models.BooleanField(default=False)),
                ("vehicle_insurance", models.DateField(default=datetime.date.today)),
                ("vehicle_license", models.BooleanField(default=False)),
                ("carArventoNumber", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Atama",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_plaka", models.CharField(max_length=40)),
                ("vehicle_inspection", models.DateField(default=datetime.date.today)),
                (
                    "surucu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.drıver",
                    ),
                ),
                (
                    "vehicle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.vehicle",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Admın",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("surname", models.CharField(max_length=40)),
                ("mobile", models.IntegerField(null=True)),
                ("vehicle_model", models.CharField(max_length=50)),
                ("vehicle_inspection", models.DateField(null=True)),
                ("car_plaka", models.CharField(max_length=40)),
                ("vehicle_maintenance", models.DateField(default=datetime.date.today)),
                (
                    "admin",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.vehicle",
                    ),
                ),
                (
                    "driver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.drıver",
                    ),
                ),
            ],
        ),
    ]
