def n_medias(*notas, **kwnotas):
    media = 0
    if notas:
        media = sum(notas)/float(len(notas))
    elif kwnotas:
        media = sum(kwnotas.values())/float(len(kwnotas))
    return media


assert n_medias(10,5,6,8,7) == 7.2
assert n_medias(nota1=10, nota2=5, nota3=6, nota4=8, nota5=7) == 7.2
