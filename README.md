# Webservice

## Transforming html to json files

- This webservice runs by python, therefor you have to [install python and the needed packages](https://docs.anaconda.com/free/anaconda/install/index.html)

- after successfull instalation the bash terminal should have a basis in fromt of the $

```bash
(basis)$
```  

- to use the webservice it is recommended to use a [conda virtuel environment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)
  
- therefore open a bash terminal

```bash
(basis)$conda create -n yourenvname
```

-activate the virtuel environment via

```bash
(basis)$conda activate yourenvname
```

- your bash terminal now changed the basis to your virtual environment name

```bash
(yourenvname)$conda 
```

- you are now able to install all import packages such as aiohttp

- Note: [if you have installation problems try](https://anaconda.org/main/aiohttp)

```bash
(yourenvname)$conda install -c main aiohttp
```

- change directory in which the **webservice.py** script is located (try something like this)

```bash
(yourenvname)$ cd ~/Webservice/webservice
```

- now start the script via

```bash
(yourenvname)$ ./webservice.py
```

- Note: onlys files in the static folder and below can be converted and json files will be written into the webservice directory
- therefore generate an html soruce folder and json folder to not fill up webservice folder
- If every thinks workded now the bash terminal should lool like this

```bash
(yourenvname) Username@Domain:~$ ======== Running on http://0.0.0.0:8080 ========
```

- open a webbrowser
- in the adress bar typ in **http://localhost:8080/**  or  directly **http://localhost:8080/Probanden/VerFlu_TI**
- proof if dataset is complete (most important birth date and check boxes ans also if experiment and type seeting is correct, example sub-01 but not sub01 )
- press "Senden der Unterlagen"
- json file will be saved at
- copy json file in the suitable experimantal folder
