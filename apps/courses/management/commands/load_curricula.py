import importlib
from django.core.management.base import BaseCommand
from apps.courses.models import Course, CourseCategory, Program, CourseModule, Lesson
from apps.institutions.models import AcademicDepartment, Faculty, Institution

DISCIPLINE_MODULES = [
    'computer_science',
    'artificial_intelligence',
    'cybersecurity',
    'data_science',
    'electrical_engineering',
    'mechanical_engineering',
    'civil_environmental',
    'biomedical_health',
    'business_finance',
    'mathematics_physics',
]

class Command(BaseCommand):
    help = 'Loads complete academic curricula specifications across 10 faculties into database'

    def handle(self, *args, **options):
        inst = Institution.objects.first()
        if not inst:
            self.stderr.write('No institution found. Run seed_phase1 first.')
            return

        total_courses_created = 0
        total_modules_created = 0
        total_lessons_created = 0

        for mod_name in DISCIPLINE_MODULES:
            mod = importlib.import_module(f'apps.courses.curricula.{mod_name}')
            curriculum_name = mod.CURRICULUM_NAME
            code_prefix = mod.DISCIPLINE_CODE
            courses_list = mod.COURSES

            faculty, _ = Faculty.objects.get_or_create(
                institution=inst,
                code=f'FAC-{code_prefix}',
                defaults={'name': f'Faculty of {curriculum_name}'}
            )

            dept, _ = AcademicDepartment.objects.get_or_create(
                faculty=faculty,
                code=f'DEPT-{code_prefix}',
                defaults={'name': f'Department of {curriculum_name}'}
            )

            category, _ = CourseCategory.objects.get_or_create(
                code=f'CAT-{code_prefix}',
                defaults={'name': curriculum_name}
            )

            program, _ = Program.objects.get_or_create(
                department=dept,
                code=f'PROG-{code_prefix}',
                defaults={
                    'name': f'Bachelor of Science in {curriculum_name}',
                    'academic_level': 'UNDERGRADUATE',
                    'total_credits_required': 120,
                    'duration_semesters': 8,
                    'description': f'Comprehensive undergraduate curriculum in {curriculum_name}.'
                }
            )

            for c_data in courses_list:
                course, c_created = Course.objects.get_or_create(
                    code=c_data['code'],
                    defaults={
                        'department': dept,
                        'category': category,
                        'title': c_data['title'],
                        'credit_hours': c_data['credit_hours'],
                        'lecture_hours': c_data['lecture_hours'],
                        'lab_hours': c_data['lab_hours'],
                        'description': c_data['description'],
                        'summary': c_data['description'][:450],
                        'academic_level': 'UNDERGRADUATE',
                        'status': 'ACTIVE'
                    }
                )
                course.programs.add(program)
                if c_created:
                    total_courses_created += 1

                for week_info in c_data['syllabus_weeks']:
                    module, m_created = CourseModule.objects.get_or_create(
                        course=course,
                        order=week_info['week'],
                        defaults={
                            'title': week_info['topic'],
                            'summary': week_info['lecture_agenda'],
                            'estimated_hours': 4.0
                        }
                    )
                    if m_created:
                        total_modules_created += 1

                    lesson, l_created = Lesson.objects.get_or_create(
                        module=module,
                        order=1,
                        defaults={
                            'title': f"{week_info['topic']} - Lecture & Laboratory Guide",
                            'content_type': 'ARTICLE',
                            'duration_minutes': 50,
                            'is_free_preview': (week_info['week'] == 1),
                            'body_text': f"Lecture Content:\n{week_info['lecture_agenda']}\n\nRequired Reading:\n{week_info['reading']}\n\nLaboratory Assignment:\n{week_info['lab_assignment']}"
                        }
                    )
                    if l_created:
                        total_lessons_created += 1

        self.stdout.write(self.style.SUCCESS(
            f'Curricula loaded: {total_courses_created} courses, {total_modules_created} modules, {total_lessons_created} lessons.'
        ))
