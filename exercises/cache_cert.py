'''
    Cache certificate demo Glibs Python scripts
'''
#!/usr/bin/python3
import json
import numpy as np
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent / "package_demo")) # Add the modules directory to the sys.path to allow importing modules from it
import glibs_tools as glibs_tools 

def main(_args):
    menu()

def menu():
    glibs_tools.clear_console()    
    cert_cache()
    #test()

cert2id_map, id2cert_map = {}, {}
country_bitmaps, sex_bitmaps = {}, {}

def cert_cache():
    print("==== Cert cache demo ====")
    global cert2id_map, id2cert_map, country_bitmaps, sex_bitmaps
    #cd = cert_data(True)
    cd = cert_data()
    for i in range(len(cd)):
        cert = cd[i]
        print("Cert ID: ", cert.get('certId'))
        cert2id_map[cert.get('certId')] = i
        id2cert_map[i] = cert.get('certId')
        for country in cert.get('countries'):
            if country not in country_bitmaps:
                bit_map = np.zeros(len(cd), dtype=bool)
                bit_map[i] = True
                country_bitmaps[country] = bit_map
            else:
                bit_map = country_bitmaps[country]
                bit_map[i] = True
                country_bitmaps[country] = bit_map
        for sex in cert.get('sexs'):
            if sex not in sex_bitmaps:
                bit_map = np.zeros(len(cd), dtype=bool)
                bit_map[i] = True
                sex_bitmaps[sex] = bit_map
            else:
                bit_map = sex_bitmaps[sex]
                bit_map[i] = True
                sex_bitmaps[sex] = bit_map
    print()
    print("Cert to ID map: ", cert2id_map)
    print()
    print("ID to Cert map: ", id2cert_map)
    print()
    print("Country to Cert map: ", country_bitmaps)
    print()
    print("Sex to Cert map: ", sex_bitmaps)


def cert_data(debug = False):
    #print("==== Cert cache demo ====")
    js = [
        {
            "certId": "C-0001",
            "countries": ["US", "CA", "MX"],
            "validFrom": "2023-01-01",
            "validTo": "2024-01-01",
            "sexs": ["M", "F"]
        },
        {
            "certId": "C-0002",
            "countries": ["US", "CA"],
            "validFrom": "2023-02-01",
            "validTo": "2024-02-01",
            "sexs": ["Ch", "U"]
        },
        {
            "certId": "C-0003",
            "countries": ["MX"],
            "validFrom": "2023-03-01",
            "validTo": "2024-03-01",
            "sexs": ["F"]
        },
        {
            "certId": "C-0004",
            "countries": ["US", "MX"],
            "validFrom": "2023-04-01",
            "validTo": "2024-04-01",
            "sexs": ["M"]
        },
        {
            "certId": "C-0005",
            "countries": ["CA"],
            "validFrom": "2023-05-01",
            "validTo": "2024-05-01",
            "sexs": ["U"]
        },
        {
            "certId": "C-0006",
            "countries": ["US", "CA", "MX"],
            "validFrom": "2023-06-01",
            "validTo": "2024-06-01",
            "sexs": ["M", "F", "U"]
        },
        {
            "certId": "C-0007",
            "countries": ["US"],
            "validFrom": "2023-07-01",
            "validTo": "2024-07-01",
            "sexs": ["Ch"]
        },
        {
            "certId": "C-0008",
            "countries": ["CA", "MX"],
            "validFrom": "2023-08-01",
            "validTo": "2024-08-01",
            "sexs": ["F", "U"]
        },
        {
            "certId": "C-0009",
            "countries": ["US", "CA"],
            "validFrom": "2023-09-01",
            "validTo": "2024-09-01",
            "sexs": ["M", "Ch"]
        },
        {
            "certId": "C-0010",
            "countries": ["MX"],
            "validFrom": "2023-10-01",
            "validTo": "2024-10-01",
            "sexs": ["F", "U"]
        }
    ]
    if debug:
        print("Cert cache demo: ", js)
        print(json.dumps(js, ensure_ascii=False, indent = 2)) # Indent -- human readable format
    return js




def test():
    print("==== Test ====")


if __name__ == "__main__": # This will run if the script was run directly, not called as the module
    main(sys.argv)
    sys.exit() # Stops the script








