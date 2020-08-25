# Generated by Django 3.1 on 2020-08-23 19:24

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('creator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('amount', models.IntegerField()),
                ('time', models.IntegerField()),
                ('image_main', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('is_published', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='creator.creator')),
            ],
        ),
    ]
