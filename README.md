Make sure you have Django and Python installed before trying to run our web application.
Once installed, clone this repository, open Terminal and navigate to the directory. To run the server locally, type the following command in the command line while inside the projectEnergy directory.
```
python3 manage.py runserver
```
Check out the website at the dedicated ```localhost``` address. For administrative use, add "/admin" to the URL and login with
username: projectEnergy
password: projectEnergy

You can play around with the data models we have, you can add some instances. Enjoy!

The datasets are already loaded in the data folder, but to generate them:
- Open Rstudio, which you can get through Duke OIT VM Manage
- upload CS316_makeSchema.R, access-electricity.csv, and Power_Database.csv from Milestone2 in the same directory in Rstudio
- run CS316_makeSchema.R
- download Members.csv, Sellers.csv, Countries.csv from Rstudio into the data folder.

Note: if having problems after pulling current repository from GitHub, run the following two commands to synchronize the database:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
