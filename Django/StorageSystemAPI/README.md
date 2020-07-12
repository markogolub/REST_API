# Sustav za pohranu osobnih podataka

## Cilj zadatka

"Implementirati sustav za pohranu osobnih podataka koji preko API sučelja pruža mogućnost pregleda, unosa, izmjene i brisanja osoba u sustav.

 U skladu s trenutnom situacijom, sustav treba podržavati informaciju o prebivalištu, te imati podršku za trenutnu lokaciju, kao i povijest svih lokacija na kojima se osoba nalazila."


## Korištene tehnologije i alati

Programi su pisani koristeći Python verzije 3.6.7. i HTML5 na operacijskom sustavu Ubuntu 16.04. Korištena je razvojna okolina PyCharm verzije 2019.2.4. za razvoj koda, a za slanje zahtjeva korišten je i preporuča se Postman for Linux verzije 6.7.6. Svi ostali alati navedeni su u [requirements.txt](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/src/requirements.txt).

## Upute za korištenje

### Preuzimanje

Nakon pozicioniranja u direktorij gdje će projekt biti pohranjen, potrebno je izvršiti sljedeću naredbu:

*git clone https://github.com/markogolub/REST_API/tree/master/Django/StorageSystemAPI*

i pozicionirati se u direktorij src. Izvođenjem naredbe

*pip install -r requirements.txt*

provodi se instalacija svih potrebnih alata i paketa iz requirements.txt. 

### Pokretanje

Pokretanje servera moguće je iz ljuske pozicionirane u direktorij src naredbom:
python manage.py runserver

### Opis

U nastavku su navedene osnovne operacije, njihovo pokretanje i očekivani rezultati.

#### Registracija 

URL: https:/127.0.0.1:8000/osobe/register

U navedenoj poveznici "127.0.0.1:8000" predstavlja korisnikovu domenu. U postmanu je potrebno odabrati opciju "POST" te u stupcu "Body" odabrati opciju "form-data". U stupcu "KEY" potrebno je navesti sve podatke potrebne za registraciju novog korisnika, odnosno imati atribute: email, username, password, password2, name, surname, phone, cell_phone, address, residence.

Atribut *password2* predstavlja ponovni unos lozinke, a obavezna polja su polja *email*, *username* i *cell_phone*. Potrebno je paziti na pravilan format podataka unesenih za polja *phone* i *cell_phone* zbog korištenja klase [PhoneNumberField](https://pypi.org/project/django-phonenumber-field/), odnosno potrebno je unijeti kod države. Konkretno, "+385" prefiks za brojeve iz Hrvatske.
U slučaju unosa već postojeće email adrese, korisničkog imena ili broja mobitela očekivani rezultat prikazan je u [register_existing_data.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/register_existing_data.json) te je vraćen statusni kod *HTTPS_400_BAD_REQUEST*. Primjer očekivanog rezultata za ispravnu registraciju prikazan je u [register.json](https://github.com/markogolub/REST_API/blob/master/Django/StorageSystemAPI/expected_results/register.json).



