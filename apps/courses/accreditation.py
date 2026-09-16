"""
Accreditation Quality Assurance & Educational Taxonomy Standards
Compliant with ABET, AACSB, QAA (UK), NAAC, and the Bologna Process.
"""

BLOOMS_TAXONOMY = {
    'REMEMBER': {
        'level': 1,
        'name': 'Remembering / Knowledge Retrieval',
        'verbs': ['Define', 'Identify', 'List', 'Name', 'Recall', 'Recognize', 'Record', 'Repeat', 'State', 'Underline'],
        'description': 'Retrieving, recognizing, and recalling relevant knowledge from long-term memory.',
        'assessment_types': ['Multiple Choice', 'Fill in the Blanks', 'Term Definition', 'Flashcard Recall']
    },
    'UNDERSTAND': {
        'level': 2,
        'name': 'Understanding / Comprehension',
        'verbs': ['Classify', 'Describe', 'Discuss', 'Explain', 'Express', 'Identify', 'Locate', 'Recognize', 'Report', 'Review'],
        'description': 'Constructing meaning from oral, written, and graphic messages through interpreting, exemplifying, classifying, summarizing, inferring, comparing, and explaining.',
        'assessment_types': ['Concept Summary', 'Short Essay', 'Diagram Labeling', 'Oral Explanation']
    },
    'APPLY': {
        'level': 3,
        'name': 'Applying / Execution',
        'verbs': ['Apply', 'Choose', 'Demonstrate', 'Dramatize', 'Employ', 'Illustrate', 'Interpret', 'Operate', 'Practice', 'Schedule'],
        'description': 'Carrying out or using a procedure through executing or implementing in novel problem domains.',
        'assessment_types': ['Computational Exercises', 'Laboratory Practicum', 'Algorithm Coding', 'Simulation Analysis']
    },
    'ANALYZE': {
        'level': 4,
        'name': 'Analyzing / Differentiation',
        'verbs': ['Analyze', 'Appraise', 'Calculate', 'Categorize', 'Compare', 'Contrast', 'Criticize', 'Differentiate', 'Discriminate', 'Distinguish'],
        'description': 'Breaking material into constituent parts, determining how the parts relate to one another and to an overall structure or purpose.',
        'assessment_types': ['Case Studies', 'Troubleshooting Scenarios', 'Asymptotic Proofs', 'Data Dissection']
    },
    'EVALUATE': {
        'level': 5,
        'name': 'Evaluating / Critical Judgment',
        'verbs': ['Appraise', 'Argue', 'Assess', 'Attach', 'Choose', 'Defend', 'Estimate', 'Judge', 'Predict', 'Rate', 'Score'],
        'description': 'Making judgments based on criteria and standards through checking and critiquing.',
        'assessment_types': ['Peer Code Reviews', 'Security Architecture Audits', 'Design Trade-off Defenses', 'Ethical Debates']
    },
    'CREATE': {
        'level': 6,
        'name': 'Creating / Synthesis & Innovation',
        'verbs': ['Arrange', 'Assemble', 'Categorize', 'Collect', 'Combine', 'Comply', 'Compose', 'Construct', 'Create', 'Design', 'Develop'],
        'description': 'Putting elements together to form a coherent or functional whole; reorganizing elements into a new pattern or structure.',
        'assessment_types': ['Senior Capstone Projects', 'Hardware Prototypes', 'Open-Source Contributions', 'Original Research']
    }
}

ABET_STUDENT_OUTCOMES = {
    'SO-1': {
        'code': 'SO-1',
        'title': 'Complex Problem Solving',
        'description': 'An ability to identify, formulate, and solve complex engineering problems by applying principles of engineering, science, and mathematics.',
        'performance_indicators': [
            'Applies fundamental mathematical and scientific principles to model engineering systems.',
            'Formulates well-defined problem statements from ambiguous real-world requirements.',
            'Evaluates analytical and computational solution alternatives systematically.'
        ]
    },
    'SO-2': {
        'code': 'SO-2',
        'title': 'Engineering Design & Constraints',
        'description': 'An ability to apply engineering design to produce solutions that meet specified needs with consideration of public health, safety, and welfare, as well as global, cultural, social, environmental, and economic factors.',
        'performance_indicators': [
            'Designs components, systems, or processes meeting functional specifications within realistic constraints.',
            'Evaluates public safety, occupational health, and regulatory compliance standards.',
            'Assesses environmental sustainability and economic lifecycle feasibility.'
        ]
    },
    'SO-3': {
        'code': 'SO-3',
        'title': 'Effective Professional Communication',
        'description': 'An ability to communicate effectively with a range of audiences through written, oral, and visual media.',
        'performance_indicators': [
            'Prepares clear, structured technical reports, design documentation, and specifications.',
            'Delivers persuasive, well-organized technical presentations to diverse stakeholder groups.',
            'Creates professional engineering drawings, schematics, and system architecture diagrams.'
        ]
    },
    'SO-4': {
        'code': 'SO-4',
        'title': 'Ethical & Professional Responsibility',
        'description': 'An ability to recognize ethical and professional responsibilities in engineering situations and make informed judgments, which must consider the impact of engineering solutions in global, economic, environmental, and societal contexts.',
        'performance_indicators': [
            'Identifies ethical dilemmas and applies professional engineering codes of ethics (IEEE, ACM, ASME).',
            'Analyzes the societal and environmental ramifications of technological deployments.',
            'Demonstrates accountability, intellectual property respect, and confidentiality compliance.'
        ]
    },
    'SO-5': {
        'code': 'SO-5',
        'title': 'Collaborative Teamwork & Leadership',
        'description': 'An ability to function effectively on a team whose members together provide leadership, create a collaborative and inclusive environment, establish goals, plan tasks, and meet objectives.',
        'performance_indicators': [
            'Contributes constructively to interdisciplinary team goals and deliverables.',
            'Demonstrates effective project management, task breakdown, and schedule tracking.',
            'Fosters an inclusive, collaborative climate that resolves conflicts constructively.'
        ]
    },
    'SO-6': {
        'code': 'SO-6',
        'title': 'Experimentation & Data Analysis',
        'description': 'An ability to develop and conduct appropriate experimentation, analyze and interpret data, and use engineering judgment to draw conclusions.',
        'performance_indicators': [
            'Designs and conducts controlled laboratory experiments safely and methodically.',
            'Applies statistical tools to analyze measurement errors and confidence intervals.',
            'Draws scientifically defensible conclusions from experimental findings.'
        ]
    },
    'SO-7': {
        'code': 'SO-7',
        'title': 'Continuous & Autonomous Learning',
        'description': 'An ability to acquire and apply new knowledge as needed, using appropriate learning strategies.',
        'performance_indicators': [
            'Demonstrates self-directed learning to master emerging tools, libraries, and frameworks.',
            'Critically evaluates peer-reviewed literature, patents, and industry whitepapers.',
            'Engages in lifelong professional development and industry certification programs.'
        ]
    }
}
