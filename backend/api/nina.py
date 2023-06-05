import requests
import json
# Gebietscode von https://www.xrepository.de/api/xrepository/urn:de:bund:destatis:bevoelkerungsstatistik:schluessel:rs_2021-07-31/download/Regionalschl_ssel_2021-07-31.json
# ab Stelle 6 nur Nullen verwenden!

def get_nina_warnings():
    ninaBaseUrl = "https://warnung.bund.de/api31"
    #gebietscodeSegeberg = "010600000000"
    #gebietscodeKiel="010020000000"
    #gebietscodeSchwerin="120610000000"
    gebietscodes=["010600000000", "010020000000", "120610000000"]
    for gebietscode in gebietscodes:
        response = requests.get(ninaBaseUrl+"/dashboard/"+gebietscode+".json")
        warnungen_list = []   # Create an empty list to hold the warnings
        if response.status_code == 200:
            warnungen = response.json()
            for warnung in warnungen:
                id = warnung["id"]
                warningDetails = requests.get(
                    ninaBaseUrl + "/warnings/" + id + ".json").json()
                meldungsText = warningDetails["info"][0]["headline"] + ": " + warningDetails["info"][0]["description"]
                if "<br/>" in meldungsText:
                    meldungsText = meldungsText.replace("<br/>", " ")
                warnungen_list.append(meldungsText)
        return warnungen_list