# Generated by Django 4.2.1 on 2023-06-05 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_owners_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('fullname', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('email_id', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=50)),
                ('nid_no', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=300)),
            ],
        ),
    ]
