# Generated by Django 4.0.6 on 2022-08-07 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vagas', '0003_vagas_candidatura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidaturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidato', models.IntegerField()),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vagas.vagas')),
            ],
        ),
    ]
