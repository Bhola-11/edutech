import os
import sys

EXTENSIONS = {
    '.py': 'Python',
    '.html': 'HTML Templates',
    '.js': 'JavaScript',
    '.css': 'CSS Styles',
    '.json': 'JSON Fixtures/Schemas',
    '.md': 'Documentation',
    '.sql': 'SQL Schemas/Seeds',
}

EXCLUDE_DIRS = {
    '.git', '__pycache__', 'venv', 'env', '.venv', 'staticfiles', 
    'media', 'node_modules', '.pytest_cache', 'htmlcov'
}

def is_comment(line, ext):
    line = line.strip()
    if not line:
        return True
    if ext == '.py' and (line.startswith('#') or line.startswith('"""') or line.startswith("'''")):
        return True
    if ext in ['.js', '.css'] and (line.startswith('//') or line.startswith('/*') or line.startswith('*')):
        return True
    if ext == '.html' and (line.startswith('<!--') or line.startswith('{#')):
        return True
    return False

def count_project_loc(root_dir):
    stats = {lang: {'files': 0, 'total_lines': 0, 'code_lines': 0} for lang in set(EXTENSIONS.values())}
    detailed_files = []

    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in EXTENSIONS:
                lang = EXTENSIONS[ext]
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                    total = len(lines)
                    code = sum(1 for line in lines if not is_comment(line, ext))
                    stats[lang]['files'] += 1
                    stats[lang]['total_lines'] += total
                    stats[lang]['code_lines'] += code
                    detailed_files.append((filepath, lang, total, code))
                except Exception as e:
                    pass

    total_files = sum(s['files'] for s in stats.values())
    total_lines = sum(s['total_lines'] for s in stats.values())
    total_code = sum(s['code_lines'] for s in stats.values())

    print('=' * 75)
    print(f'{"LANGUAGE":<20} | {"FILES":<8} | {"TOTAL LINES":<15} | {"GENUINE CODE LOC":<15}')
    print('-' * 75)
    for lang, data in sorted(stats.items(), key=lambda x: x[1]['code_lines'], reverse=True):
        if data['files'] > 0:
            print(f'{lang:<20} | {data["files"]:<8} | {data["total_lines"]:<15} | {data["code_lines"]:<15}')
    print('=' * 75)
    print(f'{"TOTAL":<20} | {total_files:<8} | {total_lines:<15} | {total_code:<15}')
    print('=' * 75)
    return total_code

if __name__ == '__main__':
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    count_project_loc(root)
