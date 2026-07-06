from django.db import migrations, models
import django.db.models.deletion


def delete_old_data(apps, schema_editor):
    apps.get_model('voting', 'Vote').objects.all().delete()
    apps.get_model('voting', 'MachineState').objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0002_populate_data'),
    ]

    operations = [
        migrations.RunPython(delete_old_data),
        migrations.DeleteModel(name='Vote'),
        migrations.DeleteModel(name='Symbol'),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_marathi', models.CharField(blank=True, max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='candidates/')),
                ('vote_count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_date', models.DateField(auto_now_add=True)),
                ('vote_time', models.TimeField(auto_now_add=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='voting.candidate')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
