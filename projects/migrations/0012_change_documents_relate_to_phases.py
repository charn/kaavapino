# Generated by Django 2.0 on 2018-01-15 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_require_index_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documenttemplate',
            name='project_type',
        ),
        migrations.AddField(
            model_name='documenttemplate',
            name='project_phase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.ProjectPhase', verbose_name='project phase'),
        ),
        migrations.AlterField(
            model_name='projectphasesectionattribute',
            name='generated',
            field=models.BooleanField(default=False, verbose_name='generated'),
        ),
        migrations.AlterField(
            model_name='documenttemplate',
            name='project_phase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_templates', to='projects.ProjectPhase', verbose_name='project phase'),
        ),
    ]
