# Generated by Django 4.1.1 on 2023-03-06 06:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question', models.TextField(max_length=5000)),
                ('mark', models.IntegerField(default=5)),
                ('active', models.BooleanField(default=True, verbose_name='status')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_category', to='core.subcategory', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=500)),
                ('is_correct', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True, verbose_name='status')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Create date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fk_question', to='quiz.question')),
            ],
        ),
    ]
