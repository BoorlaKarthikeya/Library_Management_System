# Generated by Django 4.0.3 on 2023-07-17 04:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0020_alter_book_issue_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 25, 9, 54, 34, 374905), help_text='Date the book is due to'),
        ),
    ]
