class Tex:
    def __init__(self, tex_file):
        self.t = tex_file
        self.sections = []

    def load(self):
        s = ''
        with open(self.t, 'r', encoding='utf-8') as f:
            s = f.read()
        lines = [i.strip() for i in s.split('\n')]
        lines = [lines[0]] + [lines[i] for i in range(1, len(lines)) if
                              not (len(lines[i]) == 0 and (lines[i - 1].startswith('\\') or len(lines[i - 1]) == 0))]
        self.s = '\n'.join(lines)

    def save(self, out):
        if not out.endswith('.tex'):
            out += '.tex'
        print(self.s, file=open(out, 'w', encoding='utf-8'))

    def ident(self):
        def identar(lines, n, l2str=False, str=''):
            nl = []
            for i in lines:
                if r'\begin' in i and not r'\end' in i:
                    nl.append('\t' * n + i)
                    n += 1
                elif not r'\begin' in i and r'\end' in i:
                    n -= 1
                    nl.append('\t' * n + i)
                else:
                    nl.append('\t' * n + i)
            if l2str:
                return str + '\n'.join(nl), n
            return nl, n

        # identar secoes
        sections = self.s.replace(r'\section', r'(--++section++--)\section').split(r'(--++section++--)')
        for i in range(1, len(sections)):  # secoes
            lines = sections[i].split('\n')
            sections[i] = '\n\t'.join(lines)
            subsec = sections[i].replace(r'\subsection', r'(--++subsection++--)\subsection').split(
                r'(--++subsection++--)')
            for j in range(1, len(subsec)):  # subssecoes
                lines = subsec[j].split('\n')
                subsec[j] = '\n\t'.join(lines)
                subsub = subsec[j].replace(r'\subsubsection', r'(--++subsubsection++--)\subsubsection').split(
                    r'(--++subsubsection++--)')
                for k in range(1, len(subsub)):  # subsubssecoes
                    lines = subsub[k].split('\n')
                    subsec[k] = '\n\t'.join(lines)
                subsec[j] = ''.join(subsub)
            sections[i] = ''.join(subsec)
        print(''.join(sections))
        id, n = identar(''.join(sections).split('\n'), 0, True, '')
        self.s = id



# identar('inp.tex', 'out.tex')


t = Tex('inp.tex')
t.load()
t.ident()
t.save('out')
