import os

BODIES = [
    ("NECHE", "New England Commission of Higher Education", "United States (Regional)", [
        ("Standard 1: Mission and Purposes", "The institution's mission clearly defines its distinctive character, addressing the educational needs of its students and community."),
        ("Standard 2: Planning and Evaluation", "The institution undertakes planning and evaluation to accomplish and improve its programs, facilities, and financial stability."),
        ("Standard 3: Organization and Governance", "The institution has a system of governance that facilitates the accomplishment of its mission and integrity."),
        ("Standard 4: The Academic Program", "The institution offers undergraduate and graduate programs consistent with its mission, with rigorous curricula and outcome assessments."),
        ("Standard 5: Students", "The institution provides student support services, admissions counseling, and financial aid to promote learner success."),
        ("Standard 6: Teaching, Learning, and Scholarship", "The institution maintains a qualified faculty committed to instructional excellence and scholarly inquiry."),
        ("Standard 7: Institutional Resources", "The institution has physical, financial, technological, and library resources to sustain its educational mission."),
        ("Standard 8: Educational Effectiveness", "The institution systematically collects and analyzes evidence of student learning to enhance curricular outcomes."),
        ("Standard 9: Integrity, Transparency, and Public Disclosure", "The institution subscribes to high ethical standards in management, public disclosures, and academic freedom.")
    ]),
    ("SACSCOC", "Southern Association of Colleges and Schools Commission on Colleges", "United States (Regional)", [
        ("Principle 1: Institutional Integrity", "The institution operates with integrity in all matters, ensuring student welfare, truth in advertising, and academic freedom."),
        ("Principle 2: Mission", "The institution has a clearly defined, published mission statement that guides operational priorities and educational goals."),
        ("Principle 3: Basic Eligibility Standard", "The institution possesses appropriate degree-granting authority and continuous educational operations."),
        ("Principle 4: Governing Board", "The governing board is an active policy-making body responsible for financial soundness and institutional direction."),
        ("Principle 5: Administration and Organization", "The institution has a full-time chief executive officer and qualified administrative officers."),
        ("Principle 6: Faculty", "The institution employs qualified full-time faculty members to ensure curriculum quality and academic oversight."),
        ("Principle 7: Institutional Planning and Effectiveness", "The institution engages in ongoing, integrated, and institution-wide research-based planning and evaluation."),
        ("Principle 8: Student Achievement", "The institution identifies, evaluates, and publishes goals and outcomes for student achievement appropriate to its mission."),
        ("Principle 9: Educational Program Structure", "Educational programs embody a coherent course of study with appropriate general education breadth."),
        ("Principle 10: Educational Policies, Procedures, and Practices", "The institution publishes clear academic policies regarding grading, credit transfer, and graduation requirements."),
        ("Principle 11: Library and Learning Resources", "The institution provides adequate and qualified library staff, collections, and digital information resources."),
        ("Principle 12: Academic and Student Support Services", "The institution provides student support services that promote student learning and campus community."),
        ("Principle 13: Financial and Physical Resources", "The institution possesses financial stability and safe, accessible, and well-maintained physical facilities."),
        ("Principle 14: Transparency and Representation", "The institution complies with federal financial aid mandates and accurate representation to the public.")
    ]),
    ("HLC", "Higher Learning Commission", "United States (Regional)", [
        ("Criterion 1: Mission", "The institution's mission is clear and articulated publicly; it guides the institution's operations."),
        ("Criterion 2: Integrity - Ethical and Responsible Conduct", "The institution acts with integrity; its conduct is ethical and responsible."),
        ("Criterion 3: Teaching and Learning - Quality, Resources, and Support", "The institution provides high quality education, wherever and however its offerings are delivered."),
        ("Criterion 4: Teaching and Learning - Evaluation and Improvement", "The institution demonstrates responsibility for the quality of its educational programs and assesses student learning."),
        ("Criterion 5: Institutional Effectiveness, Resources and Planning", "The institution's resources, structures, and processes are sufficient to fulfill its mission and improve education.")
    ]),
    ("NAAC", "National Assessment and Accreditation Council", "India", [
        ("Criterion 1: Curricular Aspects", "Curriculum design and development, academic flexibility, curriculum enrichment, and stakeholder feedback systems."),
        ("Criterion 2: Teaching-Learning and Evaluation", "Student enrollment and profile, diversity, student-centric teaching methods, teacher quality, and evaluation processes."),
        ("Criterion 3: Research, Innovations and Extension", "Promotion of research, resource mobilization, innovation ecosystems, publications, and social extension activities."),
        ("Criterion 4: Infrastructure and Learning Resources", "Physical facilities, library as a learning resource, IT infrastructure, and campus maintenance systems."),
        ("Criterion 5: Student Support and Progression", "Student mentoring, scholarships, capability enhancement, student participation, and alumni engagement."),
        ("Criterion 6: Governance, Leadership and Management", "Institutional vision and leadership, strategy development, faculty empowerment, and financial management."),
        ("Criterion 7: Institutional Values and Best Practices", "Gender equity, environmental consciousness, green campus initiatives, constitutional values, and institutional distinctiveness.")
    ]),
    ("QAA", "Quality Assurance Agency for Higher Education", "United Kingdom", [
        ("Core Practice 1: Standards", "The provider ensures that the threshold standards for its qualifications are consistent with national qualification frameworks."),
        ("Core Practice 2: Quality", "The provider designs and delivers high-quality, up-to-date courses with credible learning assessments."),
        ("Core Practice 3: Supporting Student Success", "The provider provides fair admissions, transparent academic progression, and effective pastoral support."),
        ("Core Practice 4: Course Monitoring and Review", "The provider monitors and reviews its courses systematically using external examiner reports and student feedback."),
        ("Core Practice 5: Information and Public Transparency", "The provider publishes clear, accurate, and reliable information about courses and outcomes.")
    ]),
    ("TEQSA", "Tertiary Education Quality and Standards Agency", "Australia", [
        ("Domain 1: Student Participation and Attainment", "Admission policies, learning environment, learning outcomes, and qualification issuance."),
        ("Domain 2: Learning Environment", "Facilities, infrastructure, diversity, student well-being, and grievance handling."),
        ("Domain 3: Teaching", "Course design, staffing qualifications, teaching and learning resources, and assessment integrity."),
        ("Domain 4: Research and Research Training", "Research oversight, research training supervision, and research environment integrity."),
        ("Domain 5: Institutional Quality Assurance", "Course monitoring and review, academic governance, and academic integrity policies."),
        ("Domain 6: Governance and Accountability", "Corporate governance, academic governance, and institutional accountability."),
        ("Domain 7: Representation, Information and Public Information", "Accurate representations, student information transparency, and public register compliance.")
    ])
]

