# Generated by Django 4.2.7 on 2023-12-08 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_customer_email_customer_repass'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_column='name', null=True)),
                ('email', models.TextField(db_column='email', null=True)),
                ('message', models.TextField(db_column='message', null=True)),
            ],
        ),
    ]