# ping_alert
send a mail via sendgrid after 4 ping failures with a 1s timeout

## nb :
to install python3 on windows : 
`https://docs.python.org/fr/3/using/windows.html`

to install the external libs with pip:
`pip install multiping`
`pip install sendgrid`

remember to replace variables in lib/sendgrid.py (mail contents and api key) and edit the ip addr list in the main.py file 
execute the main.py script in python3 with administrator rights