# Generated by Django 4.1.1 on 2022-09-07 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_movelist_invul_alter_movelist_special_props'),
    ]

    operations = [
        migrations.AddField(
            model_name='movelist',
            name='character_movelist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.character'),
        ),
    ]