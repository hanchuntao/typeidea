# Generated by Django 2.2.3 on 2019-07-22 16:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='herf',
            new_name='href',
        ),
        migrations.RemoveField(
            model_name='sidebar',
            name='name',
        ),
        migrations.AddField(
            model_name='sidebar',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='标题'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='display_type',
            field=models.PositiveIntegerField(choices=[(1, 'HTML'), (2, '最新文章'), (3, '最热文章'), (4, '最近评论')], default=1, verbose_name='展示类型'),
        ),
    ]
