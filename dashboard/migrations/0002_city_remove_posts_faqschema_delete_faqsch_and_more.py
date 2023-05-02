# Generated by Django 4.0.2 on 2023-05-02 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='posts',
            name='faqSchema',
        ),
        migrations.DeleteModel(
            name='faqSch',
        ),
        migrations.AlterField(
            model_name='projects',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.city'),
        ),
        migrations.AlterField(
            model_name='properties',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.city'),
        ),
    ]