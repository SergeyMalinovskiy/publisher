# Generated by Django 3.2.18 on 2023-04-10 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publisher', '0002_alter_publisher_id'),
        ('books', '0004_alter_book_other_authors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('cover_image', models.FileField(upload_to='uploads/%Y_%m_$d')),
                ('is_active', models.BooleanField(default=False)),
                ('publication_datetime', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('books', models.ManyToManyField(null=True, to='books.Book')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='publisher.publisher')),
            ],
        ),
    ]
