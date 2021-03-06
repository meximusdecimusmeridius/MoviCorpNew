# Generated by Django 2.0.4 on 2018-04-20 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email_id', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Departments')),
            ],
            options={
                'verbose_name_plural': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=350)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('open', 'OPEN'), ('closed', 'CLOSED'), ('fixed', 'FIXED'), ('in_progress', 'IN PROGRESS'), ('reopened', 'REOPENED')], max_length=30)),
                ('priority', models.CharField(choices=[('low', 'LOW'), ('medium', 'MEDIUM'), ('high', 'HIGH'), ('critical', 'CRITICAL')], max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('ticket_owner', models.CharField(max_length=250)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Employee')),
            ],
            options={
                'verbose_name_plural': 'tickets',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='emp_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Employee'),
        ),
        migrations.AddField(
            model_name='comments',
            name='ticket_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Tickets'),
        ),
    ]
