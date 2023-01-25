# todo:
#   Esercizio 1:
#   Usando Python:
#   •Scrivere su un file 'proverbio.txt' un proverbio a scelta
#   •Aprire il file proverbio.txt
#   •Leggerne tutto il contenuto
#   •Scrivere i caratteri in posizione pari su un file 'file_proverbio_dispari.txt '
#   •Scrivere i caratteri in posizione dispari su un file ‘file_proverbio_dispari.txt’
#   Suggerimento: questa volta leggeteTUTTO il file e poi...

with (open("Proverbio.txt", 'w')) as w_file:
    w_file.write(input("Inserire un proverbio: --> "))

with (open("Proverbio.txt", 'r')) as r_file,\
     (open("file_proverbio_dispari.txt", 'w')) as d_file,\
     (open("file_proverbio_pari.txt", 'w')) as p_file:
    for i, char in enumerate(r_file.read()):
        if i%2:
            p_file.write(char)
        else:
            d_file.write(char)
