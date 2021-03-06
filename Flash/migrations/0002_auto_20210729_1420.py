# Generated by Django 3.1.8 on 2021-07-29 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Flash', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='back',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='flashcards',
            name='front',
            field=models.TextField(max_length=200),
        ),
        migrations.AddField(
            model_name='flashcards',
            name='card',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Flash.collectionpoint'),
            preserve_default=False,
        ),
    ]
