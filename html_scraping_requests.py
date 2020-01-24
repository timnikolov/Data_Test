
def get_exposure_monitor_all_tables():
    #Import libraries
    import pandas as pd
    import requests
    from requests_ntlm import HttpNtlmAuth


    try:
        #create request to return html of the address
        r = requests.get('http:...', auth=HttpNtlmAuth('user', 'pass'))

        #MAP DIFFERENT CONTENT TABLES
        FES = pd.read_html(r.text, header=0)[2]
        fx = pd.read_html(r.text, header=0)[4]
        eq = pd.read_html(r.text, header=0)[5]
        indices = pd.read_html(r.text, header=0)[6]
        etfs = pd.read_html(r.text, header=0)[7]
        debt = pd.read_html(r.text, header=0)[8]
        commodities = pd.read_html(r.text, header=0)[9]

        tables = [FES, fx, eq, indices, etfs, debt, commodities]
        return tables

    except Exception as e:
            return e