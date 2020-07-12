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


