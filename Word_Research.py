# todo: Creare un file con un testo a scelta suddiviso in righe e colonne (vedi ad esempio: https://it.lipsum.com/)
#   •Il file potrebbe essere potenzialmente enorme
#   •Fino a che l'utente non scrive la singola lettera 'q’
#   •Leggere Una Parola Da Input
#   •Se la parola è presente nel file indicare la riga e la Colonna
#   •Altrimentiscrivere'Parolanonpresente’
#   •Suggerimento
#   •Aprire e chiudere il file ad ogni ciclo (non caricare il file in memoria)
#   •Una parola non è spezzabile in due righe

fine = False
try:
    while True:
        with (open("testo.txt", 'r')) as r_testo:
            word = input("Inserire la parola da cercare ==> ").lower()
            if word == 'q':
                fine = True
                break
            # lettura del file riga per riga
            for i, line in enumerate(r_testo):
                # verifica della presenza della parola nella riga corrente
                if line.find(word) != -1:
                    row = i
                    col = line.find(word)
                    found = True
                    break
                else:
                    found = False

            if found == True: print(f"La parola si trova a\n\t\t\t\t\triga: {row}\n\t\t\t\t\tcolonna: {col}")
            else: print("Parola non trovata")
            r_testo.seek(0)

except FileNotFoundError:
    if input(f"File non esistente, crarne uno? y/n") == ('y' or 'si'):
        with(open("testo.txt", 'w')) as w_testo:
            w_testo.write(input("Inserire il testo --> "))
