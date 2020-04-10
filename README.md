# pOVHAvailableServers

**About**

This small repo permits you to call OVH Kimsufi servers availability API.
When a server becomes available, you receive an email containing a direct link to the server page.

**Installation**

You need Python 3.5 and pip3: `$ sudo apt-get install python3 python3-pip`

Then install the following modules:
`$ pip3 install requests configParser`

Update the configuration file [src/config.txt](src/config.txt):

```txt
[API]
url = https://url-of-api.com

[Server]
Hardware = server-reference
Region = europe
link = https://link-to-book-the-server.com

[SMTP]
From = from@example.com
To = to@example.com
UseGmail = True
#useless if using Gmail
server = localhost
port = 25
```

If you set `UseGmail = True`, you will need to install the following modules to use Gmail API client:

`$ pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`


**First use**

Edit the config file and set a `Hardware` that is currently available

Then run `$ python main.py`

You will have to follow a procedure to be able to send email with Gmail
