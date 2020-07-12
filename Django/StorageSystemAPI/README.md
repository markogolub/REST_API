# Sustav za pohranu osobnih podataka

## Cilj zadatka

"Implementirati sustav za pohranu osobnih podataka koji preko API sučelja pruža mogućnost pregleda, unosa, izmjene i brisanja osoba u sustav.

 U skladu s trenutnom situacijom, sustav treba podržavati informaciju o prebivalištu, te imati podršku za trenutnu lokaciju, kao i povijest svih lokacija na kojima se osoba nalazila."


## Korištene tehnologije i alati

Programi su pisani koristeći Python verzije 3.6.7. i HTML5 na operacijskom sustavu Ubuntu 16.04. Korištena je razvojna okolina PyCharm verzije 2019.2.4. za razvoj koda, a za slanje zahtjeva korišten je i preporuča se Postman for Linux verzije 6.7.6. Svi ostali alati navedeni su u [requirements.txt](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/src/requirements.txt).

## Upute za korištenje

### Preuzimanje

Nakon pozicioniranja u direktorij gdje će projekt biti pohranjen, potrebno je izvršiti sljedeću naredbu:

*git clone https://github.com/markogolub/REST_API.git*

i pozicionirati se u sljedeće direktorije: *REST_API/Django/StorageSystemAPI/src*. Izvođenjem naredbe

*pip install -r requirements.txt*

provodi se instalacija svih potrebnih alata i paketa iz requirements.txt. 

### Pokretanje

Pokretanje servera moguće je iz ljuske pozicionirane u direktorij *src* naredbom:

*python manage.py runserver*

### Opis

U nastavku su navedene osnovne operacije, njihovo pokretanje i očekivani rezultati.
Pregled svih podataka moguć je prijavom administratora na [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). 

#### Registracija 

URL: http://127.0.0.1:8000/osobe/register

U navedenoj poveznici "127.0.0.1:8000" predstavlja korisnikovu domenu. U Postmanu je potrebno odabrati opciju "POST" te u stupcu "Body" odabrati opciju "form-data". U stupcu "KEY" potrebno je navesti sve podatke potrebne za registraciju novog korisnika, odnosno imati atribute: email, username, password, password2, name, surname, phone, cell_phone, address, residence.

