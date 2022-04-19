# Generated by Django 4.0.4 on 2022-04-19 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='질문')),
                ('category', models.CharField(choices=[('General', '일반'), ('Account', '계정'), ('Etc', '기타')], default='General', max_length=7, verbose_name='카테고리')),
                ('answer', models.TextField(null=True, verbose_name='답변')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('final_created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일시')),
                ('final_writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faq_final_writer', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faq_writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
