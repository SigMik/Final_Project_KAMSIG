### Lithuanian basketball LKL and MLKL leagues statistic data analysis 

Project created by: Kamila Kononovič and Sigita Mikolainienė
Project theme: Lithuanian basketball men (LKL) and women (MLKL) leagues statistic data analysis 

Education institution: Vilnius Coding School
Lecturer: Modestas Viršila

The main goal of the project is to collect, process, analyze and visualize the LKL and MLKL statistics using Python 
language and its related libraries.

### Web scraping

This is the summary of steps which were made for the web scraping. The workings for web scraping were performed in the
following files:
[web_scrap_LKL.py](web_scrap_LKL.py)
[web_scrap_MLKL.py](web_scrap_MLKL.py)

Used libraries: BeautifulSoup, requests, pandas

Steps:
1. Finding reliable source of Lithuanian basketball statistics for the web scraping. Men and women basketball leagues 
   data were taken from the following URLs where the official basketball is available:
   * https://lkl.lt/statistika
   * https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html
2. Determining which basketball statistics categories will be analyzed. For our analysis, we have chosen points (PTS), 
   efficiency (EFF) of the basketball players
3. Getting needed data from URLs as table using BeautifulSoup and indicating analysis method (html.parser)
4. Creating 'for' loop in order to scrape the data over each URL page. As a result, the full data available at the
   website was extracted
5. Using DataFrame function to store the collected information and exporting the DataFrame into a csv files

### Statistics and visuals

This is the summary of targets and steps which were done to perform statistic and visual analysis of basketball teams.
The workings of statistic and visuals analysis were perfomed in the file:
[statistics_and_visuals.py](statistics_and_visuals.py)

Used libraries: BeautifulSoup, requests, pandas, numpy, seaborn, matplotlib.pyplot, OffsetImage, AnnotationBbox

Targets:
1. To identify the players with the highest points scoring average per season in LKL and MLKL and to add image of each 
player into the graph. In order to perform the analysis, the following steps were taken:
   * Reading the csv files created earlier with points of basketball teams
   * Calculating the points average result per game in LKL and MLKL
   * Sorting the values by result in the descending order
   * Creating graph using seaborn and matplotlib packages and adding the images of each player

After the performed analysis, we have obtained the graph with below results:

![Highest results players.png](images%2FHighest%20results%20players.png)

2. To identify three players according to the highest efficiency scores in the LKL and MLKL. In order to conduct the 
analysis, the following steps were taken:
   * Reading the csv files created earlier with efficiency results of basketball teams
   * Calculating the efficiency average result per game in LKL and MLKL
   * Creating new DataFrame where the values are sorted by efficiency score in the descending order
   * Creating graphs using seaborn and matplotlib packages

After the performed analysis, we have obtained the graphs with below results:

![LKL teams EFF 2022-2023.png](images%2FLKL%20teams%20EFF%202022-2023.png)
![MLKL teams EFF 2022-2023.png](images%2FMLKL%20teams%20EFF%202022-2023.png)

3. To analyse performance of basketball teams according to the points score in LKL during three last seasons:
2020-2021, 2021-2022 and 2022-2023. In order to conduct the analysis, the following steps were taken:
   * Reading the csv files created earlier with efficiency results of basketball teams
   * Calculating the efficiency average result per game in LKL
   * Creating new DataFrame where the values are sorted by points score in the ascending order
   * Eliminating the irrelevant columns 
   * Creating the barplots using seaborn and matplotlib packages and adding all basketball teams played in the season.

After the performed analysis, we have obtained the graph with below results:

![LKL teams variation 3 seasons.png](images%2FLKL%20teams%20variation%203%20seasons.png)

### Conclusions

After the performed analysis of Lithuanian LKL and MLKL basketball leagues, it is now possible to define the best
players and their teams in LKL and MLKL according to the criterias described above. Therefore, we have achieved the 
following findings:
   * The best players in season 2022-2023 in LKL according to the calculated average points per games was Ahmad Caver 
     from basketball team 'Wolves' with average result per game 17.09, while the best player from MLKL was Tyra Marie 
     Buss with average result per game 10.57
   * The top teams from the total 12 teams played in season 2022-2023 in LKL according to the calculated average 
     efficiency ratio per game was 'Rytas' with efficiency of 157, the second and third place was taken by the teams 
     'Žalgiris' and 'Uniclub Casino - Juventus' with same efficiency of 155. However, the lowest efficiency of 87 was 
     earned by the team 'Gargždai'. 
   * Referring to MLKL, the total number of teams which played in 2022-2023 were 5 teams. The best performance by 
     efficiency was earned by the team 'Vilniaus Kibirkštis' with efficiency of 133, while the second and third place 
     was taken by the 'Klaipėdos Neptūnas' and 'Kauno Aistės LSMU' teams with similar results of 81 and 77 accordingly. 
     The lowest result was made by 'Šiaulių Šiauliai-Vilmers' team with efficiency of 52.
   * Based on the results from analysis performance of basketball teams according to the points score in LKL during 
     three last seasons, it can be noticed that not all the teams were playing in all analyzed periods. ...(to be done)
