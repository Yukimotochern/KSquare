# Generated by Django 2.1.3 on 2018-11-20 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0006_auto_20181120_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forthrelationentry',
            name='to_relation_partner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forth_relation_partner', to='knowledge.ToRelationEntry'),
        ),
    ]