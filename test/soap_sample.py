# -*- coding: utf-8 -*-

from requests import Session
from zeep import Client
from zeep import helpers
from zeep.transports import Transport

import warnings
warnings.filterwarnings("ignore")

def main():
    wsdl = "https://dsm.trendmicroindia.com:443/webservice/Manager?WSDL "
    username = "admin"
    password = "P@ssw0rd"
    try:
        session = Session()
        session.verify = False
        transport = Transport(session=session)
        client = Client(wsdl, transport=transport)
        sid = client.service.authenticate(username, password)
        print(client.service.hostRetrieveAll(sid))
    finally:
        client.service.endSession(sid)

if __name__ == "__main__":
    main()
