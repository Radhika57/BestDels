# Generated by Django 4.0.2 on 2023-05-02 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_city_remove_posts_faqschema_delete_faqsch_and_more'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertiesReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
                ('reviews', models.TextField()),
                ('rating', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED')], max_length=500)),
                ('property_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.properties')),
            ],
        ),
    ]
