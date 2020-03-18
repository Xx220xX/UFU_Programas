import Sites

profs = Sites.Docente.load_list('../out/Docentes/profs.bin')  # le a lista de Docentes
table = ''
with open('../out/table.md', 'w', encoding='utf-8')as file:
    print('| Nome | telefone | email |  status | faculdade | lates |', file=file)
    print('| :----: | :----: | :----: | :----: | :----: | :----: |', file=file)
    for prof in profs:
        print(prof.tableMarkdown().replace('None',' - '), file=file)
