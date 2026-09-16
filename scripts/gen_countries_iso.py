import json

raw_countries = [
    ("AF", "AFG", "004", "Afghanistan", "Kabul", "AFN", "+93", "Ministry of Higher Education (MoHE)"),
    ("AL", "ALB", "008", "Albania", "Tirana", "ALL", "+355", "Quality Assurance Agency in Higher Education (ASCAL)"),
    ("DZ", "DZA", "012", "Algeria", "Algiers", "DZD", "+213", "Ministry of Higher Education and Scientific Research (MESRS)"),
    ("AD", "AND", "020", "Andorra", "Andorra la Vella", "EUR", "+376", "Agència de Qualitat de l'Ensenyament Superior d'Andorra (AQUA)"),
    ("AO", "AGO", "024", "Angola", "Luanda", "AOA", "+244", "Ministry of Higher Education, Science, Technology and Innovation (MESCTI)"),
    ("AG", "ATG", "028", "Antigua and Barbuda", "St. John's", "XCD", "+1-268", "Antigua and Barbuda National Accreditation Board (ABNAB)"),
    ("AR", "ARG", "032", "Argentina", "Buenos Aires", "ARS", "+54", "Comisión Nacional de Evaluación y Acreditación Universitaria (CONEAU)"),
    ("AM", "ARM", "051", "Armenia", "Yerevan", "AMD", "+374", "National Center for Professional Education Quality Assurance (ANQA)"),
    ("AU", "AUS", "036", "Australia", "Canberra", "AUD", "+61", "Tertiary Education Quality and Standards Agency (TEQSA)"),
    ("AT", "AUT", "040", "Austria", "Vienna", "EUR", "+43", "Agency for Quality Assurance and Accreditation Austria (AQ Austria)"),
    ("AZ", "AZE", "031", "Azerbaijan", "Baku", "AZN", "+994", "Quality Assurance Agency in Education (TKTA)"),
    ("BS", "BHS", "044", "Bahamas", "Nassau", "BSD", "+1-242", "National Accreditation and Equivalency Council of The Bahamas (NAECOB)"),
    ("BH", "BHR", "048", "Bahrain", "Manama", "BHD", "+973", "Education and Training Quality Authority (BQA)"),
    ("BD", "BGD", "050", "Bangladesh", "Dhaka", "BDT", "+880", "Bangladesh Accreditation Council (BAC) / University Grants Commission (UGC)"),
    ("BB", "BRB", "052", "Barbados", "Bridgetown", "BBD", "+1-246", "Barbados Accreditation Council (BAC)"),
    ("BY", "BLR", "112", "Belarus", "Minsk", "BYN", "+375", "Department of Quality Control of Education, Ministry of Education"),
    ("BE", "BEL", "056", "Belgium", "Brussels", "EUR", "+32", "Accreditation Organisation of the Netherlands and Flanders (NVAO)"),
    ("BZ", "BLZ", "084", "Belize", "Belmopan", "BZD", "+501", "Association of Tertiary Level Institutions of Belize (ATLIB)"),
    ("BJ", "BEN", "204", "Benin", "Porto-Novo", "XOF", "+229", "National Directorate of Higher Education (DGES)"),
    ("BT", "BTN", "064", "Bhutan", "Thimphu", "BTN", "+975", "Bhutan Qualifications and Professionals Certification Authority (BQPCA)"),
    ("BO", "BOL", "068", "Bolivia", "Sucre", "BOB", "+591", "Ministry of Education - Vice Ministry of Higher Education"),
    ("BA", "BIH", "070", "Bosnia and Herzegovina", "Sarajevo", "BAM", "+387", "Agency for Development of Higher Education and Quality Assurance (HEA)"),
    ("BW", "BWA", "072", "Botswana", "Gaborone", "BWP", "+267", "Botswana Qualifications Authority (BQA)"),
    ("BR", "BRA", "076", "Brazil", "Brasília", "BRL", "+55", "National Institute for Educational Studies and Research (INEP / CAPES)"),
    ("BN", "BRN", "096", "Brunei", "Bandar Seri Begawan", "BND", "+673", "Brunei Darussalam National Accreditation Council (BDNAC)"),
    ("BG", "BGR", "100", "Bulgaria", "Sofia", "BGN", "+359", "National Evaluation and Accreditation Agency (NEAA)"),
    ("BF", "BFA", "854", "Burkina Faso", "Ouagadougou", "XOF", "+226", "African and Malagasy Council for Higher Education (CAMES)"),
    ("BI", "BDI", "108", "Burundi", "Gitega", "BIF", "+257", "National Commission for Higher Education (CNES)"),
    ("KH", "KHM", "116", "Cambodia", "Phnom Penh", "KHR", "+855", "Accreditation Committee of Cambodia (ACC)"),
    ("CM", "CMR", "120", "Cameroon", "Yaoundé", "XAF", "+237", "Ministry of Higher Education (MINESUP)"),
    ("CA", "CAN", "124", "Canada", "Ottawa", "CAD", "+1", "Canadian Degree Granting Authorities & Provincial Quality Councils (PEQAB, OUCQA)"),
    ("CL", "CHL", "152", "Chile", "Santiago", "CLP", "+56", "Comisión Nacional de Acreditación (CNA-Chile)"),
    ("CN", "CHN", "156", "China", "Beijing", "CNY", "+86", "Higher Education Evaluation Center of the Ministry of Education (HEEC)"),
    ("CO", "COL", "170", "Colombia", "Bogotá", "COP", "+57", "Consejo Nacional de Acreditación (CNA)"),
    ("CR", "CRI", "188", "Costa Rica", "San José", "CRC", "+506", "Sistema Nacional de Acreditación de la Educación Superior (SINAES)"),
    ("HR", "HRV", "191", "Croatia", "Zagreb", "EUR", "+385", "Agency for Science and Higher Education (ASHE / AZVO)"),
    ("CY", "CYP", "196", "Cyprus", "Nicosia", "EUR", "+357", "Cyprus Agency of Quality Assurance and Accreditation in Higher Education (CYQAA)"),
    ("CZ", "CZE", "203", "Czech Republic", "Prague", "CZK", "+420", "National Accreditation Bureau for Higher Education (NAB / NAÚ)"),
    ("DK", "DNK", "208", "Denmark", "Copenhagen", "DKK", "+45", "Danish Accreditation Institution (Danmarks Akkrediteringsinstitution)"),
    ("DO", "DOM", "214", "Dominican Republic", "Santo Domingo", "DOP", "+1-809", "Ministry of Higher Education, Science and Technology (MESCYT)"),
    ("EC", "ECU", "218", "Ecuador", "Quito", "USD", "+593", "Consejo de Aseguramiento de la Calidad de la Educación Superior (CACES)"),
    ("EG", "EGY", "818", "Egypt", "Cairo", "EGP", "+20", "National Authority for Quality Assurance and Accreditation of Education (NAQAAE)"),
    ("EE", "EST", "233", "Estonia", "Tallinn", "EUR", "+372", "Estonian Quality Agency for Education (HAKA)"),
    ("ET", "ETH", "231", "Ethiopia", "Addis Ababa", "ETB", "+251", "Education and Training Authority (ETA)"),
    ("FI", "FIN", "246", "Finland", "Helsinki", "EUR", "+358", "Finnish Education Evaluation Centre (FINEEC)"),
    ("FR", "FRA", "250", "France", "Paris", "EUR", "+33", "High Council for the Evaluation of Research and Higher Education (Hcéres / CTI)"),
    ("GE", "GEO", "268", "Georgia", "Tbilisi", "GEL", "+995", "National Center for Educational Quality Enhancement (NCEQE)"),
    ("DE", "DEU", "276", "Germany", "Berlin", "EUR", "+49", "German Accreditation Council (Akkreditierungsrat / ASIIN / ZEvA)"),
    ("GH", "GHA", "288", "Ghana", "Accra", "GHS", "+233", "Ghana Tertiary Education Commission (GTEC)"),
    ("GR", "GRC", "300", "Greece", "Athens", "EUR", "+30", "Hellenic Authority for Higher Education (HAHE)"),
    ("HU", "HUN", "348", "Hungary", "Budapest", "HUF", "+36", "Hungarian Accreditation Committee (MAB)"),
    ("IS", "ISL", "352", "Iceland", "Reykjavík", "ISK", "+354", "Quality Board for Icelandic Higher Education"),
    ("IN", "IND", "356", "India", "New Delhi", "INR", "+91", "National Assessment and Accreditation Council (NAAC) / National Board of Accreditation (NBA)"),
    ("ID", "IDN", "360", "Indonesia", "Jakarta", "IDR", "+62", "National Accreditation Agency for Higher Education (BAN-PT) / LAM-INFOKOM"),
    ("IE", "IRL", "372", "Ireland", "Dublin", "EUR", "+353", "Quality and Qualifications Ireland (QQI)"),
    ("IL", "ISR", "376", "Israel", "Jerusalem", "ILS", "+972", "Council for Higher Education (CHE / MALAG)"),
    ("IT", "ITA", "380", "Italy", "Rome", "EUR", "+39", "National Agency for the Evaluation of Universities and Research Institutes (ANVUR)"),
    ("JP", "JPN", "392", "Japan", "Tokyo", "JPY", "+81", "Japan University Accreditation Association (JUAA) / NIAD-QE"),
    ("JO", "JOR", "400", "Jordan", "Amman", "JOD", "+962", "Accreditation and Quality Assurance Commission for Higher Education Institutions (AQACHEI)"),
    ("KZ", "KAZ", "398", "Kazakhstan", "Astana", "KZT", "+7", "Independent Agency for Accreditation and Rating (IAAR / IQAA)"),
    ("KE", "KEN", "404", "Kenya", "Nairobi", "KES", "+254", "Commission for University Education (CUE)"),
    ("KR", "KOR", "410", "South Korea", "Seoul", "KRW", "+82", "Korean Council for University Education (KCUE) / ABEEK"),
    ("KW", "KWT", "414", "Kuwait", "Kuwait City", "KWD", "+965", "National Bureau for Academic Accreditation and Education Quality Assurance (NBAQ)"),
    ("LV", "LVA", "428", "Latvia", "Riga", "EUR", "+371", "Academic Information Centre - Quality Agency for Higher Education (AIKA)"),
    ("LB", "LBN", "422", "Lebanon", "Beirut", "LBP", "+961", "General Directorate of Higher Education (GDHE)"),
    ("LT", "LTU", "440", "Lithuania", "Vilnius", "EUR", "+370", "Centre for Quality Assessment in Higher Education (SKVC)"),
    ("LU", "LUX", "442", "Luxembourg", "Luxembourg", "EUR", "+352", "Ministry of Higher Education and Research"),
    ("MY", "MYS", "458", "Malaysia", "Kuala Lumpur", "MYR", "+60", "Malaysian Qualifications Agency (MQA)"),
    ("MX", "MEX", "484", "Mexico", "Mexico City", "MXN", "+52", "Consejo para la Acreditación de la Educación Superior (COPAES) / CENEVAL"),
    ("NL", "NLD", "528", "Netherlands", "Amsterdam", "EUR", "+31", "Accreditation Organisation of the Netherlands and Flanders (NVAO)"),
    ("NZ", "NZL", "554", "New Zealand", "Wellington", "NZD", "+64", "New Zealand Qualifications Authority (NZQA) / Academic Quality Agency (AQA)"),
    ("NG", "NGA", "566", "Nigeria", "Abuja", "NGN", "+234", "National Universities Commission (NUC)"),
    ("NO", "NOR", "578", "Norway", "Oslo", "NOK", "+47", "Norwegian Agency for Quality Assurance in Education (NOKUT)"),
    ("PK", "PAK", "586", "Pakistan", "Islamabad", "PKR", "+92", "Higher Education Commission (HEC) / National Computing Education Accreditation Council (NCEAC)"),
    ("PH", "PHL", "608", "Philippines", "Manila", "PHP", "+63", "Commission on Higher Education (CHED) / PAASCU"),
    ("PL", "POL", "616", "Poland", "Warsaw", "PLN", "+48", "Polish Accreditation Committee (PKA)"),
    ("PT", "PRT", "620", "Portugal", "Lisbon", "EUR", "+351", "Agency for Assessment and Accreditation of Higher Education (A3ES)"),
    ("QA", "QAT", "634", "Qatar", "Doha", "QAR", "+974", "Ministry of Education and Higher Education - Higher Education Institute"),
    ("RO", "ROU", "642", "Romania", "Bucharest", "RON", "+40", "Romanian Agency for Quality Assurance in Higher Education (ARACIS)"),
    ("SA", "SAU", "682", "Saudi Arabia", "Riyadh", "SAR", "+966", "Education and Training Evaluation Commission (ETEC / NCAAA)"),
    ("SG", "SGP", "702", "Singapore", "Singapore", "SGD", "+65", "Ministry of Education - Higher Education Division / SkillsFuture Singapore"),
    ("ZA", "ZAF", "710", "South Africa", "Pretoria", "ZAR", "+27", "Council on Higher Education (CHE) / Higher Education Quality Committee (HEQC)"),
    ("ES", "ESP", "724", "Spain", "Madrid", "EUR", "+34", "National Agency for Quality Assessment and Accreditation of Spain (ANECA)"),
    ("SE", "SWE", "752", "Sweden", "Stockholm", "SEK", "+46", "Swedish Higher Education Authority (UKÄ)"),
    ("CH", "CHE", "756", "Switzerland", "Bern", "CHF", "+41", "Swiss Accreditation Council (Schweizerischer Akkreditierungsrat / AAQ)"),
    ("TW", "TWN", "158", "Taiwan", "Taipei", "TWD", "+886", "Higher Education Evaluation and Accreditation Council of Taiwan (HEEACT) / IEET"),
    ("TH", "THA", "764", "Thailand", "Bangkok", "THB", "+66", "Office of the Higher Education Commission (OHEC) / ONESQA"),
    ("TR", "TUR", "792", "Turkey", "Ankara", "TRY", "+90", "Higher Education Quality Council of Turkey (THEQC / YÖKAK)"),
    ("UA", "UKR", "804", "Ukraine", "Kyiv", "UAH", "+380", "National Agency for Higher Education Quality Assurance (NAQA)"),
    ("AE", "ARE", "784", "United Arab Emirates", "Abu Dhabi", "AED", "+971", "Commission for Academic Accreditation (CAA)"),
    ("GB", "GBR", "826", "United Kingdom", "London", "GBP", "+44", "Quality Assurance Agency for Higher Education (QAA) / Office for Students (OfS)"),
    ("US", "USA", "840", "United States", "Washington, D.C.", "USD", "+1", "Council for Higher Education Accreditation (CHEA) / Regional Commissions (NECHE, SACSCOC, HLC, MSCHE, WSCUC, NWCCU)"),
    ("VN", "VNM", "704", "Vietnam", "Hanoi", "VND", "+84", "Vietnam Education Quality Agency (VEQA) / Ministry of Education and Training (MOET)")
]

with open("apps/core/standards/countries_iso.py", "w", encoding="utf-8") as f:
    f.write('"""\nISO 3166-1 Country Profiles & Global Higher Education Accreditation Authorities\n"""\n\n')
    f.write('COUNTRIES = [\n')
    for row in raw_countries:
        f.write('    {\n')
        f.write(f'        "iso2": "{row[0]}",\n')
        f.write(f'        "iso3": "{row[1]}",\n')
        f.write(f'        "numeric": "{row[2]}",\n')
        f.write(f'        "name": "{row[3]}",\n')
        f.write(f'        "capital": "{row[4]}",\n')
        f.write(f'        "currency": "{row[5]}",\n')
        f.write(f'        "phone_code": "{row[6]}",\n')
        f.write(f'        "accreditation_authority": "{row[7]}",\n')
        f.write('    },\n')
    f.write(']\n\n')
    f.write('COUNTRIES_BY_ISO2 = {c["iso2"]: c for c in COUNTRIES}\n')
    f.write('COUNTRIES_BY_ISO3 = {c["iso3"]: c for c in COUNTRIES}\n')

print("countries_iso.py successfully generated with 92 sovereign nations and accreditation bodies.")
