# Generated by Django 5.0.4 on 2024-07-11 11:58

import django.db.models.deletion
from django.db import migrations, models
from datetime import date

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_rename_subject_student_subjects_and_more'),
    ]

    state_operations = [
        migrations.CreateModel(
            name='StudentEnrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.subject')),
            ],
        ),
        migrations.AlterModelTable(
            name='studentenrollment',
            table='main_app_student_subjects',
        ),
        migrations.AlterField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(through='main_app.StudentEnrollment', to='main_app.Subject'),
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations),
        migrations.AddField(
            model_name='StudentEnrollment',
            name='enrollment_date',
            field=models.DateField(default=date.today),
        ),
        migrations.AddField(
            model_name='StudentEnrollment',
            name='grade',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')],
                                   max_length=1, null=True),
        ),
        migrations.AlterModelTable(
            name='studentenrollment',
            table=None,
        ),
    ]


    # operations = [
    #     migrations.CreateModel(
    #         name='StudentEnrollment',
    #         fields=[
    #             ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    #             ('enrollment_date', models.DateField(auto_now_add=True)),
    #             ('grade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=1)),
    #             ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.student')),
    #             ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.subject')),
    #         ],
    #     ),
    #     migrations.AlterField(
    #         model_name='student',
    #         name='subjects',
    #         field=models.ManyToManyField(through='main_app.StudentEnrollment', to='main_app.subject'),
    #     ),
    # ]