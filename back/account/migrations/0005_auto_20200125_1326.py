# Generated by Django 2.2.9 on 2020-01-25 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_tempuser_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentVerificationCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('verification_code', models.CharField(max_length=10)),
                ('expiry_date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='TempUser',
        ),
        migrations.AddField(
            model_name='user',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
