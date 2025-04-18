# Generated by Django 5.1.6 on 2025-03-30 04:47

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_orderitem_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '۱ ستاره - بسیار ضعیف'), (2, '۲ ستاره - ضعیف'), (3, '۳ ستاره - متوسط'), (4, '۴ ستاره - خوب'), (5, '۵ ستاره - عالی')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='امتیاز')),
                ('comment', models.TextField(blank=True, verbose_name='دیدگاه')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='store.product', verbose_name='محصول')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'نظر محصول',
                'verbose_name_plural': 'نظرات محصولات',
                'unique_together': {('product', 'user')},
            },
        ),
    ]
