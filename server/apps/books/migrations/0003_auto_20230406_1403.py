# Generated by Django 3.2.18 on 2023-04-06 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_auto_20230406_1403'),
        ('books', '0002_20230329_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='book',
            name='other_authors',
            field=models.ManyToManyField(related_name='other_author', to='author.Author'),
        ),
    ]