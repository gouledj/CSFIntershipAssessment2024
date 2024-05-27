# Generated by Django 4.1.3 on 2024-05-27 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieReviews',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_review', models.CharField(max_length=300)),
                ('movie_rating', models.PositiveIntegerField()),
                ('movie_recommendation', models.CharField(max_length=5)),
            ],
        ),
    ]