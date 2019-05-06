import scripts.config as config
import requests

def login():
    with requests.Session() as session:
    #login to the website
        session.post(config.login_url, data=config.payload)
        return session