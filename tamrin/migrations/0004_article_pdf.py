# Generated by Django 3.1.7 on 2021-03-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamrin', '0003_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pdf',
            field=models.FileField(blank=True, default='defaul.pdf', upload_to=''),
        ),
    ]