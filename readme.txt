Run setup.py
You will get a link on terminal as "Running on " where the application is running.
Now it will run on localhost or 127.0.0.1:port_number you have mentioned while making configuration
After Successfully Running the Application it will run on the default browser or manually selected browser.
127.0.0.1:your_port_number/api/v1 -> it is a endpoint which is the homepage of the website.
127.0.0.1:your_port_number/api/v1/banks -> it is an endpoint which will give you the bank list.
127.0.0.1:your_port_number/api/v1/banks/id -> it is an endpoint which will give you the all branch details of the particular bank id which you get from the bank list.
e.g. ABHYUDAYA BANK COOPERATIVE LIMITED:60
so id will be 60 it is present in the database 
127.0.0.1:your_port_number/api/v1/banks/60
127.0.0.1:your_port_number/api/v1/banks/id/branch -> it is an endpoint which will give you the specific/ particular details of the branch.
e.g. suppose ABHYUDAYA BANK COOPERATIVE LIMITED has Branch as 'RTGS-HO'
127.0.0.1:your_port_number/api/v1/banks/60/RTGS-HO

Also I have attached the WSGI waitress server for that
make mode as prod
so it will run in single click.