os.makedirs('apps/core/standards', exist_ok=True)
target = 'apps/core/standards/accreditation_standards.py'

with open(target, 'w', encoding='utf-8') as f:
    f.write('"""\nGlobal Higher Education Accreditation Bodies & Quality Benchmark Standards\n"""\n\n')
    f.write('ACCREDITATION_FRAMEWORKS = [\n')
    for code, name, jurisdiction, criteria in BODIES:
        f.write('    {\n')
        f.write(f'        "acronym": "{code}",\n')
        f.write(f'        "agency_name": "{name}",\n')
        f.write(f'        "jurisdiction": "{jurisdiction}",\n')
        f.write('        "standards": [\n')
        for crit_title, crit_desc in criteria:
            f.write('            {\n')
            f.write(f'                "title": "{crit_title}",\n')
            f.write(f'                "description": "{crit_desc}",\n')
            f.write('                "audit_rubrics": [\n')
            f.write('                    "Institutional documentation verified against statutory guidelines.",\n')
            f.write('                    "On-site peer review evaluation and stakeholder interviews.",\n')
            f.write('                    "Quantitative outcome metric assessment and continuous improvement plans."\n')
            f.write('                ]\n')
            f.write('            },\n')
        f.write('        ]\n')
        f.write('    },\n')
    f.write(']\n\n')
    f.write('ACCREDITATION_BY_CODE = {a["acronym"]: a for a in ACCREDITATION_FRAMEWORKS}\n')

print("Generated accreditation_standards.py with major international accreditation bodies.")
