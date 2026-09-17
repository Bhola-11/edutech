"""
Academic Assessment & Grading Rubrics Engine
Multi-criterion evaluation rubrics for collegiate engineering, scientific, and business curricula.
"""

RUBRIC_TEMPLATES = [
    {
        "code": "PROGRAMMING_LAB",
        "title": "Software Engineering & Programming Laboratory Rubric",
        "criteria": [
            {
                "name": "Code Correctness & Functional Requirements",
                "weight_percentage": 35,
                "description": "Solution satisfies all edge cases, unit tests pass, and algorithm behaves according to specification.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Algorithmic Complexity & Optimization",
                "weight_percentage": 25,
                "description": "Algorithm achieves optimal time and space complexity; minimal memory footprint and no redundant loops.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Code Architecture & Clean Code Standards",
                "weight_percentage": 20,
                "description": "Proper modular decomposition, descriptive naming, consistent formatting, and solid adherence to DRY/SOLID principles.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Error Handling & Boundary Robustness",
                "weight_percentage": 10,
                "description": "Input validation present, exceptions caught and handled gracefully, no uncaught crashes on edge cases.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Documentation & Unit Test Coverage",
                "weight_percentage": 10,
                "description": "Comprehensive docstrings, inline explanatory comments, and robust automated unit test assertions.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
        ]
    },
    {
        "code": "ENGINEERING_DESIGN",
        "title": "Engineering Capstone & Hardware System Design Rubric",
        "criteria": [
            {
                "name": "Problem Formulation & Requirements Engineering",
                "weight_percentage": 20,
                "description": "Clear identification of societal/engineering need, stakeholder analysis, and quantified performance metrics.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Conceptual Design & Trade-Off Analysis",
                "weight_percentage": 20,
                "description": "Evaluation of competing design alternatives using decision matrices and quantitative trade-off analysis.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Detailed Design, Schematics & Simulation",
                "weight_percentage": 25,
                "description": "Complete engineering drawings, circuit schematics, finite element analysis (FEA), and CAD models.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Physical Prototyping & Experimental Verification",
                "weight_percentage": 25,
                "description": "Functional hardware prototype constructed, rigorous bench testing conducted, and validation data documented.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Ethical, Environmental & Regulatory Compliance",
                "weight_percentage": 10,
                "description": "Safety standards (OSHA/ISO), environmental lifecycle impact, and engineering professional ethics addressed.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
        ]
    },
    {
        "code": "SCIENTIFIC_RESEARCH",
        "title": "Undergraduate & Graduate Research Thesis Rubric",
        "criteria": [
            {
                "name": "Literature Review & Theoretical Framework",
                "weight_percentage": 25,
                "description": "Thorough synthesis of existing peer-reviewed literature, identification of research gaps, and clear theoretical groundings.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Research Methodology & Experimental Design",
                "weight_percentage": 25,
                "description": "Methodologically sound experimental or computational design, sample selection, controls, and reproducibility.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Data Analysis & Quantitative Interpretation",
                "weight_percentage": 25,
                "description": "Statistical rigor, hypothesis testing, error analysis, and accurate visualization of experimental results.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Discussion, Limitations & Future Work",
                "weight_percentage": 15,
                "description": "Insightful interpretation of findings relative to existing literature, honest acknowledgment of limitations, and future directions.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Clarity, Scholarly Writing & Citations",
                "weight_percentage": 10,
                "description": "Academic prose quality, standard citation formatting (IEEE/APA), clear figures, and well-organized narrative structure.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
        ]
    },
    {
        "code": "BUSINESS_CASE",
        "title": "Managerial & Executive Business Strategy Rubric",
        "criteria": [
            {
                "name": "Financial Statement & Ratio Analysis",
                "weight_percentage": 25,
                "description": "Accurate liquidity, solvency, profitability, and cash flow analysis using GAAP/IFRS balance sheets.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Market & Industry Competitive Analysis",
                "weight_percentage": 25,
                "description": "Rigorous application of Porter's Five Forces, PESTEL, and SWOT models to identify competitive advantages.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Strategic Formulation & Business Model Innovation",
                "weight_percentage": 25,
                "description": "Viable strategic initiatives, go-to-market plan, revenue model, and pricing structure.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Risk Assessment & Mitigation Playbook",
                "weight_percentage": 15,
                "description": "Identification of macro, operational, supply chain, and regulatory risks with quantified mitigation plans.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Executive Presentation & Stakeholder Pitch",
                "weight_percentage": 10,
                "description": "Professional slide deck, executive summary clarity, and persuasive defense during Q&A panel.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
        ]
    },
    {
        "code": "MEDICAL_CLINICAL",
        "title": "Biomedical & Clinical Device Engineering Rubric",
        "criteria": [
            {
                "name": "Clinical Need & Patient Safety Analysis",
                "weight_percentage": 25,
                "description": "Identification of unmet clinical need, patient risk assessment (ISO 14971), and biocompatibility considerations.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Sensor Accuracy, Resolution & Noise Floor",
                "weight_percentage": 25,
                "description": "Signal-to-noise ratio optimization, baseline wander removal, and calibration accuracy.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Regulatory Strategy & Compliance Roadmap",
                "weight_percentage": 20,
                "description": "Clear classification (FDA Class I/II/III or MDR), 510(k) pathway strategy, and verification testing protocols.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "Biocompatibility & Materials Sterilization",
                "weight_percentage": 15,
                "description": "Material selection (USP Class VI), corrosion resistance, sterilization protocols (autoclave/EtO/gamma).",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
            {
                "name": "User Experience & Clinical Usability (IEC 62366)",
                "weight_percentage": 15,
                "description": "Ergonomic clinical form factor, intuitive visual alarms, and human factors validation testing.",
                "scale_levels": {
                    "EXEMPLARY": {"points_multiplier": 1.0, "descriptor": "Flawless execution exceeding all expectations."},
                    "PROFICIENT": {"points_multiplier": 0.85, "descriptor": "Strong execution meeting standard collegiate requirements."},
                    "DEVELOPING": {"points_multiplier": 0.70, "descriptor": "Partial understanding with minor defects or oversights."},
                    "UNSATISFACTORY": {"points_multiplier": 0.40, "descriptor": "Substantial failure to meet basic technical standards."}
                }
            },
        ]
    },
]

RUBRICS_BY_CODE = {r["code"]: r for r in RUBRIC_TEMPLATES}
