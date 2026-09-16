"""
National Center for Education Statistics (NCES) - Classification of Instructional Programs (CIP)
Standardized taxonomic scheme for academic programs and degree fields in higher education.
"""

CIP_DIRECTORY = {
    '11.0101': {
        'code': '11.0101',
        'title': 'Computer and Information Sciences, General',
        'definition': 'A general program that focuses on the computer and information sciences and prepares students for various applications.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '11.0102': {
        'code': '11.0102',
        'title': 'Artificial Intelligence',
        'definition': 'A program that focuses on the symbolic and numeric representation and manipulation of information by machine.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '11.0103': {
        'code': '11.0103',
        'title': 'Information Technology',
        'definition': 'A program that focuses on the design of technological information systems and infrastructure.',
        'stem_designated': True,
        'degree_levels': ['ASSOCIATE', 'BACHELOR', 'MASTER']
    },
    '11.0104': {
        'code': '11.0104',
        'title': 'Informatics',
        'definition': 'A program that focuses on computer systems and their integration in specific domains like healthcare, sciences, and governance.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER']
    },
    '11.0201': {
        'code': '11.0201',
        'title': 'Computer Programming/Programmer, General',
        'definition': 'A program that prepares individuals to design and develop software applications across multi-platform runtimes.',
        'stem_designated': True,
        'degree_levels': ['ASSOCIATE', 'CERTIFICATE', 'BACHELOR']
    },
    '11.0401': {
        'code': '11.0401',
        'title': 'Information Science/Studies',
        'definition': 'A program that focuses on the theory, organization, and properties of information systems and user behavior.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '11.0701': {
        'code': '11.0701',
        'title': 'Computer Science',
        'definition': 'A program that focuses on computer theory, computing problems and solutions, and the design of computer systems.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '11.0801': {
        'code': '11.0801',
        'title': 'Web Page, Digital/Multimedia and Information Resources Design',
        'definition': 'A program that prepares individuals to apply HTML, CSS, JavaScript, graphics, and server-side logic to web systems.',
        'stem_designated': False,
        'degree_levels': ['ASSOCIATE', 'BACHELOR']
    },
    '11.0802': {
        'code': '11.0802',
        'title': 'Data Modeling/Warehousing and Database Administration',
        'definition': 'A program that prepares individuals to design, implement, and administer enterprise database infrastructures.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'CERTIFICATE']
    },
    '11.1001': {
        'code': '11.1001',
        'title': 'Network and System Administration/Administrator',
        'definition': 'A program that prepares individuals to manage and configure computer networks and operating system environments.',
        'stem_designated': True,
        'degree_levels': ['ASSOCIATE', 'BACHELOR']
    },
    '11.1003': {
        'code': '11.1003',
        'title': 'Computer and Information Systems Security/Information Assurance',
        'definition': 'A program that prepares individuals to assess security risks, implement cryptosystems, and conduct incident response.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '14.0101': {
        'code': '14.0101',
        'title': 'Engineering, General',
        'definition': 'A program that generally prepares individuals to apply mathematical and scientific principles to solve technical challenges.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '14.0501': {
        'code': '14.0501',
        'title': 'Bioengineering and Biomedical Engineering',
        'definition': 'A program that prepares individuals to apply engineering principles to medicine, healthcare, and physiological systems.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '14.0801': {
        'code': '14.0801',
        'title': 'Civil Engineering, General',
        'definition': 'A program that prepares individuals to apply mathematical and physical principles to the design of infrastructure.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '14.0901': {
        'code': '14.0901',
        'title': 'Computer Engineering, General',
        'definition': 'A program that prepares individuals to apply mathematical and scientific principles to the design of hardware and embedded firmware.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '14.0903': {
        'code': '14.0903',
        'title': 'Computer Software Engineering',
        'definition': 'A program that prepares individuals to apply software engineering principles to large-scale software system design.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '14.1001': {
        'code': '14.1001',
        'title': 'Electrical and Electronics Engineering',
        'definition': 'A program that prepares individuals to apply mathematical and scientific principles to electric circuits, semiconductors, and power.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '14.1901': {
        'code': '14.1901',
        'title': 'Mechanical Engineering',
        'definition': 'A program that prepares individuals to apply mathematical and scientific principles to the design and analysis of mechanical systems.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '27.0101': {
        'code': '27.0101',
        'title': 'Mathematics, General',
        'definition': 'A general program that focuses on the relationships between quantities, magnitudes, and forms through symbolic language.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '27.0301': {
        'code': '27.0301',
        'title': 'Applied Mathematics, General',
        'definition': 'A program that focuses on the application of mathematics to solving problems in engineering, sciences, and industry.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '27.0501': {
        'code': '27.0501',
        'title': 'Statistics, General',
        'definition': 'A program that focuses on the collection, analysis, interpretation, and presentation of quantitative empirical data.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '30.7001': {
        'code': '30.7001',
        'title': 'Data Science, General',
        'definition': 'An interdisciplinary program that prepares individuals to extract knowledge from complex tabular and unstructured data.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '40.0801': {
        'code': '40.0801',
        'title': 'Physics, General',
        'definition': 'A general program that focuses on the basic laws governing energy, matter, space, and time in physical systems.',
        'stem_designated': True,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '52.0101': {
        'code': '52.0101',
        'title': 'Business/Commerce, General',
        'definition': 'A general program that focuses on the administrative and operational aspects of business enterprises.',
        'stem_designated': False,
        'degree_levels': ['ASSOCIATE', 'BACHELOR', 'MASTER']
    },
    '52.0201': {
        'code': '52.0201',
        'title': 'Business Administration and Management, General',
        'definition': 'A program that prepares individuals to plan, organize, direct, and control the functions and processes of a firm.',
        'stem_designated': False,
        'degree_levels': ['ASSOCIATE', 'BACHELOR', 'MASTER', 'DOCTORATE']
    },
    '52.0301': {
        'code': '52.0301',
        'title': 'Accounting',
        'definition': 'A program that prepares individuals to practice the profession of accounting and to perform related financial services.',
        'stem_designated': False,
        'degree_levels': ['ASSOCIATE', 'BACHELOR', 'MASTER']
    },
    '52.0801': {
        'code': '52.0801',
        'title': 'Finance, General',
        'definition': 'A program that generally prepares individuals to plan, manage, and analyze the financial and monetary aspects of firms and portfolios.',
        'stem_designated': False,
        'degree_levels': ['BACHELOR', 'MASTER', 'DOCTORATE']
    }
}
