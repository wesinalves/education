# Generated by Django 4.2.9 on 2024-01-16 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webadmin', '0002_course_price_alter_course_banner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='grade',
        ),
        migrations.AddField(
            model_name='coursestudent',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='webadmin.payment'),
        ),
        migrations.AddField(
            model_name='payment',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webadmin.course'),
        ),
        migrations.AddField(
            model_name='payment',
            name='recurrent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='payment',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webadmin.student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promotion',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promotion',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='promotion',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='coursestudent',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='coursestudent',
            name='grade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(null=True),
        ),
    ]
