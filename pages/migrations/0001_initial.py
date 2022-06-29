# Generated by Django 4.0.5 on 2022-06-29 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField(max_length=11)),
                ('photo', models.ImageField(blank=True, upload_to='photos/')),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=6)),
                ('is_addmited', models.BooleanField(default=False)),
            ],
        ),
    ]
