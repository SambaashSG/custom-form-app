# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pre_employment_card_no', models.CharField(max_length=50, verbose_name=b'Fav Flick',
                                                    error_messages={b'required': 'Type in your pre-employment card number.',
                                                                    b'invalid': "Pre-employment card number is not correct"})),
                ('mobile_phone_number', models.PositiveIntegerField(max_length=12, verbose_name=b'Fav Flick',
                                                    error_messages={b'required': 'Type in your mobile number',
                                                                    b'invalid': "Mobile number is not correct"})),
                ('voucher_code', models.CharField(max_length=14, verbose_name=b'Fav Flick',
                                                    error_messages={b'required': 'Type in your voucher code',
                                                                    b'invalid': "Voucher code is not correct"})),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
        ),
    ]
