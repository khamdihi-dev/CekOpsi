import re, requests
from bs4 import BeautifulSoup as bs

from rich.tree import Tree
from rich import print as zprint

username = "" # MASUKAN ID ATAU EMAIL AKUN FB KAMU
password = "" # MASUKAN KATA SANDI AKUN FB KAMU

class Login:

    def __init__(self):
        self.item,self.data = [], {}
        self.nunu = requests.Session()
        self.Brute()

    def Brute(self):
        self.link = self.nunu.get('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
        self.fika = bs(self.link.text,'html.parser')
        self.value = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries"]
        for self.find in self.fika.find_all("input"):
            if self.find.get("name") in self.value:
               self.data.update({self.find.get("name"):self.find.get("value")})

        self.data.update({
           "email":username,
           "pass":password,
           "login":"Masuk"
        })

        headers = {
           "Host": "m.facebook.com",
           "x-fb-lsd": self.data.get("lsd"),
           "user-agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.117 Mobile Safari/537.36",
           "viewport-width": "360",
           "sec-ch-ua-platform": '"Android"',
           "accept": "*/*",
           "sec-fetch-site": "same-origin",
           "sec-fetch-mode": "cors",
           "sec-fetch-dest": "empty",
           "referer": "https://m.facebook.com/profile.php?eav=Afbqp5f0f_Ll_KxmzXTD2qIlqIGqQYB2Wunwkroy0qTugsMMrB9ngvHTlKDYW3sv-rk&paipv=0",
           "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        self.khamdihiXD = ["Gak Jelas Banget Hidup Gw","action"]
        self.url_login_ = self.fika.find('form', method='post').get(self.khamdihiXD[1])
        self.nufikha    = self.nunu.post("https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl", data=self.data, headers=headers)
        if "checkpoint" in self.nufikha.cookies.get_dict():
            data1,nufikha = {}, []
            self.url_chekpoint = bs(self.nufikha.text,'html.parser')
            self.dataList = ["fb_dtsg","jazoest","checkpoint_data","nh"]
            for items in self.url_chekpoint.find_all("input"):
                if items.get('name') in self.dataList:
                   data1.update({items.get('name'):items.get('value')})
            data1.update({"submit[Continue]":"Lanjutkan"})
            xxxx = self.url_chekpoint.find('form', method='post')['action']
            wwww = self.nunu.post(f'https://m.facebook.com{xxxx}', data=data1)
            pars = bs(wwww.text,'html.parser')
            opsi = pars.find_all('option')
            if len(opsi) == 0:
                 tree = Tree('',style='bold yellow')
                 tree.add(f'username : {username}').add(f'password : {password}')
                 tree.add('tidak ada opsi yang tersedia')
                 zrpint(tree)
            else:
                 ytta = Tree('')
                 for cantik in opsi:
                     nufikha.append(cantik.text)

                 loop = 0
                 for _nunu_ in nufikha:
                     loop +=1
                     ytta.add(f"{loop}. {_nunu_}")
                 tree = Tree("",style='bold yellow')
                 tree.add(f'[bold white]username : {username}')
                 tree.add(f'[bold white]password : {password}')
                 tree.add(f'[bold white]ada {len(nufikha)} opsi').add(ytta)
                 zprint(tree)

        elif "c_user" in self.nunu.cookies.get_dict():
              coki = ";".join([str(kunci)+'='+str(value) for kunci, value in self.nunu.cookies.get_dict().items()])
              tree = Tree("",style="bold green")
              tree.add(f'[bold white]username : [bold green]{username}')
              tree.add(f'[bold white]password : [bold green]{password}').add(coki)
              zprint(tree)
        else:
              tree = Tree("")
              tree.add(f'[bold white]username : [bold red]{username}')
              tree.add(f'[bold white]password : [bold red]{password}')
              tree.add('[bold white]status   : [bold yellow]Kata sandi salah atau spam')
              zprint(tree)

if __name__ == '__main__':
   Login()

