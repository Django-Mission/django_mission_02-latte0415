# Generated by Django 4.0.4 on 2022-04-19 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0002_inquiry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='final_created_at',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='final_writer',
        ),
        migrations.AddField(
            model_name='faq',
            name='modified_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='최종수정일시'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faq',
            name='modifier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faq_modifier', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='답변내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('modified_at', models.DateTimeField(auto_now_add=True, verbose_name='최종수정일시')),
                ('from_inquiry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.inquiry')),
                ('modifier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_modifier', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
