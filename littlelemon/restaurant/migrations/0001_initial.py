# Generated by Django 5.0 on 2023-12-16 03:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("numberOfGuests", models.IntegerField()),
                ("bookingDate", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("inventory", models.IntegerField()),
            ],
        ),
    ]