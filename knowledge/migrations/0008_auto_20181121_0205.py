# Generated by Django 2.1.3 on 2018-11-21 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0007_auto_20181120_0552'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForthLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('t_is_f', models.CharField(max_length=30, null=True)),
                ('related_concept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forth_link', to='knowledge.Concept')),
                ('relation_main', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='knowledge.Relation')),
            ],
        ),
        migrations.CreateModel(
            name='ToLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('f_is_t', models.CharField(max_length=30, null=True)),
                ('related_concept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_link', to='knowledge.Concept')),
                ('relation_main', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='knowledge.Relation')),
            ],
        ),
        migrations.RemoveField(
            model_name='forthrelationentry',
            name='related_concept',
        ),
        migrations.RemoveField(
            model_name='forthrelationentry',
            name='relation_main',
        ),
        migrations.RemoveField(
            model_name='forthrelationentry',
            name='to_relation_partner',
        ),
        migrations.RemoveField(
            model_name='torelationentry',
            name='related_concept',
        ),
        migrations.RemoveField(
            model_name='torelationentry',
            name='relation_main',
        ),
        migrations.DeleteModel(
            name='ForthRelationEntry',
        ),
        migrations.DeleteModel(
            name='ToRelationEntry',
        ),
        migrations.AddField(
            model_name='forthlink',
            name='to_link_partner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forth_link_partner', to='knowledge.ToLink'),
        ),
    ]
