import requests
import json

url="https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
expiry ="24-sep-2020"
def fetch_oi():
        r = requests.get(url).json()
        #print(r)
        '''if expiry:
                ce_values = [data['CE'] for data in r['records']['data'] if "CE" in data and str(data['expiryData']).lower()==str(expiry).lower()]
                pe_values = [data['PE'] for data in r['records']['data'] if "PE" in data and str(data['expiryData']).lower()==str(expiry).lower()]
        else:
                ce_values = [data['CE'] for data in r['filtered']['data'] if "CE" in data]
                pe_values = [data['PE'] for data in r['filtered']['data'] if "PE" in data]
                ce_data =pd.DataFrame(ce_values)
                pe_data =pd.DataFrame(pe_values)'''
        with open("old.json","w") as files:
           files.write(json.dumps(r,indent=4,sort_key = True))
        ce_value = [data['CE'] for data in r['filtered']['data'] if "CE" in data]
        pe_value = [data['PE'] for data in r['filtered']['data'] if "PE" in data]
        
        print(ce_value)
        print(pe_value)
def main():
        fetch_oi()

if __name__=='__main__':
        main()