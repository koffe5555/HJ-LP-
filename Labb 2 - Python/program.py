import module


def menu():
    print("\n 1. Läs in orginalfil \n 2. Visa json-data \n 3. Lägg till person \n 4. Ta bort person \n 5. Spara fil \n 6. Avsluta")
    answer = input()
    while True:
        if answer == '1':
            module.ReadCsv('personer.csv')
            menu()
        elif answer == '2':
            show = module.ReadJson('personer.json')
            print(show)
            menu()
        elif answer == '3':
            module.AddPerson()
            menu()
        elif answer == '4':
            module.RemovePerson()
            menu()
        elif answer == '5':
            print('File Saved!')
            module.ToJson('personer.json', module.dictionary)
            menu()
        else:
            print('Exiting')
        break


menu()
