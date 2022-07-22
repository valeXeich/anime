# Generated by Django 4.0.6 on 2022-07-22 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_customuser_throw'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'ordering': ['-value'],
            },
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='slug',
        ),
        migrations.AlterField(
            model_name='rating',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anime_rating', to='anime.anime'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rating',
            name='star',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.ratingstar'),
        ),
    ]
