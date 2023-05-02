# Generated by Django 4.0.2 on 2023-05-01 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=15)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProjectReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
                ('reviews', models.TextField()),
                ('rating', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED')], max_length=500)),
                ('project_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.projects')),
            ],
        ),
    ]