# Generated by Django 4.0.1 on 2022-03-26 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields
import school.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_id', models.CharField(max_length=200, unique=True)),
                ('category_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to=school.models.save_category_image, verbose_name='Category Image')),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comm_name', models.CharField(blank=True, max_length=200)),
                ('body', models.TextField(max_length=1000)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reply_body', models.TextField(max_length=500)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='school.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.CharField(max_length=200, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=250)),
                ('position', models.PositiveBigIntegerField(verbose_name='Post no.')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('videolink', embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='Video link')),
                ('filelink', models.URLField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to=school.models.save_post_files, verbose_name='Video')),
                ('ppt', models.FileField(blank=True, upload_to=school.models.save_post_files, verbose_name='Presentations')),
                ('Notes', models.FileField(blank=True, upload_to=school.models.save_post_files, verbose_name='Notes')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='school.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='school.post'),
        ),
    ]
