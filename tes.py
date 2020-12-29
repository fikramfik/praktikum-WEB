import requests, schedule

def maluku():
    api_url="https://api.kawalcorona.com/indonesia/provinsi/"
    rstl= requests.get(api_url).json()
    cek=rstl[19]
    ambil_dic= cek ["attributes"]
    a=[ambil_dic]
    print(a)

r_maluku=schedule.every(2).seconds.do(maluku)

while True:
    schedule.run_pending()

data_maluku=maluku()
print(data_maluku)