# Generated by Django 3.2.13 on 2022-04-22 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('parameters', models.TextField(primary_key=True, serialize=False)),
                ('headline', models.TextField()),
                ('saved_at_date', models.TextField()),
                ('urls', models.TextField()),
                ('source', models.TextField()),
            ],
        ),
    ]
