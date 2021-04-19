import sqlite3
conn = sqlite3.connect('passbase.db')
c = conn.cursor()
#INIZIO CODING
c.execute("""CREATE TABLE IF NOT EXISTS pwbase (
    sito text,
    username text,
    email,
    passwd
)""")


print("1. salva una nuova password \n2. vedi le tue password salvate \n3. esci")

baseput = input("Scegli un opzione: ")

if baseput == "1":
    k_sito = input("Inserisci il sito: ")
    k_username = input("Inserisci il nome utente: (facoltatvo) ")
    k_email = input("Inserisci l'email: ")
    k_passwd = input("Inserisci la password: ")
    insertValue = """INSERT INTO pwbase
        (sito, username, email, passwd)
        VALUES ('{}','{}','{}','{}');""".format(
            k_sito, k_username, k_email, k_passwd)
    c.execute(insertValue)
    conn.commit()
    baseput2 = input("Password salvata con successo, Premi invio per chiudere, o premi 2 per vedere la lista delle password salvate.")
    if baseput2 == "2":
        c.execute("SELECT * FROM pwbase")
        items = c.fetchall()
        for item in items:
            print("---------\n" + "Sito: " + item[0] + " \n" + "Username: " + item[1] + " \n" + "Email: " + item[2] + " \n" + "Password: " + item[3])
        input("Premi invio per chiudere.")
elif baseput == '2':
    c.execute("SELECT * FROM pwbase")
    items = c.fetchall()
    for item in items:
        print("---------\n" + "Sito: " + item[0] + " \n" + "Username: " + item[1] + " \n" + "Email: " + item[2] + " \n" + "Password: " + item[3])
    input("Premi invio per chiudere.")
elif baseput == '3':
    exit()







#FINE CODING
conn.close()