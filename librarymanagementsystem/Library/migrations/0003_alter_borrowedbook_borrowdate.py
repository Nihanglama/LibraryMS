# Generated by Django 5.0.1 on 2024-02-02 17:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Library", "0002_alter_bookdetail_bookid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowedbook",
            name="BorrowDate",
            field=models.DateField(auto_now_add=True),
        ),
    ]
