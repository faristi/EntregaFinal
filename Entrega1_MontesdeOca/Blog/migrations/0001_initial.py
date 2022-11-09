# Generated by Django 4.0.5 on 2022-10-12 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Articulo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=60)),
                ("texto", models.TextField()),
                ("fecha", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Autor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=40)),
                ("apellido", models.CharField(max_length=40)),
                ("profesion", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Lector",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=40)),
                ("apellido", models.CharField(max_length=40)),
                ("profesion", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Seccion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Reseña",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("reseña", models.TextField()),
                (
                    "articulo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Blog.articulo"
                    ),
                ),
                (
                    "lector",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Blog.lector"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="articulo",
            name="autor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Blog.autor"
            ),
        ),
    ]
