# Generated by Django 4.2.1 on 2023-08-12 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('art_forms', models.CharField(max_length=100)),
                ('art_preference', models.CharField(max_length=100)),
                ('art_inspiration', models.CharField(max_length=100)),
                ('art_emotions', models.CharField(max_length=100)),
                ('art_themes', models.CharField(max_length=100)),
                ('art_creation', models.CharField(max_length=100)),
                ('art_role', models.CharField(max_length=100)),
                ('art_feedback', models.CharField(max_length=100)),
                ('art_goals', models.CharField(max_length=100)),
                ('creative_process', models.CharField(max_length=100)),
                ('technical_skill', models.CharField(max_length=100)),
                ('art_experimentation', models.CharField(max_length=100)),
                ('target_audience', models.CharField(max_length=100)),
                ('cultural_influences', models.CharField(max_length=100)),
            ],
        ),
    ]
