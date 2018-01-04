# Aplikacija za spletno trgovino

import modeli # delo z bazo
from bottle import *

# Metode za prikazovanje ustreznih strani:

@get('/')
def prikaziMenuDomov():
    return template('domov2.html')

@get('/static/<filename:path>')
def static(filename):
    return static_file(filename, root='static')

@get('/static/images/<filename:path>')
def static(filename):
    return static_file(filename, root='static/images')

@get('/static/fonts/<filename:path>')
def static(filename):
    return static_file(filename, root='static/fonts')

@get('/aboutme')
def prikaziMenuOpis():
    return template('aboutme.html')

@get('/contact')
def prikaziMenuKontakt():
    return template('contact.html')

@get('/store')
def prikaziMenuTrgovina():
    """ Prikaže slike z naslovi, cenami in košaricami. """
    uporabnik = modeli.Uporabnik.id
    return template('store.html', uporabnik=uporabnik, cena_kosarice=modeli.vrednostKosarice(uporabnik), slike=modeli.slike())

@get('/store/register')
def prikaziMenuRegister():
    return template('register.html')


@get('/basket')
def prikaziKosaricoUporabnika():
    uporabnik = modeli.Uporabnik.id
    podatki = modeli.relevantniPodatkiSlikKosarice(uporabnik)
    return template('basket.html', relevantni_podatki_slik_kosarice=podatki, cena_kosarice=modeli.vrednostKosarice(uporabnik))

@get('/basket/invoice')
def prikaziRacun():
    """ Prikaze racun na podlagi košarice prijavljenega uporabnika. """
    uporabnik = modeli.Uporabnik.id
    podatki = modeli.relevantniPodatkiSlikKosarice(uporabnik)
    return template('invoice.html', relevantni_podatki_slik_kosarice=podatki, cena_kosarice=modeli.vrednostKosarice(uporabnik))


@post('/store/register_submit')
def registracija():
    """ Vzame podatke vnešene v polja za registracijo in jih shrani v bazo. """
    name = request.forms.name
    surname = request.forms.surname
    email = request.forms.email
    password = request.forms.password

    modeli.dodajUporabnika(name, surname, email, password)
    return template('login.html')

@post('/store/add_to_basket<slika_id>')
def dodajVKosarico(slika_id):
    """ Doda sliko v košarico prijavljenega uporabnika """
    modeli.dodajSlikoVKosarico(modeli.Uporabnik.id, slika_id)
    redirect('/store')

@post('/basket/remove_painting<slika_id>')
def odstraniIzKosarice(slika_id):
    """ Doda sliko v košarico prijavljenega uporabnika """
    modeli.odstraniSlikoIzKosarice(modeli.Uporabnik.id, slika_id)
    redirect('/basket')

@get('/store/login')
def prikaziMenuLogin():
    return template('login.html')

@post('/store/login_submit')
def prikaziMenuLogin():
    email = request.forms.email
    password = request.forms.password
    if modeli.prijavaUporabnika(email, password):
        modeli.Uporabnik.id = modeli.uporabnikovId(email)
    redirect('/store') # gremo nazaj na trgovino, da lahko kupujemo - sedaj lahko dodajamo v košarico



run(host='localhost', port=8080)

