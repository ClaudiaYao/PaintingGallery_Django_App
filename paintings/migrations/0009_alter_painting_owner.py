# Generated by Django 4.2.6 on 2024-06-09 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_message'),
        ('paintings', '0008_alter_painting_options_alter_review_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]