# Generated by Django 4.2.3 on 2023-07-16 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0019_alter_book_issue_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 24, 15, 3, 0, 360956), help_text='Date the book is due to'),
        ),
    ]
