### Lithuanian basketball LKL and MLKL leagues statistic data analysis 

Project created by: Kamila Kononovič and Sigita Mikolainienė

Project theme: Lithuanian basketball men (LKL) and women (MLKL) leagues statistics data analysis 

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
   data were taken from the following URLs where the official basketball statistics is available:
   * https://lkl.lt/statistika
   * https://moterulyga.lt/lygos/164-moteru-lkl-a-divizionas/statistika.html
2. Determining which basketball statistics categories will be analyzed. For our analysis, we have chosen points (PTS)
   and efficiency (EFF) of the basketball players
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
1. To identify the best player from LKL and MLKL with the highest average points scored per season and to add image of 
each basketball player into the graph. In order to perform the analysis, the following steps were taken:
   * Reading the csv files created earlier with points of basketball teams
   * Calculating the average points results per game in LKL and MLKL
   * Creating new DataFrame and sorting the values by result in the descending order
   * Creating graph using seaborn and matplotlib packages and adding the images of each player

After the performed analysis, we have obtained the graph with below results:

![Highest results players.png](images%2FHighest%20results%20players.png)

2. To find the best three players with highest efficiency in LKL and MLKL during 2022-2023 season. In order to perform 
the analysis, the following steps were taken:
   * Reading the csv files created earlier with efficiency of LKL and MLKL
   * Calculating the average efficiency results per game in LKL and MLKL
   * Creating new DataFrame and sorting the values by efficiency in the descending order
   * Creating graph using seaborn and matplotlib packages and indicating names and surnames of best three players and 
     their teams

After the performed analysis, we have obtained the graph with below results:

![EFF points by players in LKL and MLKL.png](images%2FEFF%20points%20by%20players%20in%20LKL%20and%20MLKL.png)

3. To identify best teams according to the highest efficiency scores in the LKL and MLKL. In order to conduct the 
analysis, the following steps were taken:
   * Reading the csv files created earlier with efficiency results of basketball teams
   * Calculating the efficiency average result per game in LKL and MLKL
   * Creating new DataFrame where the values are sorted by efficiency score in the descending order
   * Creating graphs using seaborn and matplotlib packages

After the performed analysis, we have obtained the graphs with below results:

![LKL teams EFF 2022-2023.png](images%2FLKL%20teams%20EFF%202022-2023.png)
![MLKL teams EFF 2022-2023.png](images%2FMLKL%20teams%20EFF%202022-2023.png)

4. To analyse performance of basketball teams according to the average points in LKL during three last seasons:
2020-2021, 2021-2022 and 2022-2023. In order to conduct the analysis, the following steps were taken:
   * Reading the csv files created earlier with efficiency results of basketball teams
   * Eliminating the irrelevant columns 
   * Creating new DataFrame where the values are sorted by average points and seasons in the ascending order
   * Creating the barplots using seaborn and matplotlib packages and adding all basketball teams played in the season

After the performed analysis, we have obtained the graph with below results:

![LKL teams variation 3 seasons.png](images%2FLKL%20teams%20variation%203%20seasons.png)

### Conclusions

After the performed analysis of Lithuanian LKL and MLKL basketball leagues, it is now possible to define the best
players and their teams in LKL and MLKL according to the criterias chosen (points and efficiency). Therefore, we have 
achieved the following findings:
   * The best players in season 2022-2023 in LKL according to the calculated average points per games was Ahmad Caver 
     from basketball team 'Wolves' with average result per game 17.09, while the best player from MLKL was Tyra Marie 
     Buss from team 'Kauno Aistės-LSMU' with average result per game 10.57
   * The best three players in season 2022-2023 in LKL according to the calculated average efficiency was Ahmad Caver
     with efficiency of 21, when the second and third places were taken by Jeffery Garrett and Martynas Echodas with
     similar efficiency results of 18. Meanwhile, the best three players from MLKL was Gintarė Petronytė with efficiency
     of 35, and the second and third places were taken by Tyra Marie Buss and Laura Juškaitė with efficiency of 17 and
     16 accordingly.
     from basketball team 'Wolves' with average result per game 17.09, while the best player from MLKL was Tyra Marie 
     Buss from team 'Kauno Aistės-LSMU' with average result per game 10.57
   * The top teams from the total 12 teams played in season 2022-2023 in LKL according to the calculated average 
     efficiency ratio per game was 'Rytas' with efficiency of 157, the second and third places were taken by the teams 
     'Žalgiris' and 'Uniclub Casino - Juventus' with similar efficiency of approx. 155. However, the lowest efficiency 
     of 87 was earned by the team 'Gargždai'. 
   * Referring to MLKL efficiency, the total number of teams which played in 2022-2023 were 5 teams. From the total 
     number of 5 teams, the best performance by efficiency was earned by the team 'Vilniaus Kibirkštis' with efficiency
     of 133, while the second and third places were taken by the 'Klaipėdos Neptūnas' and 'Kauno Aistės-LSMU' teams 
     with similar results of 81 and 77 accordingly. The lowest result was made by 'Šiaulių Šiauliai-Vilmers' team with 
     efficiency of 52.
   * Based on the results from analysis of basketball teams according to the points score in LKL during three last 
     seasons, it can be stated that team 'Nevėžis-Optibet' with each season had the better points score results, as the 
     graph line has the upward tendency to grow. Meanwhile, teams as 'Pieno žvaigždės' and 'Šiauliai' had the stable 
     results during analysed period. However, it can be noticed that not all the teams were playing in all analyzed 
     periods. For example, teams 'Prienų CBet' and 'Lietkabelis' played in 2020-2021 and 2021-2022 seasons, while teams 
     'Uniclub Casino - Juventus' and 'Labas Gas' played in 2021-2022 and 2022-2023 seasons.
