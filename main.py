def terulet_sikidomok():
    adott_input = input('Írj egy "N"-t a négyzetért, "T"-t a téglalapért. Írj egy "0"-t, ha ki szeretnél lépni a programból: ').capitalize()
    terulet: int = 0
    if adott_input == "N":
        negyzet_oldala = int(input('Add meg a négyzet oldalát cm-ben: '))
        terulet = negyzet_oldala * negyzet_oldala
        print(f'A négyzet területe: {terulet}cm2')
    elif adott_input == "T":
        elso_oldal = int(input('Add meg a téglalap első oldalát cm-ben: '))
        masodik_oldal = int(input('Add meg a téglalap második oldalát cm-ben: '))
        terulet = elso_oldal * masodik_oldal
        print(f'A téglalap területe: {terulet}cm2')
    elif adott_input == "0":
        print('Program leállítása...')
        quit()
    else:
        print('Az általad megadott opció nem létezik!')


def main() -> None:
    print('=====================')
    print('Síkidomok területének kiszámolása: ')
    print('')
    terulet_sikidomok()

    while True:
        print('=====================')
        valasztas = int(input('A program újboli lefuttatásához írj egy "1"-est: '))
        if valasztas == 1:
            terulet_sikidomok()
        else:
            print("Program leállítása...")
            quit()


if __name__ == "__main__":
    main()
