# Python-Price-Checker
Checks price of mechanical keyboard switches and emails when sale is found.
Intended for use with online service such as Heroku. Additional webclients may be necessary to avoid websites from denying requests for being made too quickly from the same client.

# Techniques/Tools used
Requests library - downloading webpage
Beautiful Soup - parsing webpage results
SMTPlib - handling email 
MIME - handling email header, subject, body, etc.
