import os

TOP_UNIVERSITIES_DATA = [
    ("Harvard University", "HARVARD", "Cambridge", "United States", 1636, "Veritas (Truth)", "info@harvard.edu", "Grade A++", "https://harvard.edu"),
    ("Stanford University", "STANFORD", "Stanford", "United States", 1885, "Die Luft der Freiheit weht", "admissions@stanford.edu", "Grade A++", "https://stanford.edu"),
    ("Massachusetts Institute of Technology", "MIT", "Cambridge", "United States", 1861, "Mens et Manus", "admissions@mit.edu", "Grade A++", "https://mit.edu"),
    ("University of Oxford", "OXFORD", "Oxford", "United Kingdom", 1096, "Dominus Illuminatio Mea", "enquiries@ox.ac.uk", "Grade A++", "https://ox.ac.uk"),
    ("University of Cambridge", "CAMBRIDGE", "Cambridge", "United Kingdom", 1209, "Hinc lucem et pocula sacra", "admissions@cam.ac.uk", "Grade A++", "https://cam.ac.uk"),
    ("California Institute of Technology", "CALTECH", "Pasadena", "United States", 1891, "The truth shall make you free", "admissions@caltech.edu", "Grade A++", "https://caltech.edu"),
    ("ETH Zurich", "ETH-ZURICH", "Zurich", "Switzerland", 1855, "Where the future begins", "info@ethz.ch", "Grade A++", "https://ethz.ch"),
    ("Imperial College London", "IMPERIAL", "London", "United Kingdom", 1907, "Scientia imperii decus et tutamen", "admissions@imperial.ac.uk", "Grade A++", "https://imperial.ac.uk"),
    ("University College London", "UCL", "London", "United Kingdom", 1826, "Cuncti adsint meritaeque expectent praemia palmae", "study@ucl.ac.uk", "Grade A+", "https://ucl.ac.uk"),
    ("National University of Singapore", "NUS", "Singapore", "Singapore", 1905, "Towards a Global Knowledge Enterprise", "admissions@nus.edu.sg", "Grade A++", "https://nus.edu.sg"),
    ("Nanyang Technological University", "NTU", "Singapore", "Singapore", 1991, "A Great Global University", "admissions@ntu.edu.sg", "Grade A+", "https://ntu.edu.sg"),
    ("Tsinghua University", "TSINGHUA", "Beijing", "China", 1911, "Self-Discipline and Social Commitment", "admission@tsinghua.edu.cn", "Grade A++", "https://tsinghua.edu.cn"),
    ("Peking University", "PKU", "Beijing", "China", 1898, "Patriotism, Progress, Democracy, and Science", "admission@pku.edu.cn", "Grade A++", "https://pku.edu.cn"),
    ("University of Tokyo", "UTOKYO", "Tokyo", "Japan", 1877, "Discover Excellence", "contact@u-tokyo.ac.jp", "Grade A++", "https://u-tokyo.ac.jp"),
    ("Kyoto University", "KYOTO", "Kyoto", "Japan", 1897, "Freedom of Academic Culture", "info@kyoto-u.ac.jp", "Grade A+", "https://kyoto-u.ac.jp"),
    ("University of Toronto", "UTORONTO", "Toronto", "Canada", 1827, "Velut arbor aevo (As a tree through the ages)", "admissions@utoronto.ca", "Grade A++", "https://utoronto.ca"),
    ("McGill University", "MCGILL", "Montreal", "Canada", 1821, "Grandescunt Aucta Labore", "admissions@mcgill.ca", "Grade A+", "https://mcgill.ca"),
    ("University of Melbourne", "UNIMELB", "Melbourne", "Australia", 1853, "Postera crescam laude", "study@unimelb.edu.au", "Grade A++", "https://unimelb.edu.au"),
    ("Australian National University", "ANU", "Canberra", "Australia", 1946, "Naturam primum cognoscere rerum", "admissions@anu.edu.au", "Grade A+", "https://anu.edu.au"),
    ("University of Sydney", "USYD", "Sydney", "Australia", 1850, "Sidere mens eadem mutato", "admissions@sydney.edu.au", "Grade A+", "https://sydney.edu.au"),
    ("Princeton University", "PRINCETON", "Princeton", "United States", 1746, "Dei Sub Numine Viget", "uaoffice@princeton.edu", "Grade A++", "https://princeton.edu"),
    ("Yale University", "YALE", "New Haven", "United States", 1701, "Lux et Veritas (Light and Truth)", "admissions@yale.edu", "Grade A++", "https://yale.edu"),
    ("Columbia University", "COLUMBIA", "New York", "United States", 1754, "In lumine Tuo videbimus lumen", "ugrad-ask@columbia.edu", "Grade A++", "https://columbia.edu"),
    ("University of Chicago", "UCHICAGO", "Chicago", "United States", 1890, "Crescat scientia; vita excolatur", "collegeadmissions@uchicago.edu", "Grade A++", "https://uchicago.edu"),
    ("University of Pennsylvania", "UPENN", "Philadelphia", "United States", 1740, "Leges sine moribus vanae", "admissions@upenn.edu", "Grade A++", "https://upenn.edu"),
    ("Cornell University", "CORNELL", "Ithaca", "United States", 1865, "I would found an institution where any person can find instruction in any study", "admissions@cornell.edu", "Grade A++", "https://cornell.edu"),
    ("Johns Hopkins University", "JHU", "Baltimore", "United States", 1876, "Veritas vos liberabit", "gotojhu@jhu.edu", "Grade A++", "https://jhu.edu"),
    ("University of California, Berkeley", "UCB", "Berkeley", "United States", 1868, "Fiat Lux (Let there be light)", "admissions@berkeley.edu", "Grade A++", "https://berkeley.edu"),
    ("University of California, Los Angeles", "UCLA", "Los Angeles", "United States", 1919, "Fiat Lux", "admissions@ucla.edu", "Grade A++", "https://ucla.edu"),
    ("University of Michigan", "UMICH", "Ann Arbor", "United States", 1817, "Artes, Scientia, Veritas", "admissions@umich.edu", "Grade A++", "https://umich.edu"),
    ("Carnegie Mellon University", "CMU", "Pittsburgh", "United States", 1900, "My heart is in the work", "admission@cmu.edu", "Grade A++", "https://cmu.edu"),
    ("Technical University of Munich", "TUM", "Munich", "Germany", 1868, "The Entrepreneurial University", "studium@tum.de", "Grade A++", "https://tum.de"),
    ("Heidelberg University", "HEIDELBERG", "Heidelberg", "Germany", 1386, "Semper Apertus", "studium@uni-heidelberg.de", "Grade A+", "https://uni-heidelberg.de"),
    ("Paris Sciences et Lettres", "PSL", "Paris", "France", 2010, "Sapere Aude", "admissions@psl.eu", "Grade A++", "https://psl.eu"),
    ("Institut Polytechnique de Paris", "IP-PARIS", "Palaiseau", "France", 2019, "Excellence in Science and Technology", "contact@ip-paris.fr", "Grade A+", "https://ip-paris.fr"),
    ("Karolinska Institute", "KAROLINSKA", "Stockholm", "Sweden", 1810, "Att genom forskning och utbildning förbättra människors hälsa", "info@ki.se", "Grade A++", "https://ki.se"),
    ("Sorbonne University", "SORBONNE", "Paris", "France", 1257, "Créateurs de futurs depuis 1257", "admissions@sorbonne-universite.fr", "Grade A+", "https://sorbonne-universite.fr"),
    ("King's College London", "KCL", "London", "United Kingdom", 1829, "Sancte et Sapienter (With holiness and wisdom)", "admissions@kcl.ac.uk", "Grade A+", "https://kcl.ac.uk"),
    ("University of Edinburgh", "EDINBURGH", "Edinburgh", "United Kingdom", 1583, "Nec tamen consumebatur", "futurestudents@ed.ac.uk", "Grade A++", "https://ed.ac.uk"),
    ("University of Manchester", "MANCHESTER", "Manchester", "United Kingdom", 1824, "Cognitio, sapientia, humanitas", "study@manchester.ac.uk", "Grade A+", "https://manchester.ac.uk"),
    ("Seoul National University", "SNU", "Seoul", "South Korea", 1946, "Veritas lux mea", "snuadmit@snu.ac.kr", "Grade A++", "https://snu.ac.kr"),
    ("Korea Advanced Institute of Science & Technology", "KAIST", "Daejeon", "South Korea", 1971, "Creation, Challenge, Caring", "admission@kaist.ac.kr", "Grade A+", "https://kaist.ac.kr"),
    ("University of Hong Kong", "HKU", "Hong Kong", "Hong Kong", 1911, "Sapientia et Virtus", "admissions@hku.hk", "Grade A++", "https://hku.hk"),
    ("Hong Kong University of Science and Technology", "HKUST", "Hong Kong", "Hong Kong", 1991, "Hands on the present, eyes on the future", "ugadmit@ust.hk", "Grade A+", "https://ust.hk"),
    ("Indian Institute of Technology Bombay", "IIT-BOMBAY", "Mumbai", "India", 1958, "Gyanam Paramam Dhyeyam", "jeeoffice@iitb.ac.in", "Grade A++", "https://iitb.ac.in"),
    ("Indian Institute of Technology Delhi", "IIT-DELHI", "New Delhi", "India", 1961, "Excellence in Technology and Research", "admissions@iitd.ac.in", "Grade A++", "https://iitd.ac.in"),
    ("Indian Institute of Science", "IISC", "Bengaluru", "India", 1909, "Discover and Innovate", "admissions@iisc.ac.in", "Grade A++", "https://iisc.ac.in"),
    ("University of Auckland", "AUCKLAND", "Auckland", "New Zealand", 1883, "Ingenio et labore", "studentinfo@auckland.ac.nz", "Grade A+", "https://auckland.ac.nz"),
    ("Trinity College Dublin", "TCD", "Dublin", "Ireland", 1592, "Perpetuis futuris temporibus duraturam", "academic.registry@tcd.ie", "Grade A+", "https://tcd.ie"),
    ("KU Leuven", "KULEUVEN", "Leuven", "Belgium", 1425, "Sedes Sapientiae", "info@kuleuven.be", "Grade A++", "https://kuleuven.be")
]

target = 'apps/institutions/registries/global_universities.py'

with open(target, 'w', encoding='utf-8') as f:
    f.write('"""\nGlobal Higher Education Institutional Registry\nStandardized records of world-class universities and colleges.\n"""\n\n')
    f.write('GLOBAL_UNIVERSITIES = [\n')
    for name, code, city, country, year, motto, email, grade, web in TOP_UNIVERSITIES_DATA:
        f.write('    {\n')
        f.write(f'        "name": "{name}",\n')
        f.write(f'        "code": "{code}",\n')
        f.write(f'        "city": "{city}",\n')
        f.write(f'        "country": "{country}",\n')
        f.write(f'        "established_year": {year},\n')
        f.write(f'        "motto": "{motto}",\n')
        f.write(f'        "contact_email": "{email}",\n')
        f.write(f'        "accreditation_grade": "{grade}",\n')
        f.write(f'        "website": "{web}",\n')
        f.write('    },\n')
    f.write(']\n\n')
    f.write('UNIVERSITIES_BY_CODE = {u["code"]: u for u in GLOBAL_UNIVERSITIES}\n')

print("global_universities.py successfully written.")
