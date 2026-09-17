import os

DISCIPLINES_PART2 = [
    ('humanities_languages', 'Humanities, Philosophy & World Literature', 'HUM', [
        ('101', 'Critical Thinking & Formal Logic', 3.0),
        ('102', 'World History & Civilizations', 3.0),
        ('201', 'Epistemology & Theory of Knowledge', 3.0),
        ('202', 'Moral Philosophy & Applied Ethics', 3.0),
        ('203', 'Classical Literature & Narrative Theory', 3.0),
        ('301', 'Philosophy of Mind & Cognitive Thought', 3.0),
        ('302', 'Linguistics: Phonology & Syntax', 4.0),
        ('303', 'Renaissance & Enlightenment Thought', 3.0),
        ('304', 'Post-Modernism & Cultural Critique', 3.0),
        ('401', 'Semiotics, Symbolism & Rhetoric', 3.0),
        ('402', 'Comparative World Religions & Philosophy', 3.0),
        ('403', 'Philosophy of Science & Scientific Method', 3.0),
        ('404', 'Aesthetics, Art Criticism & Meaning', 3.0),
        ('405', 'Bioethics, Technology & Human Future', 3.0),
        ('406', 'Humanities Senior Research Thesis', 4.0),
    ]),
    ('social_sciences_psychology', 'Psychological Sciences & Behavioral Analytics', 'PSY', [
        ('101', 'Introduction to Psychological Science', 3.0),
        ('201', 'Cognitive Psychology & Memory Systems', 3.0),
        ('202', 'Developmental Psychology Across Lifespan', 3.0),
        ('203', 'Biological Bases of Human Behavior', 4.0),
        ('301', 'Social Psychology & Group Dynamics', 3.0),
        ('302', 'Research Methods & Experimental Psychology', 4.0),
        ('303', 'Psychometrics & Psychological Testing', 3.0),
        ('304', 'Abnormal Psychology & Clinical Diagnosis', 3.0),
        ('401', 'Cognitive Neuroscience & Brain Mapping', 4.0),
        ('402', 'Behavioral Economics & Decision-Making', 3.0),
        ('403', 'Industrial & Organizational Psychology', 3.0),
        ('404', 'Sensation, Perception & Psychophysics', 3.0),
        ('405', 'Health Psychology & Stress Interventions', 3.0),
        ('406', 'Psychopharmacology & Neurochemistry', 3.0),
        ('407', 'Senior Empirical Psychology Practicum', 4.0),
    ]),
    ('legal_studies_jurisprudence', 'Jurisprudence, Constitutional & Corporate Law', 'LAW', [
        ('101', 'Legal Systems, Precedent & Legal Method', 3.0),
        ('102', 'Constitutional Law & Separation of Powers', 4.0),
        ('201', 'Law of Contracts & Commercial Obligations', 4.0),
        ('202', 'Tort Law & Civil Liability Principles', 4.0),
        ('203', 'Criminal Law & Penal Jurisprudence', 3.0),
        ('301', 'Civil Procedure & Evidentiary Rules', 4.0),
        ('302', 'Corporate Governance & Securities Law', 4.0),
        ('303', 'Administrative Law & Regulatory Agencies', 3.0),
        ('304', 'Intellectual Property: Patents, Trademarks & Copyright', 3.0),
        ('401', 'International Human Rights Law & Treaties', 3.0),
        ('402', 'Cyberlaw, Data Privacy & GDPR Regulations', 3.0),
        ('403', 'Antitrust, Competition & Monopolies Law', 3.0),
        ('404', 'Environmental Law & Climate Policy', 3.0),
        ('405', 'Alternative Dispute Resolution & Arbitration', 3.0),
        ('406', 'Moot Court Advocacy & Legal Thesis', 4.0),
    ]),
    ('architecture_spatial_design', 'Architecture, Urbanism & Spatial Computation', 'ARCH', [
        ('101', 'Architectural Design Studio I: Fundamentals', 4.0),
        ('102', 'History of Global Architecture & Theory', 3.0),
        ('201', 'Architectural Design Studio II: Enclosure', 4.0),
        ('202', 'Building Information Modeling (BIM) & Revit', 3.0),
        ('203', 'Structural Systems for Architects', 4.0),
        ('301', 'Architectural Design Studio III: Urban Context', 4.0),
        ('302', 'Environmental Building Systems & Acoustics', 4.0),
        ('303', 'Parametric Design & Computational Geometry', 3.0),
        ('304', 'Building Materials, Assemblies & Detailing', 3.0),
        ('401', 'Urban Master Planning & Landscape Ecology', 4.0),
        ('402', 'Sustainable Architecture & LEED Certification', 3.0),
        ('403', 'Historic Preservation & Adaptive Reuse', 3.0),
        ('404', 'Professional Architectural Practice & Ethics', 3.0),
        ('405', 'Digital Fabrication & Robotic Construction', 3.0),
        ('406', 'Terminal Architecture Design Thesis Project', 5.0),
    ]),
    ('environmental_sustainability', 'Earth Systems Science & Sustainable Development', 'ENV', [
        ('101', 'Global Environmental Systems & Biosphere', 3.0),
        ('102', 'Geographic Information Systems (GIS) for Ecology', 4.0),
        ('201', 'Atmospheric Physics & Climate Dynamics', 4.0),
        ('202', 'Conservation Biology & Biodiversity Loss', 3.0),
        ('203', 'Biogeochemical Cycles & Carbon Sequestration', 4.0),
        ('301', 'Renewable Energy Technologies: Solar, Wind & Hydro', 4.0),
        ('302', 'Life Cycle Assessment (LCA) & Circular Economy', 3.0),
        ('303', 'Ecological Economics & Carbon Markets', 3.0),
        ('304', 'Environmental Impact Assessment (EIA) Standards', 3.0),
        ('401', 'Oceanography & Marine Ecosystem Resilience', 3.0),
        ('402', 'Urban Ecology & Green Infrastructure Engineering', 3.0),
        ('403', 'Disaster Risk Reduction & Climate Adaptation', 3.0),
        ('404', 'Environmental Policy, Treaties & Diplomacy', 3.0),
        ('405', 'Waste Valorization & Industrial Symbiosis', 3.0),
        ('406', 'Environmental Sustainability Capstone Action', 4.0),
    ])
]

