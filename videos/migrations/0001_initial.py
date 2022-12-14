# Generated by Django 4.1.2 on 2022-10-14 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(max_length=300)),
                ('youtube_video_id', models.CharField(max_length=255)),
                ('author_id', models.BigIntegerField()),
                ('view_count', models.BigIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.PositiveIntegerField()),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='videos.video')),
            ],
            options={
                'unique_together': {('user_id', 'video')},
                'index_together': {('user_id', 'video')},
            },
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.PositiveIntegerField()),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='videos.video')),
            ],
            options={
                'unique_together': {('user_id', 'video')},
                'index_together': {('user_id', 'video')},
            },
        ),
    ]
