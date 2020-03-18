from Sites import *
import pdfquery  # pip install pdfquery


def square(x_botom, y_botom, x_top, y_top, mm=True):
    y_top = 211 - y_top
    y_botom = 211 - y_botom
    if mm:
        x_botom /= 25.4
        y_botom /= 25.4
        x_top /= 25.4
        y_top /= 25.4
    x_botom *= 72
    y_botom *= 72
    x_top *= 72
    y_top *= 72
    # print('%s, %s, %s, %s' % (x_botom, y_botom, x_top, y_top))
    return '%s, %s, %s, %s' % (x_botom, y_botom, x_top, y_top)


profs = Docente.load_list('../out/Docentes/profs.bin')  # le a lista de Docentes
prof = profs[0]



def extract(fileName, table_out):
    outs = [open('../out/' + f + '.md', 'w', encoding='utf-8') for f in table_out]
    for f in outs:
        print('| Nome | total de aulas |', file=f)
        print('| :---- | :---- |', file=f)
    progress = 0
    d_progress = 100 / len(profs)
    for prof in profs:
        for i in range(len(fileName)):
            pdf = None
            try:
                pdf = pdfquery.PDFQuery('../out/Docentes/' + prof.name + fileName[i])
            except FileNotFoundError as e:
                print(f'{prof.name} não possui informaçao de {fileName[i][1:-3]}')
                print(f'| {prof.name} | Nao possui arquivo {fileName[i][1:-3]}|', file=outs[i])
                continue
            pdf.load(0)
            a = pdf.extract([('with_formatter', 'text'), \
                                 ('total de aulas', f':in_bbox("{square(100, 131, 137, 81)}")')])
            print(f'| {prof.name} | {a["total de aulas"][:len(a["total de aulas"]) // 2]} |', file=outs[i])
        progress += d_progress
        print("%.2f %%" % progress)
    for f in outs:
        f.close()


extract(['/2018 - 2.pdf', '/2019 - 1.pdf', '/2019 - 2.pdf'], ['tabela2018', 'tabela20191', 'tabela20192'])
