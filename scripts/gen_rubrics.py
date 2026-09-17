import os

os.makedirs('apps/courses', exist_ok=True)
target = 'apps/courses/rubrics.py'

RUBRIC_DOMAINS = [
    ("PROGRAMMING_LAB", "Software Engineering & Programming Laboratory Rubric", [
        ("Code Correctness & Functional Requirements", 35, "Solution satisfies all edge cases, unit tests pass, and algorithm behaves according to specification."),
        ("Algorithmic Complexity & Optimization", 25, "Algorithm achieves optimal time and space complexity; minimal memory footprint and no redundant loops."),
        ("Code Architecture & Clean Code Standards", 20, "Proper modular decomposition, descriptive naming, consistent formatting, and solid adherence to DRY/SOLID principles."),
        ("Error Handling & Boundary Robustness", 10, "Input validation present, exceptions caught and handled gracefully, no uncaught crashes on edge cases."),
        ("Documentation & Unit Test Coverage", 10, "Comprehensive docstrings, inline explanatory comments, and robust automated unit test assertions.")
    ]),
    ("ENGINEERING_DESIGN", "Engineering Capstone & Hardware System Design Rubric", [
        ("Problem Formulation & Requirements Engineering", 20, "Clear identification of societal/engineering need, stakeholder analysis, and quantified performance metrics."),
        ("Conceptual Design & Trade-Off Analysis", 20, "Evaluation of competing design alternatives using decision matrices and quantitative trade-off analysis."),
        ("Detailed Design, Schematics & Simulation", 25, "Complete engineering drawings, circuit schematics, finite element analysis (FEA), and CAD models."),
        ("Physical Prototyping & Experimental Verification", 25, "Functional hardware prototype constructed, rigorous bench testing conducted, and validation data documented."),
        ("Ethical, Environmental & Regulatory Compliance", 10, "Safety standards (OSHA/ISO), environmental lifecycle impact, and engineering professional ethics addressed.")
    ]),
    ("SCIENTIFIC_RESEARCH", "Undergraduate & Graduate Research Thesis Rubric", [
        ("Literature Review & Theoretical Framework", 25, "Thorough synthesis of existing peer-reviewed literature, identification of research gaps, and clear theoretical groundings."),
        ("Research Methodology & Experimental Design", 25, "Methodologically sound experimental or computational design, sample selection, controls, and reproducibility."),
        ("Data Analysis & Quantitative Interpretation", 25, "Statistical rigor, hypothesis testing, error analysis, and accurate visualization of experimental results."),
        ("Discussion, Limitations & Future Work", 15, "Insightful interpretation of findings relative to existing literature, honest acknowledgment of limitations, and future directions."),
        ("Clarity, Scholarly Writing & Citations", 10, "Academic prose quality, standard citation formatting (IEEE/APA), clear figures, and well-organized narrative structure.")
    ]),
    ("BUSINESS_CASE", "Managerial & Executive Business Strategy Rubric", [
        ("Financial Statement & Ratio Analysis", 25, "Accurate liquidity, solvency, profitability, and cash flow analysis using GAAP/IFRS balance sheets."),
        ("Market & Industry Competitive Analysis", 25, "Rigorous application of Porter's Five Forces, PESTEL, and SWOT models to identify competitive advantages."),
        ("Strategic Formulation & Business Model Innovation", 25, "Viable strategic initiatives, go-to-market plan, revenue model, and pricing structure."),
        ("Risk Assessment & Mitigation Playbook", 15, "Identification of macro, operational, supply chain, and regulatory risks with quantified mitigation plans."),
        ("Executive Presentation & Stakeholder Pitch", 10, "Professional slide deck, executive summary clarity, and persuasive defense during Q&A panel.")
    ]),
    ("MEDICAL_CLINICAL", "Biomedical & Clinical Device Engineering Rubric", [
        ("Clinical Need & Patient Safety Analysis", 25, "Identification of unmet clinical need, patient risk assessment (ISO 14971), and biocompatibility considerations."),
        ("Sensor Accuracy, Resolution & Noise Floor", 25, "Signal-to-noise ratio optimization, baseline wander removal, and calibration accuracy."),
        ("Regulatory Strategy & Compliance Roadmap", 20, "Clear classification (FDA Class I/II/III or MDR), 510(k) pathway strategy, and verification testing protocols."),
        ("Biocompatibility & Materials Sterilization", 15, "Material selection (USP Class VI), corrosion resistance, sterilization protocols (autoclave/EtO/gamma)."),
        ("User Experience & Clinical Usability (IEC 62366)", 15, "Ergonomic clinical form factor, intuitive visual alarms, and human factors validation testing.")
    ])
]

with open(target, 'w', encoding='utf-8') as f:
    f.write('"""\nAcademic Assessment & Grading Rubrics Engine\nMulti-criterion evaluation rubrics for collegiate engineering, scientific, and business curricula.\n"""\n\n')
    f.write('RUBRIC_TEMPLATES = [\n')
    for domain_code, domain_title, criteria in RUBRIC_DOMAINS:
        f.write('    {\n')
        f.write(f'        "code": "{domain_code}",\n')
        f.write(f'        "title": "{domain_title}",\n')
        f.write('        "criteria": [\n')
        for crit_name, weight, desc in criteria:
            f.write('            {\n')
            f.write(f'                "name": "{crit_name}",\n')
            f.write(f'                "weight_percentage": {weight},\n')
            f.write(f'                "description": "{desc}",\n')
            f.write('                "scale_levels": {\n')
            f.write('                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},\n')
            f.write('                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},\n')
            f.write('                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},\n')
            f.write('                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}\n')
            f.write('                }\n')
            f.write('            },\n')
        f.write('        ]\n')
        f.write('    },\n')
    f.write(']\n\n')
    f.write('RUBRICS_BY_CODE = {r["code"]: r for r in RUBRIC_TEMPLATES}\n')

print("Generated rubrics.py successfully.")
