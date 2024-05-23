import sqlite3

connection = sqlite3.connect("Filmler.db")


cursor = connection.cursor()


def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS FILMLER (Ad TEXT, Yer TEXT, Ratinq INT)")
    connection.commit()

def add_data():
    cursor.execute("INSERT INTO FILMLER VALUES ('Titanik', 'Atlantik Okean', 10)")
    connection.commit()

def dynamic_add_data(Ad, Yer, Ratinq):
    cursor.execute("INSERT INTO FILMLER VALUES (?, ?, ?)", (Ad, Yer, Ratinq))
    connection.commit()


def update_yer(old_yer, new_yer):
    cursor.execute("UPDATE FILMLER SET Yer = ? WHERE Yer = ?", (new_yer, old_yer))
    connection.commit()


def delete_yer(Yer):
    cursor.execute("DELETE FROM FILMLER WHERE Yer = ?", (Yer,))
    connection.commit()


def list_all_films():
    cursor.execute("SELECT * FROM FILMLER")
    films = cursor.fetchall()
    for film in films:
        print(f"Ad: {film[0]}, Yer: {film[1]}, Ratinq: {film[2]}")


def search_film_by_name(film_name):
    cursor.execute("SELECT * FROM FILMLER WHERE Ad = ?", (film_name,))
    films = cursor.fetchall()
    if films:
        for film in films:
            print(f"Ad: {film[0]}, Yer: {film[1]}, Ratinq: {film[2]}")
    else:
        print("Film tapilmadi.")


def update_rating(film_name, new_rating):
    cursor.execute("UPDATE FILMLER SET Ratinq = ? WHERE Ad = ?", (new_rating, film_name))
    connection.commit()


create_table()


add_data()


Ad = input("Filmin adini daxil edin: ")
Yer = input("Filmin yerini daxil edin: ")
Ratinq = int(input("Filmin ratinqin daxil edin: "))


dynamic_add_data(Ad, Yer, Ratinq)


update_yer("Atlantik Okean", "Atlantik Okean Buz")


delete_yer("Atlantik Okean Buz")


print("Mevcut filmler:")
list_all_films()


film_name = input("Axtarmaq istediğiniz filmin adını girin: ")
search_film_by_name(film_name)


film_name = input("Derecesin deyismek istediyiniz filmin adin girin: ")
new_rating = int(input("Yeni derecelendirmeyi girin: "))
update_rating(film_name, new_rating)


connection.close()
