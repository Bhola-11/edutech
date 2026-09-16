import datetime
from django.core.management.base import BaseCommand
from django.utils import timezone
from apps.accounts.models import User
from apps.core.constants import UserRoleChoices, AcademicLevelChoices
from apps.institutions.models import Institution, Campus, Faculty, AcademicDepartment, AcademicSession, Semester, Classroom
from apps.courses.models import Program, CourseCategory, Course, CourseModule, Lesson, CourseInstructorAllocation, CourseReview
from apps.enrollments.models import AdmissionCycle, AdmissionApplication, Batch, StudentEnrollment, CourseProgress
from apps.profiles.models import StudentProfile, InstructorProfile, AcademicCredential

class Command(BaseCommand):
    help = 'Seeds initial realistic Phase 1 enterprise data into SQLite database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Beginning Phase 1 data seeding...'))

        # 1. Create SuperUser
        super_admin, _ = User.objects.get_or_create(
            email='admin@edutech.edu',
            defaults={
                'username': 'superadmin',
                'first_name': 'Global',
                'last_name': 'Administrator',
                'role': UserRoleChoices.SUPERADMIN,
                'is_staff': True,
                'is_superuser': True,
                'is_verified': True,
            }
        )
        super_admin.set_password('Admin@12345')
        super_admin.save()
        self.stdout.write(self.style.SUCCESS('Superadmin user created/verified.'))

        # 2. Institutions
        inst, _ = Institution.objects.get_or_create(
            code='MIT-GLOBAL',
            defaults={
                'name': 'Massachusetts Institute of Technology & Global Science',
                'motto': 'Mens et Manus (Mind and Hand)',
                'established_year': 1861,
                'website': 'https://mit.edu',
                'contact_email': 'admissions@mit.edu',
                'contact_phone': '+1 (617) 253-1000',
                'address_line_1': '77 Massachusetts Ave',
                'city': 'Cambridge',
                'state_province': 'Massachusetts',
                'postal_code': '02139',
                'country': 'United States',
                'accreditation_body': 'New England Commission of Higher Education',
                'accreditation_grade': 'Grade A++',
                'timezone': 'America/New_York',
            }
        )

        # 3. Campuses
        campus_main, _ = Campus.objects.get_or_create(
            institution=inst,
            code='CAMBRIDGE-MAIN',
            defaults={
                'name': 'Cambridge Main Campus',
                'campus_type': 'MAIN',
                'address': '77 Massachusetts Ave, Cambridge, MA',
                'city': 'Cambridge',
                'state': 'MA',
                'country': 'United States',
                'capacity': 12000,
            }
        )

        campus_tech, _ = Campus.objects.get_or_create(
            institution=inst,
            code='SV-CENTER',
            defaults={
                'name': 'Silicon Valley Technology Center',
                'campus_type': 'REGIONAL',
                'address': '100 Innovation Way, San Jose, CA',
                'city': 'San Jose',
                'state': 'CA',
                'country': 'United States',
                'capacity': 3500,
            }
        )

        # 4. Faculty & Academic Department
        faculty_eng, _ = Faculty.objects.get_or_create(
            institution=inst,
            code='SOE',
            defaults={
                'name': 'School of Engineering & Computing',
                'description': 'Pioneering scientific discovery and engineering breakthroughs for humanity.'
            }
        )

        dept_cs, _ = AcademicDepartment.objects.get_or_create(
            faculty=faculty_eng,
            code='EECS',
            defaults={
                'campus': campus_main,
                'name': 'Electrical Engineering & Computer Science',
                'contact_email': 'eecs-chair@mit.edu',
                'office_location': 'Building 38, Room 401',
            }
        )

        # 5. Academic Sessions & Semesters
        session, _ = AcademicSession.objects.get_or_create(
            institution=inst,
            academic_year='2026-2027',
            defaults={
                'name': '2026-2027 Academic Year',
                'start_date': datetime.date(2026, 9, 1),
                'end_date': datetime.date(2027, 6, 15),
                'is_current': True,
            }
        )

        semester_fall, _ = Semester.objects.get_or_create(
            academic_session=session,
            name='Fall 2026 Semester',
            defaults={
                'term_type': 'FALL',
                'start_date': datetime.date(2026, 9, 1),
                'end_date': datetime.date(2026, 12, 20),
                'registration_start_date': datetime.date(2026, 8, 1),
                'registration_end_date': datetime.date(2026, 9, 15),
                'add_drop_deadline': datetime.date(2026, 9, 20),
                'is_current': True,
            }
        )

        # 6. Classrooms
        Classroom.objects.get_or_create(
            campus=campus_main,
            building='Building 10 (Stata Center)',
            room_number='Auditorium 10-250',
            defaults={
                'room_type': 'AUDITORIUM',
                'seating_capacity': 250,
                'has_projector': True,
                'has_computers': True,
                'has_audio_system': True,
            }
        )

        # 7. Degree Program
        prog_cs, _ = Program.objects.get_or_create(
            department=dept_cs,
            code='BS-CS',
            defaults={
                'name': 'Bachelor of Science in Computer Science & Artificial Intelligence',
                'academic_level': AcademicLevelChoices.UNDERGRADUATE,
                'total_credits_required': 128,
                'duration_semesters': 8,
                'description': 'A comprehensive computer science curriculum covering computational theory, software design, and AI models.',
            }
        )

        # 8. Course Category & Courses
        cat_core, _ = CourseCategory.objects.get_or_create(
            code='CS-CORE',
            defaults={'name': 'Computer Science Core Disciplines', 'description': 'Foundational programming and algorithmic disciplines.'}
        )

        course_101, _ = Course.objects.get_or_create(
            code='CS-101',
            defaults={
                'department': dept_cs,
                'category': cat_core,
                'title': 'Introduction to Computer Science & Python Programming',
                'credit_hours': 4.0,
                'lecture_hours': 3,
                'lab_hours': 2,
                'academic_level': AcademicLevelChoices.UNDERGRADUATE,
                'summary': 'An introduction to computational thinking, algorithm formulation, and practical software engineering using Python 3.',
                'description': 'Students explore computational problem solving, data abstraction, object-oriented concepts, and algorithmic complexity.',
                'is_featured': True,
            }
        )
        course_101.programs.add(prog_cs)

        course_204, _ = Course.objects.get_or_create(
            code='CS-204',
            defaults={
                'department': dept_cs,
                'category': cat_core,
                'title': 'Data Structures & Advanced Algorithmic Analysis',
                'credit_hours': 4.0,
                'lecture_hours': 3,
                'lab_hours': 2,
                'academic_level': AcademicLevelChoices.UNDERGRADUATE,
                'summary': 'Comprehensive design and empirical analysis of fundamental data structures: trees, graphs, heaps, and hashing.',
                'description': 'Topics include asymptotic analysis (Big-O, Omega, Theta), balanced search trees, graph traversals, and dynamic programming.',
                'is_featured': True,
            }
        )
        course_204.programs.add(prog_cs)
        course_204.prerequisites.add(course_101)

        # 9. Modules & Lessons for CS-101
        mod_1, _ = CourseModule.objects.get_or_create(
            course=course_101,
            order=1,
            defaults={
                'title': 'Computational Problem Solving & Python Syntax',
                'summary': 'Variables, memory models, conditionals, loops, and functional encapsulation.',
                'estimated_hours': 6.0,
            }
        )

        Lesson.objects.get_or_create(
            module=mod_1,
            order=1,
            defaults={
                'title': 'Architecture of Computing: Memory, Registers & the Python Runtime',
                'content_type': 'ARTICLE',
                'duration_minutes': 45,
                'is_free_preview': True,
                'body_text': 'Welcome to the foundational module. In this lesson, we study how programs compile to bytecode and execute in modern runtime environments.',
            }
        )

        Lesson.objects.get_or_create(
            module=mod_1,
            order=2,
            defaults={
                'title': 'Control Flow, Functional Abstraction & Recursion',
                'content_type': 'ARTICLE',
                'duration_minutes': 50,
                'is_free_preview': False,
                'body_text': 'Recursion allows expressing elegant solutions by decomposing problems into identical subproblems with well-defined base termination conditions.',
            }
        )

        # 10. Create Faculty Instructor User
        instructor_user, _ = User.objects.get_or_create(
            email='dr.alan.turing@edutech.edu',
            defaults={
                'username': 'alanturing',
                'first_name': 'Alan',
                'last_name': 'Turing',
                'role': UserRoleChoices.INSTRUCTOR,
                'institution': inst,
                'campus': campus_main,
                'department': dept_cs,
                'is_staff': True,
                'is_verified': True,
            }
        )
        instructor_user.set_password('Admin@12345')
        instructor_user.save()

        InstructorProfile.objects.get_or_create(
            user=instructor_user,
            defaults={
                'employee_id': 'FAC-MIT-1001',
                'designation': 'PROFESSOR',
                'office_room': 'Building 38, Room 410',
                'office_hours': 'Mon & Wed 2:00 PM - 4:00 PM EST',
                'research_interests': 'Theoretical computer science, artificial intelligence, cryptanalysis, and machine intelligence.',
            }
        )

        CourseInstructorAllocation.objects.get_or_create(
            course=course_101,
            instructor=instructor_user,
            semester=semester_fall,
            defaults={'is_lead': True}
        )

        # 11. Create Student User
        student_user, _ = User.objects.get_or_create(
            email='student.alex@edutech.edu',
            defaults={
                'username': 'alexjohnson',
                'first_name': 'Alex',
                'last_name': 'Johnson',
                'role': UserRoleChoices.STUDENT,
                'institution': inst,
                'campus': campus_main,
                'department': dept_cs,
                'is_verified': True,
            }
        )
        student_user.set_password('Admin@12345')
        student_user.save()

        StudentProfile.objects.get_or_create(
            user=student_user,
            defaults={
                'roll_number': 'CS-2026-0042',
                'registration_number': 'REG-2026-90412',
                'program': prog_cs,
                'current_semester': semester_fall,
                'cgpa': 3.92,
                'blood_group': 'O+',
            }
        )

        # 12. Student Enrollment & Progress
        StudentEnrollment.objects.get_or_create(
            student=student_user,
            course=course_101,
            semester=semester_fall,
            defaults={'status': 'ACTIVE'}
        )

        CourseProgress.objects.get_or_create(
            student=student_user,
            course=course_101,
            defaults={'completion_percentage': 50.0}
        )

        # 13. Admission Cycle
        AdmissionCycle.objects.get_or_create(
            program=prog_cs,
            session=session,
            name='Fall 2026 Undergraduate Admissions',
            defaults={
                'start_date': datetime.date(2026, 6, 1),
                'application_deadline': datetime.date(2026, 8, 15),
                'max_seats': 120,
                'is_open': True,
            }
        )

        self.stdout.write(self.style.SUCCESS('Successfully completed Phase 1 enterprise database seeding!'))
