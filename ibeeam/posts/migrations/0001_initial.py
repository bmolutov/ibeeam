# Generated by Django 4.1.3 on 2022-12-03 07:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import utils.upload


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date and time of create')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date and time of update')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to=utils.upload.get_post_image_path)),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('content', models.CharField(blank=True, max_length=2048, null=True, verbose_name='content')),
                ('views_count', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)], verbose_name='views count')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='PostReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_liked', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_reactions', to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='own_post_reactions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reaction',
                'verbose_name_plural': 'Reactions',
            },
        ),
    ]
