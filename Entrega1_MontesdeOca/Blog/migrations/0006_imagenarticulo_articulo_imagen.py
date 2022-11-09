# Generated by Django 4.1.1 on 2022-11-08 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_articulo_subtitulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenArticulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Blog.imagenarticulo'),
            preserve_default=False,
        ),
    ]
