### Lithuanian basketball LKL and MLKL leagues statistic analysis 

Projektą kūrė: Kamila Kononovič ir Sigita Mikolainienė
Projekto tema: Krepšinio statistinė analizė Lietuvos vyrų ir moterų krepšinio lygoje

Mokykla: Vilnius Coding school
Lektorius: Modestas Viršila


Projekto tikslas: surinkti, apdoroti, išanalizuoti ir vizualizuoti krepšinio paskutinio sezono 2022 -2023 LKL ir MLKL
statistiką naudojant Python ir susijusias bibliotekas. Išanalizuoti papildomų dviejų sezonų 2021-2022, 2020-2021 LKL ir
MLK  statistiką ir vizualizuoti pagal pasirinktus kriterijus.

Projekte buvo naudojama Python kalba, python bibliotekos, csv failai, vizualai.

### Web scraping

[web_scrap_LKL.py](web_scrap_LKL.py)
[web_scrap_MLKL.py](web_scrap_MLKL.py)

Used imports:....

Steps:
1. Finding necesary LKL and MLKL data from url [(https://lkl.lt/statistika)] and [(....)]
2. Getting needed data from url as table using Beautiful soup and  indicate analysis method (html.parser)
3. Using for loop received data and saved to csv files

### Statistics and visuals

[statistics_and_visuals.py](statistics_and_visuals.py)

Used imports:...
Steps:
1.  ...
2.  ...

### Conclusions....



Su BeautifulSoup buvo paimti duomenys iš svetainės  


Projekto užduotys (pildysis projekto eigoje):
    ⁙ surinkti duomenis iš pasirinktų dviejų url
    ⁙ sudėti juos į lentelė ir apdoroti reikšmes, kurias naudosime analizei
    ⁙ atlikti LKL ir MLKL  statistinę analizę:
        ⁘ geriausią taškų vidurkį per rungtynes turintis žaidėjas LKL ir MLKL
        ⁘ penki žaidėjai pagal didžiausius efektyvumo balus LKL ir MLKL 
        ⁘ komandų pasiskirstymas pagal efektyvumo balą LKL ir MLKL     
        ⁘ taškų santykis su klaidomis LKL 5 žaidėjų ir MLKL 5 žaidėjų (nezinau)
        ⁘ tritaškių pataikymo procentas LKL ir MLKL (reikia padaryti)
        ⁘ geriausią taškų vidurkį pagal komandas ir sezonus  arba komandos 
pokytis per tris sezonus (reikia padaryti)

    ⁙ vizualizuoti duomenis pagal atliktą analizę
    ⁙ naudojant biblioteką leidžiančia prognozuoti rezultatus, pabandyti numatyti šio sezono LKL laimėtojus  

PAVYZDYS

![Highest results players.png](images%2FHighest%20results%20players.png)