Atribut *password2* predstavlja ponovni unos lozinke, a obavezna polja su polja *email*, *username* i *cell_phone*. Potrebno je paziti na pravilan format podataka unesenih za polja *phone* i *cell_phone* zbog korištenja klase [PhoneNumberField](https://pypi.org/project/django-phonenumber-field/), odnosno potrebno je unijeti kod države. Konkretno, "+385" prefiks za brojeve iz Hrvatske.
U slučaju unosa već postojeće email adrese, korisničkog imena ili broja mobitela očekivani rezultat prikazan je u [register_existing_data.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/register_existing_data.json) te je vraćen statusni kod *HTTPS_400_BAD_REQUEST*. Primjer očekivanog rezultata za ispravnu registraciju prikazan je u [register.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/register.json).

#### Dohvat liste osoba

URL: http://127.0.0.1:8000/osobe/

Dohvat liste osoba omogućen je jedino administratoru (superuseru). U Postmanu je potrebno odabrati opciju "GET" te u stupcu "Headers" kao *KEY* dodati "Authorization", a kao *VALUE* "Token $admin_token$". Konkretno, token "f699cec5f3e0f930aa677a03e0e0a3ca006974f4". Prikaz očekivanog rezultata za ispravan zahtjev prikazan je u [osobe.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/osobe.json). U slučaju pokušaja dohvata liste osoba s drugim tokenom očekivani rezultat prikazan je u [token_wrong.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/token_wrong.json), odnosno u slučaju pokušaja dohvata s nepostojećim tokenom [token_fail.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/token_fail.json).

#### Dohvat pojedinačne osobe

URL: http://127.0.0.1:8000/osobe/$pk$

Dohvate informacija o svakoj pojedinačnoj osobi omogućen je administratoru, a također omogućen je i dohvat svojih vlastitih informacija za svaku osobu. "$pk$" označa jedinstven *primary_key* koji posjeduje svaka osoba. U Postmanu je potrebno odabrati opciju "GET" te u stupcu "Headers" kao *KEY* dodati "Authorization", a kao *VALUE* "Token $token$" gdje je "$token$" vlastiti token osobe čije informacije želimo vidjeti (ili $admin_token$ kojim je moguće pregledati informacije svih osoba). Očekivani rezultat za zahtjev "http://127.0.0.1:8000/osobe/3" uz token "ea590815d41bc8378d86dcec1b429795ecef45be" prikazan je u [osobe_3.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/osobe_3.json), dok je očekivani rezultat za zahtjev "http://127.0.0.1:8000/osobe/4" [token_wrong.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/token_wrong.json). U slučaju slanja zahtjeva za nepostojećim "$pk$" očekivani rezultat je statusni kod *HTTPS_404_NOT_FOUND*. 

#### Prijava

URL: http://127.0.0.1:8000/osobe/login

Prijava je omogućena samo registriranim osobama. Ukoliko registrirana osoba nema token on će biti stvoren. U Postmanu je potrebno postaviti "POST" zahtjev te u stupcu Body odabrati "form-data". Iako se prijava obavlja koristeći *email*, zbog Django defualt zahtjeva kao prvi atribut stupca *KEY* potrebno je navesti "username". Drugi je atribut "password" te konkretno za "pero.peric@example.com" i "sifra4" očekivani rezultat je [login.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/login.json), a u slučaju pogrešnog unosa podataka očekivani je rezultat [login_fail.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/login_fail.json).

#### Izmjena podataka osobe

URL: http://127.0.0.1:8000/osobe/update/$pk$

Izmjena podataka svake pojedinačne osobe omogućena je administratoru, a također omogućena je i izmjena svojih vlastitih informacija za svaku osobu. U Postmanu je potrebno postaviti "PUT" zahtjev te u stupcu Body odabrati "form-data". Kao atribute stupca *KEY* potrebno je navesti sve atribute koje korisnik želi zamijeniti (nije potrebno unositi i one atribute koje korisnik ne mijenja), a kao *VALUE* novu vrijednost. Osim toga, u stupcu "Header" potrebno je kao *KEY* navesti "Authorization", a kao *VALUE* "Token $token$". Konkretno, za izmjenu imena osobe Marko Marić u Mihael Marić potrebno je unijeti token "0a1c46d07ba85c2de06f35415f1cf7e7d21ffca6" (ili token administratora: "f699cec5f3e0f930aa677a03e0e0a3ca006974f4") te u stupcu name unijeti vrijednost "Mihael". U slučaju ispravnog zahtjeva, očekivani rezultat je [update.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/update.json). U slučaju pokušaja izmjene podataka računa koji ne pripada osobi koja izvodi zahjev očekivani rezultat je [update_fail.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/update_fail.json), a u slučaju pokušaja izmjene podataka nepostojeće osobe očekivani rezultat je statusni kod *HTTPS_404_NOT_FOUND*.

#### Brisanje osobe

URL: http://127.0.0.1:8000/osobe/delete/$pk$

Brisanje svake pojedinačne osobe omogućeno je administratoru, a također omogućeno je i brisanje vlastitog računa za svaku osobu. U Postmanu je potrebno odabrati opciju "DELETE" te u stupcu "Header" za vrijednosti *KEY* i *VALUE* unijeti "Authorization" odnosno "Token $ispravan_token$". Očekivani rezultat ispravnog zahtjeva je [delete.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/delete.json), dok je očekivani rezultat neispravnog rezultata brisanja postojeće osobe [delete_fail.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/delete_fail.json), a nepostojeće osobe statusni kod *HTTPS_404_NOT_FOUND*.

#### Stvaranje lokacije 

URL: http://127.0.0.1:8000/osobe/location/create/$pk$

Stvaranje nove lokacije omogućeno je svakoj osobi. U Postmanu je potrebno odabrati "POST", u stupcu "Headers" kao vrijednost *KEY* i *VALUE* unijeti "Authorization" i "Token $ispravan_token$". U stupcu "Body" nakon odabira opcije "form-data" kao vrijednosti stupca *KEY* potrebno je unijeti "latitude" i "longitude" te im pridružiti vrijednosti koje predstavljaju koordinate. Primjer očekivanog rezultata ispravnog zahtjeva prikazan je u [location.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/location.json), a primjer očekivanog rezultata neispravnog zahtjeva je statusni kod *HTTPS_400_BAD_REQUEST* odnosno [token_wrong.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/token_wrong.json) u slučaju korištenja pogrešnog tokena.

#### Prikaz svih lokacija

URL: http://127.0.0.1:8000/osobe/locations/$pk$

Prikaz svih prijašnjih lokacija svih osoba omogućen je administratoru te pojedinačno vlastita povijest lokacija za svaku osobu. Za svaku osobu potrebno je posebno unositi njen *$pk$*. U Postmanu je potrebno izabrati "GET" te unijeti ispravan token. Očekivan rezultat za ispravan token "ea590815d41bc8378d86dcec1b429795ecef45be" i *$pk$* odnosno "http://127.0.0.1:8000/osobe/locations/3" prikazan je u [locations.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/locations.json), a primjer očekivanog rezultata neispravnog zahtjeva je statusni kod *HTTPS_404_NOT_FOUND* odnosno [token_wrong.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/token_wrong.json) u slučaju korištenja pogrešnog tokena.

#### Bonus: pretraga po lokaciji

URL: http://127.0.0.1:8000/osobe/location/search

Pretragu po lokaciji moguće je obaviti dodavanjem "?search=$traženi_pojam$". Konkretno, s tokenom administratora "f699cec5f3e0f930aa677a03e0e0a3ca006974f4" očekivani rezultat zahtjeva "http://127.0.0.1:8000/osobe/location/search?search=Zagreb" prikazan je u [search.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/search.json). Rezultat pretrage je lista svih osoba čija adresa sadrži traženi pojam "Zagreb". 

Dodatno svojstvo je mogućnost sortiranja dodavanje "&ordering=$uvjet$". Konkretno očekivani rezultat zahtjeva "http://127.0.0.1:8000/osobe/location/search?search=zagreb&ordering=-date_joined" prikazan je u [ordering.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/ordering.json). Sada je rezultat pretrag sortiran tako da su osobe stovrene kasnije na vrhu liste. 

#### Zaboravljena lozinka

URL: http://127.0.0.1:8000/password_reset/

U slučaju zaboravljene lozinke, moguće je postaviti novu. Otvaranjem [http://127.0.0.1:8000/password_reset/](http://127.0.0.1:8000/password_reset/) u web pregledniku, ili navigiranjem na "Login" pa "Forgot password?" na [http://127.0.0.1:8000/](http://127.0.0.1:8000/) za unesenu email adresu u ljusci se ispisuje poveznica pomoću koje je moguće promijeniti lozinku. 