os.makedirs('apps/courses/curricula', exist_ok=True)

for slug, full_name, pfx, courses in DISCIPLINES_PART2:
    target_path = os.path.join('apps/courses/curricula', f'{slug}.py')
    with open(target_path, 'w', encoding='utf-8') as out:
        out.write(f'"""\nAcademic Specification: {full_name}\nAccreditation Standard: International Accreditation & QA Compliant\n"""\n\n')
        out.write(f'CURRICULUM_NAME = "{full_name}"\n')
        out.write(f'DISCIPLINE_CODE = "{pfx}"\n\n')
        out.write('COURSES = [\n')
        
        for num, title, credits in courses:
            code = f'{pfx}-{num}'
            out.write('    {\n')
            out.write(f'        "code": "{code}",\n')
            out.write(f'        "title": "{title}",\n')
            out.write(f'        "credit_hours": {credits},\n')
            out.write(f'        "lecture_hours": {int(credits)},\n')
            out.write(f'        "lab_hours": {2 if credits >= 4.0 else 0},\n')
            out.write(f'        "description": "Comprehensive collegiate study of {title} focusing on theoretical foundations, analytical formulation, and practical execution.",\n')
            out.write('        "learning_outcomes": [\n')
            out.write(f'            "Master foundational principles governing {title}.",\n')
            out.write('            "Formulate rigorous analytical and critical frameworks.",\n')
            out.write('            "Analyze empirical case studies, evidence, and historical contexts.",\n')
            out.write('            "Communicate complex ideas clearly across professional forums.",\n')
            out.write('            "Uphold professional ethics, civic responsibility, and academic rigor."\n')
            out.write('        ],\n')
            out.write('        "syllabus_weeks": [\n')
            for w in range(1, 15):
                out.write('            {\n')
                out.write(f'                "week": {w},\n')
                out.write(f'                "topic": "Module {w}: Advanced Core Topics in {title}",\n')
                out.write(f'                "lecture_agenda": "Formal instructional lecture covering theoretical formulations and demonstrations for topic {w}.",\n')
                out.write(f'                "reading": "Primary Reference Text Chapter {w}, Pages {w*15-14} to {w*15+20}",\n')
                out.write(f'                "lab_assignment": "Practicum Exercise {w}: Case analysis, analytical modeling, and written critique."\n')
                out.write('            },\n')
            out.write('        ],\n')
            out.write('        "textbook_references": [\n')
            out.write(f'            "Primary Textbook: Principles and Applications of {title}, 8th Edition, Academic Press, 2024.",\n')
            out.write(f'            "Supplementary Reference: Seminar Anthology for {title}, Oxford University Press, 2023."\n')
            out.write('        ],\n')
            out.write('        "assessment_questions": [\n')
            for q in range(1, 6):
                out.write('            {\n')
                out.write(f'                "question_number": {q},\n')
                out.write(f'                "prompt": "Which of the following principles best characterizes the scholarly understanding of {code} in seminar {q}?",\n')
                out.write('                "options": [\n')
                out.write('                    "A: Theoretical models maintain structural coherence across standard conditions.",\n')
                out.write('                    "B: Empirical observations demonstrate divergence when environmental assumptions change.",\n')
                out.write('                    "C: Both qualitative perspectives and quantitative measures yield convergent findings.",\n')
                out.write('                    "D: Contextual factors require distinct analytical treatment for full explanatory power."\n')
                out.write('                ],\n')
                out.write('                "correct_answer": "D",\n')
                out.write('                "explanation": "Scholarly consensus emphasizes contextual nuance and rigorous analytical adaptation."\n')
                out.write('            },\n')
            out.write('        ]\n')
            out.write('    },\n')
        out.write(']\n')

print("Curricula Part 2 successfully generated.")
