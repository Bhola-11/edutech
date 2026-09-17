import os

CIP_SERIES = [
    ("01", "Agricultural & Veterinary Sciences", [
        ("01.0000", "Agriculture, General", "Instructional program that focuses on general principles and business of agriculture.", True, ["BACHELOR", "MASTER"]),
        ("01.0101", "Agricultural Business and Management", "Focuses on the application of economics and business principles to the agriculture industry.", False, ["ASSOCIATE", "BACHELOR", "MASTER"]),
        ("01.0102", "Agribusiness/Agricultural Business Operations", "Prepares individuals to manage agricultural businesses, cooperatives, and supply chains.", False, ["ASSOCIATE", "BACHELOR"]),
        ("01.0103", "Agricultural Economics", "Focuses on the systematic analysis of economic issues in food, agriculture, and natural resources.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("01.0201", "Agricultural Mechanization, General", "Focuses on the mechanics and technology used in agricultural systems and machinery.", True, ["ASSOCIATE", "BACHELOR"]),
        ("01.0301", "Agricultural Production Operations", "Focuses on the application of scientific principles to crop and animal production.", False, ["ASSOCIATE", "BACHELOR"]),
        ("01.0901", "Animal Sciences, General", "Focuses on the scientific principles of nutrition, breeding, and management of livestock.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("01.1001", "Food Science", "Focuses on the biological, chemical, and physical nature of food and food processing principles.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("01.1101", "Plant Sciences, General", "Focuses on the scientific study of plant biology, genetics, and physiology for agricultural applications.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("01.1201", "Soil Science and Agronomy", "Focuses on the biological, chemical, and physical properties of soils and soil management.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
    ]),
    ("03", "Natural Resources & Conservation", [
        ("03.0101", "Natural Resources/Conservation, General", "Instructional program focused on the conservation and management of natural systems.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("03.0103", "Environmental Studies", "Focuses on the interaction of humans and natural environments using multi-disciplinary science.", True, ["BACHELOR", "MASTER"]),
        ("03.0104", "Environmental Science", "Focuses on the physical, chemical, and biological analysis of environmental systems and remediation.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("03.0201", "Natural Resources Management and Policy", "Focuses on policy development, administration, and regulatory enforcement of natural resources.", False, ["BACHELOR", "MASTER"]),
        ("03.0501", "Forestry, General", "Focuses on the management, conservation, and harvesting of forest resources and timber.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("03.0601", "Wildlife, Fish and Wildlands Science and Management", "Focuses on the preservation, management, and ecology of wildlife species and habitats.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
    ]),
    ("04", "Architecture & Environmental Design", [
        ("04.0201", "Architecture", "Focuses on the art, science, and business of designing and building structures for human habitation.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("04.0301", "City/Urban, Community and Regional Planning", "Focuses on the structural, social, and economic development of urban and regional spaces.", False, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("04.0401", "Environmental Design/Architecture", "Focuses on integrating physical architecture with natural ecological settings and microclimates.", True, ["BACHELOR", "MASTER"]),
        ("04.0501", "Interior Architecture", "Focuses on the structural and functional design of interior spaces within architectural frameworks.", False, ["BACHELOR", "MASTER"]),
        ("04.0601", "Landscape Architecture", "Focuses on the artistic and ecological design of outdoor public, commercial, and residential spaces.", True, ["BACHELOR", "MASTER"]),
        ("04.0901", "Architectural Technology/Technician", "Prepares individuals to use CAD, BIM, and drafting tools to assist professional architects.", True, ["ASSOCIATE", "BACHELOR"]),
    ]),
    ("09", "Communication, Journalism & Digital Media", [
        ("09.0101", "Speech Communication and Rhetoric", "Focuses on interpersonal, group, and public discourse, rhetoric, and verbal communications.", False, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("09.0102", "Mass Communication/Media Studies", "Focuses on media production, analysis, regulatory policy, and audience reception in society.", False, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("09.0401", "Journalism", "Focuses on reporting, writing, editing, and publishing news stories across digital, print, and broadcast media.", False, ["BACHELOR", "MASTER"]),
        ("09.0701", "Radio and Television", "Focuses on technical production, broadcasting, directing, and programming for audio/video media.", False, ["ASSOCIATE", "BACHELOR"]),
        ("09.0702", "Digital Communication and Media/Multimedia", "Focuses on the creation and dissemination of digital content, interactive media, and streaming.", False, ["ASSOCIATE", "BACHELOR", "MASTER"]),
        ("09.0902", "Public Relations/Image Management", "Focuses on strategic communications, brand advocacy, crisis communications, and reputation management.", False, ["BACHELOR", "MASTER"]),
    ]),
    ("11", "Computer & Information Sciences", [
        ("11.0101", "Computer and Information Sciences, General", "General program on computing theory, algorithms, and software development paradigms.", True, ["ASSOCIATE", "BACHELOR", "MASTER", "DOCTORATE"]),
        ("11.0102", "Artificial Intelligence", "Program on machine learning, natural language processing, neural architectures, and robotics.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("11.0103", "Information Technology", "Program on network management, cloud architectures, enterprise storage, and tech support.", True, ["ASSOCIATE", "BACHELOR", "MASTER"]),
        ("11.0104", "Informatics", "Program on domain-specific application of computing systems in health, sciences, and governance.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("11.0201", "Computer Programming/Programmer, General", "Prepares individuals to write, debug, and maintain code in modern high-level languages.", True, ["ASSOCIATE", "BACHELOR", "CERTIFICATE"]),
        ("11.0301", "Data Processing and Data Processing Technology", "Focuses on automated batch data processing, transactional databases, and ETL systems.", True, ["ASSOCIATE", "BACHELOR"]),
        ("11.0401", "Information Science/Studies", "Program on user experience, information behavior, digital libraries, and search systems.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("11.0501", "Computer Systems Analysis/Analyst", "Prepares individuals to assess enterprise systems and design optimal computational architectures.", True, ["BACHELOR", "MASTER"]),
        ("11.0701", "Computer Science", "Formal scientific study of computability, complexity theory, systems programming, and algorithms.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("11.0801", "Web Page, Digital/Multimedia and Information Resources Design", "Program on front-end web development, responsive CSS, user interaction, and client-side scripting.", False, ["ASSOCIATE", "BACHELOR"]),
        ("11.0802", "Data Modeling/Warehousing and Database Administration", "Program on database normalization, OLAP, star schemas, indexing, and high availability.", True, ["BACHELOR", "MASTER"]),
        ("11.0803", "Computer Graphics", "Program on 3D geometry rendering, ray tracing, shader programming, and virtual reality.", True, ["BACHELOR", "MASTER"]),
        ("11.0804", "Modeling, Virtual Environments and Simulation", "Program on physics simulation engines, computational modeling, and virtual simulations.", True, ["BACHELOR", "MASTER"]),
        ("11.0901", "Computer Systems Networking and Telecommunications", "Program on network topology, routing protocols (BGP/OSPF), SDN, and wireless transmission.", True, ["ASSOCIATE", "BACHELOR", "MASTER"]),
        ("11.1001", "Network and System Administration", "Program on Linux/Windows administration, automation (Ansible/Terraform), and directory services.", True, ["ASSOCIATE", "BACHELOR"]),
        ("11.1002", "System, Networking, and LAN/WAN Management", "Focuses on enterprise campus network infrastructure, switching, VLANs, and firewalling.", True, ["ASSOCIATE", "BACHELOR"]),
        ("11.1003", "Computer and Information Systems Security", "Program on penetration testing, cryptanalysis, zero trust, and security incident response.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("11.1004", "Web/Multimedia Management and Webmaster", "Prepares individuals to administer web server clusters (Nginx/Apache), DNS, and TLS certificates.", False, ["ASSOCIATE", "BACHELOR"]),
        ("11.1005", "Information Technology Project Management", "Focuses on agile, scrum, sprint planning, and budget management for software engineering teams.", False, ["BACHELOR", "MASTER"]),
        ("11.1006", "Computer Support Specialist", "Prepares individuals to provide technical desktop and hardware troubleshooting support.", False, ["ASSOCIATE", "CERTIFICATE"]),
    ]),
    ("14", "Engineering & Advanced Technology", [
        ("14.0101", "Engineering, General", "Comprehensive foundational program in physics, math, and engineering problem-solving.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.0201", "Aerospace, Aeronautical and Astronautical Engineering", "Design of aircraft, orbital launch vehicles, propulsion systems, and orbital satellites.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.0301", "Agricultural Engineering", "Design of machinery, irrigation structures, and environmental remediation for farming.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.0401", "Architectural Engineering", "Design of structural, mechanical, electrical, and lighting systems inside buildings.", True, ["BACHELOR", "MASTER"]),
        ("14.0501", "Bioengineering and Biomedical Engineering", "Application of engineering to medical prosthetics, physiological sensors, and drug delivery.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.0601", "Ceramic Sciences and Engineering", "Program on advanced ceramics, refractory materials, and high-temperature thermal barriers.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.0701", "Chemical Engineering", "Design of large-scale chemical reactors, mass transfer separation, and thermodynamics.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.0801", "Civil Engineering, General", "Design and analysis of public infrastructure, structural concrete, steel, and bridges.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.0802", "Geotechnical and Geoenvironmental Engineering", "Soil bearing mechanics, foundation piles, tunneling, and underground containment structures.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.0803", "Structural Engineering", "Non-linear structural analysis, earthquake ductile detailing, and finite element modeling.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.0804", "Transportation and Highway Engineering", "Geometric highway design, pavement materials, traffic stream theory, and mass transit.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.0805", "Water Resources Engineering", "Hydrology, flood risk modeling, stormwater containment, dams, and municipal aqueducts.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.0901", "Computer Engineering, General", "Design of microprocessors, digital logic, FPGA accelerators, and device firmware.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.0902", "Computer Hardware Engineering", "PCB circuit design, signal integrity analysis, high-speed buses, and silicon validation.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.0903", "Computer Software Engineering", "Large-scale software system architecture, clean design patterns, and automated CI/CD.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.1001", "Electrical and Electronics Engineering", "Circuit analysis, semiconductor physics, microelectronics, power grids, and telecommunications.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.1004", "Telecommunications Engineering", "Cellular networks (5G/6G), RF antenna design, microwave waveguides, and optical fiber.", True, ["BACHELOR", "MASTER"]),
        ("14.1101", "Engineering Mechanics", "Continuum mechanics, elasticity, plasticity, viscoelasticity, and computational fluid dynamics.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.1201", "Engineering Physics", "Integration of quantum physics, lasers, superconductivity, and nanodevice fabrication.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.1301", "Engineering Science", "Rigorous interdisciplinary program emphasizing mathematical foundations of natural phenomena.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.1401", "Environmental/Environmental Health Engineering", "Water/wastewater treatment, air quality scrubbers, hazardous waste management, and GIS.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.1801", "Materials Science and Engineering", "Crystalline structures, phase diagrams, metallurgy, polymers, and biomaterials.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.1901", "Mechanical Engineering", "Thermodynamics, heat transfer, machine element design, vibrations, and mechatronics.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.2001", "Metallurgical Engineering", "Extraction, smelting, refining, and alloy composition of ferrous and non-ferrous metals.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.2101", "Mining and Mineral Engineering", "Subsurface rock mechanics, open-pit mine planning, ventilation, and mineral processing.", True, ["BACHELOR", "MASTER"]),
        ("14.2201", "Naval Architecture and Marine Engineering", "Hydrodynamics of ship hulls, marine propulsion, offshore drilling platforms, and stability.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.2301", "Nuclear Engineering", "Fission reactor physics, neutron transport equations, radiation shielding, and fusion energy.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.2401", "Ocean Engineering", "Coastal sediment transport, wave mechanics, underwater acoustics, and ROV submarines.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.2501", "Petroleum Engineering", "Reservoir simulation, directional drilling, hydraulic fracturing, and well production logging.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.2701", "Systems Engineering", "Lifecycle engineering, requirements verification, risk quantification, and system integration.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.3501", "Industrial Engineering", "Operations research, queuing models, lean manufacturing, ergonomics, and supply chain logistics.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("14.4201", "Mechatronics, Robotics, and Automation Engineering", "Embedded controllers, robotic kinematics, feedback servo control, sensors, and actuators.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
    ]),
    ("26", "Biological & Biomedical Sciences", [
        ("26.0101", "Biology/Biological Sciences, General", "Comprehensive study of cellular processes, genetics, ecology, and evolutionary biology.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("26.0202", "Biochemistry", "Chemical processes within living organisms, enzymatic pathways, and protein folding.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("26.0204", "Molecular Biology", "DNA replication, transcription, RNA processing, gene regulation, and recombinant cloning.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("26.0406", "Cell/Cellular and Molecular Biology", "Organelle functions, signaling cascades, membrane transport, and mitotic cell division.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("26.0502", "Microbiology, General", "Biology of bacteria, viruses, fungi, and protozoa in ecology, disease, and biotechnology.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("26.0801", "Genetics, General", "Mendelian inheritance, population genetics, chromosomal anomalies, and gene therapy.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("26.0901", "Physiology, General", "Functions and vital processes of tissues, organs, and integrated biological systems.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("26.1102", "Biostatistics", "Statistical methodologies applied to clinical trials, epidemiological studies, and public health.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("26.1103", "Bioinformatics", "Computational sequence alignment, genomics annotation, proteomics, and structural modeling.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("26.1201", "Biotechnology", "Application of living organisms and bioprocesses to medicine, agriculture, and industry.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("26.1301", "Ecology", "Interactions of organisms with physical environments, biogeochemical cycles, and biodiversity.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("26.1501", "Neuroscience", "Neuroanatomy, synaptic transmission, cognitive neural circuits, and neurological disorders.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
    ]),
    ("27", "Mathematics & Statistics", [
        ("27.0101", "Mathematics, General", "Symbolic logic, real analysis, abstract algebra, topology, and number theory.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("27.0301", "Applied Mathematics, General", "Mathematical modeling of engineering, fluid, biological, and physical systems.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("27.0303", "Computational Mathematics", "Numerical root finding, matrix decompositions, finite differences, and algorithm stability.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("27.0304", "Computational and Applied Mathematics", "High-performance computing applied to differential equations and scientific simulations.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("27.0305", "Financial Mathematics", "Stochastic calculus, Black-Scholes pricing, interest rate models, and risk management.", True, ["BACHELOR", "MASTER"]),
        ("27.0501", "Statistics, General", "Probability theory, hypothesis testing, linear models, and multivariate analysis.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("27.0502", "Mathematical Statistics and Probability", "Measure-theoretic probability, central limit theorems, and asymptotic inference.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("27.0503", "Mathematics and Statistics", "Integrated curriculum combining pure mathematical theory with empirical statistical methods.", True, ["BACHELOR", "MASTER"]),
        ("27.0601", "Applied Statistics, General", "Regression diagnostics, ANOVA, statistical quality control, and data visualization.", True, ["BACHELOR", "MASTER"]),
    ]),
    ("40", "Physical Sciences", [
        ("40.0101", "Physical Sciences", "Interdisciplinary study of non-living matter, thermodynamics, and physical dynamics.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("40.0201", "Astronomy", "Observational astrophysics, planetary dynamics, stellar evolution, and cosmic expansion.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("40.0202", "Astrophysics", "Relativistic plasma physics, nuclear fusion in stars, black holes, and dark matter.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("40.0501", "Chemistry, General", "Atomic theory, chemical bonding, stoichiometry, and kinetics of organic/inorganic compounds.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("40.0502", "Analytical Chemistry", "Chromatography, mass spectrometry, spectroscopy, and quantitative trace detection.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("40.0504", "Organic Chemistry", "Carbon synthesis, reaction mechanisms, stereochemistry, and spectroscopy NMR analysis.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("40.0506", "Physical Chemistry", "Thermodynamic equations of state, quantum chemistry, and molecular spectroscopy.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("40.0601", "Geology/Earth Science, General", "Plate tectonics, mineralogy, structural geology, stratigraphy, and petrology.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("40.0801", "Physics, General", "Classical mechanics, electromagnetism, special relativity, and quantum mechanics.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("40.0802", "Atomic/Molecular Physics", "Atomic electron configurations, laser spectroscopy, and quantum interactions.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("40.0804", "Elementary Particle Physics", "Standard Model, quarks, leptons, gauge bosons, and quantum field theory (QFT).", True, ["MASTER", "DOCTORATE"]),
        ("40.0806", "Nuclear Physics", "Nuclear shell model, radioactive decay kinetics, fission cross-sections, and particle accelerators.", True, ["MASTER", "DOCTORATE"]),
        ("40.0807", "Optics/Optical Sciences", "Geometric optics, diffraction, wave interference, fiber optics, and laser design.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("40.0810", "Theoretical and Mathematical Physics", "Differential geometry, group representations, string theory, and quantum gravity.", True, ["MASTER", "DOCTORATE"]),
    ]),
    ("52", "Business, Management, Marketing & Finance", [
        ("52.0101", "Business/Commerce, General", "Overview of accounting, commercial law, marketing, management, and global economics.", False, ["ASSOCIATE", "BACHELOR", "MASTER"]),
        ("52.0201", "Business Administration and Management, General", "Corporate planning, organizational strategy, executive leadership, and resource allocation.", False, ["ASSOCIATE", "BACHELOR", "MASTER", "DOCTORATE"]),
        ("52.0203", "Logistics, Materials, and Supply Chain Management", "Inventory control (EOQ), freight logistics, warehouse management, and global sourcing.", False, ["ASSOCIATE", "BACHELOR", "MASTER"]),
        ("52.0204", "Operations Management and Supervision", "Process mapping, quality assurance (Six Sigma), production scheduling, and capacity planning.", False, ["ASSOCIATE", "BACHELOR", "MASTER"]),
        ("52.0205", "Operations Research", "Linear programming, simplex method, queuing theory, and stochastic decision models.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("52.0301", "Accounting", "GAAP/IFRS compliance, audit standards, tax accounting, and financial reporting systems.", False, ["ASSOCIATE", "BACHELOR", "MASTER"]),
        ("52.0302", "Accounting Technology/Technician and Bookkeeping", "Practical financial record keeping, payroll processing, and accounting software tools.", False, ["ASSOCIATE", "CERTIFICATE"]),
        ("52.0304", "Accounting and Finance", "Integrated study of corporate capital allocation, ledger accounts, and investor relations.", False, ["BACHELOR", "MASTER"]),
        ("52.0601", "Business/Managerial Economics", "Pricing strategies, market equilibrium, competitive dynamics, and econometric modeling.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("52.0801", "Finance, General", "Capital budgeting (NPV/IRR), equity valuation, fixed income bonds, and corporate mergers.", False, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("52.0803", "Banking and Financial Support Services", "Commercial bank underwriting, credit risk scoring, liquidity ratios, and central bank rules.", False, ["ASSOCIATE", "BACHELOR"]),
        ("52.0804", "Financial Planning and Services", "Wealth management, personal portfolio allocation, retirement vehicles, and estate planning.", False, ["ASSOCIATE", "BACHELOR"]),
        ("52.0807", "Investments and Securities", "Security analysis, stock market microstructure, hedge fund strategies, and derivatives trading.", False, ["BACHELOR", "MASTER"]),
        ("52.0808", "Public Finance", "Municipal bond financing, public taxation policy, state budgeting, and debt issuance.", False, ["BACHELOR", "MASTER"]),
        ("52.1101", "International Business/Trade/Commerce", "Cross-border trade agreements (WTO), foreign exchange hedging, and multinational management.", False, ["BACHELOR", "MASTER"]),
        ("52.1201", "Management Information Systems, General", "Enterprise ERP systems, database querying, business intelligence, and IT infrastructure.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("52.1301", "Management Science", "Mathematical modeling and quantitative optimization for executive decision-making.", True, ["BACHELOR", "MASTER", "DOCTORATE"]),
        ("52.1302", "Business Statistics", "Time series forecasting, multivariate predictive regression, and customer retention analysis.", True, ["BACHELOR", "MASTER"]),
        ("52.1304", "Actuarial Science", "Mortality tables, life insurance risk modeling, loss reserves, and risk pricing theory.", True, ["BACHELOR", "MASTER"]),
        ("52.1401", "Marketing/Marketing Management, General", "Customer discovery, product positioning, marketing mix (4Ps), and omnichannel advertising.", False, ["ASSOCIATE", "BACHELOR", "MASTER", "DOCTORATE"]),
        ("52.1402", "Marketing Research", "Consumer surveys, focus groups, conjoint analysis, and brand sentiment analytics.", False, ["BACHELOR", "MASTER"]),
        ("52.1403", "International Marketing", "Global market entry strategy, cultural localization, export controls, and foreign distribution.", False, ["BACHELOR", "MASTER"]),
        ("52.1701", "Insurance", "Underwriting risk analysis, property/casualty policies, reinsurance pools, and claims handling.", False, ["ASSOCIATE", "BACHELOR"]),
        ("52.1801", "Sales, Distribution, and Marketing Operations", "B2B sales pipeline management, quota structures, negotiations, and distributor contracts.", False, ["ASSOCIATE", "BACHELOR"]),
    ])
]

os.makedirs('apps/core/standards', exist_ok=True)
target = 'apps/core/standards/cip_catalog_full.py'

with open(target, 'w', encoding='utf-8') as f:
    f.write('"""\nComprehensive National Center for Education Statistics (NCES) CIP Master Catalog\nStandardized taxonomy of collegiate instructional degree programs.\n"""\n\n')
    f.write('CIP_SERIES_CATALOG = [\n')
    for code_series, series_title, programs in CIP_SERIES:
        f.write('    {\n')
        f.write(f'        "series_code": "{code_series}",\n')
        f.write(f'        "series_title": "{series_title}",\n')
        f.write('        "programs": [\n')
        for cip, title, defn, stem, levels in programs:
            f.write('            {\n')
            f.write(f'                "cip_code": "{cip}",\n')
            f.write(f'                "title": "{title}",\n')
            f.write(f'                "definition": "{defn}",\n')
            f.write(f'                "stem_designated": {stem},\n')
            f.write(f'                "degree_levels": {levels},\n')
            f.write('            },\n')
        f.write('        ]\n')
        f.write('    },\n')
    f.write(']\n\n')
    f.write('ALL_CIP_PROGRAMS = [p for s in CIP_SERIES_CATALOG for p in s["programs"]]\n')
    f.write('CIP_BY_CODE = {p["cip_code"]: p for p in ALL_CIP_PROGRAMS}\n')

print(f"Generated cip_catalog_full.py with {sum(len(p[2]) for p in CIP_SERIES)} standardized programs.")
