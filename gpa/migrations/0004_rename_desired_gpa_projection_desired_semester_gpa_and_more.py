# Generated by Django 5.0.13 on 2025-04-16 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpa', '0003_remove_enrollment_actual_grade_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projection',
            old_name='desired_gpa',
            new_name='desired_semester_gpa',
        ),
        migrations.RemoveField(
            model_name='projection',
            name='course',
        ),
        migrations.RemoveField(
            model_name='projection',
            name='current_gpa',
        ),
        migrations.RemoveField(
            model_name='projection',
            name='required_final_exam_score',
        ),
        migrations.AddField(
            model_name='projection',
            name='projected_cumulative_gpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='projection',
            name='required_average_final_exam_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='projection',
            name='semester',
            field=models.CharField(default='Spring 2025', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projection',
            name='total_credit_hours',
            field=models.PositiveIntegerField(default=3, help_text='Total credit hours for the semester'),
            preserve_default=False,
        ),
    ]
