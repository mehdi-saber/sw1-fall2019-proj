# Generated by Django 2.2.9 on 2020-01-25 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_user_student_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=30)),
                ('bio', models.TextField()),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('verification_code', models.CharField(max_length=10)),
                ('expiry_date', models.DateTimeField()),
            ],
        ),
    ]
