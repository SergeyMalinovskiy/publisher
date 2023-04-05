# Generated by Django 3.2.18 on 2023-03-29 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='main_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='author.author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='other_authors',
            field=models.ManyToManyField(null=True, related_name='other_author', to='author.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='registration_code',
            field=models.CharField(default=12345, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
