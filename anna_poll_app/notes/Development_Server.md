## Django Development Server 
Lightweight web server writtin purely in Python. Intended for use while developing so you can develop rapidly without having to deal with configuring a production server until you're ready for production. 

This server should no tbe used for anything resembling a production environement. 

### Atomatic Reloading 
Development server automatically reloads Python code for each request as needed. No need to restart server. But keep in mind, some actions, like adding new files, do not trigger restart. 

### Port 
By default, the runserver command starts the development server on the internal IP at **port 8000**<br/>

To change servers port, pass port in as a command-line argument. Ex:
``` $ python manage.py runserver 8080 ```