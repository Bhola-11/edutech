import os

for root, dirs, files in os.walk('templates'):
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8') as fh:
                c = fh.read()
            if r'\"' in c:
                c = c.replace(r'\"', '"')
                with open(p, 'w', encoding='utf-8') as fh:
                    fh.write(c)
                print('Fixed:', p)
