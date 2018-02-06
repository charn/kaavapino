# Generated by Django 2.0.1 on 2018-02-01 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_make_help_text_non_null'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectAttributeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
            ],
            options={
                'verbose_name': 'project attribute image',
                'verbose_name_plural': 'project attribute images',
            },
        ),
        migrations.AlterField(
            model_name='attribute',
            name='value_type',
            field=models.CharField(choices=[('integer', 'integer'), ('short_string', 'short string'), ('long_string', 'long string'), ('boolean', 'boolean'), ('date', 'date'), ('geometry', 'geometry'), ('image', 'image')], max_length=64, verbose_name='value type'),
        ),
        migrations.AddField(
            model_name='projectattributeimage',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='projects.Attribute', verbose_name='attribute'),
        ),
        migrations.AddField(
            model_name='projectattributeimage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='projects.Project', verbose_name='project'),
        ),
    ]