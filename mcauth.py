# coding: utf-8
from bottle import *
TEMPLATE_PATH.append('/views')
import csv
import requests
import re
import configparser
from mcrcon import MCRcon

global param
global capurl
global js
global restype
global geyser_prefix

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
# Settings 
server_address = config_ini.get('Minecraft Server Settings', 'Minecraft_Server_Address')
server_pass = config_ini.get('Minecraft Server Settings', 'RCON_Password')
captchatype = config_ini.get('CAPTCHA Settings', 'CAPTCHA_Service')
rcsite = config_ini.get('CAPTCHA Settings', 'CAPTCHA_Site_Key')
rcsicr = config_ini.get('CAPTCHA Settings', 'CAPTCHA_Secret_Key')
servername = config_ini.get('Minecraft Server Settings', 'Minecraft_Server_Name')
authurl = config_ini.get('Minecraft Server Settings', 'WebServer_Auth_Directory')
geyser_prefix = config_ini.get('Minecraft Server Settings', 'Geyser_Prefix')

# Start

if captchatype == "re":
    param = "g-recaptcha"
    capurl = "https://www.google.com/recaptcha/api/siteverify"
    js = "https://www.google.com/recaptcha/api.js"
    restype = "g-recaptcha-response"
elif captchatype == "h":
    param = "h-captcha"
    capurl = "https://api.hcaptcha.com/siteverify"
    js = "https://js.hcaptcha.com/1/api.js"
    restype = "h-captcha-response"
# Start Page
@route("/")
def start():
    input_text = ""
    try:
        return template("start",text=input_text,rcsite=rcsite,authurl=authurl,servername=servername,js=js,param=param)
    except NameError:
        return template("error",errormessage="サーバー管理者へ：captchatype が不正です。reCAPTCHA を使用する場合は re を、hCaptcha の場合は h と設定してください。")
@route("/", method="POST")
def reg():
    ip = request.remote_addr
    mcid = request.forms.input_text
    mce = request.forms.mce
    if mcid == "" or mce == "":
        return template("error",errormessage="申し訳ございません。Minecraft の MCID/ゲーマータグ、エディションの選択が確認できませんでした。")
    # Captcha Authencation
    recap_res = request.forms.get(restype)
    recap_pay = {
        'secret': rcsicr,
        'response': recap_res,
        'remoteip': ip
    }
    recap_res = requests.post(capurl, data=recap_pay)
    recap_resu = recap_res.json()
    recaped = recap_resu['success']
    mcid = mcid.replace(' ', '_')


    print(recap_resu)

    if recaped == True:
        # IP Check
        file = 'idip.txt'
        f = open('idip.txt', 'r')
        fi = f.read()
        f.close()
        if ip in fi:
            print("registerd user, abort.")
            f.close()
            return template("error",errormessage="あなたは登録済みです。")
        else:
           with open(file,"w", encoding = "utf_8") as f:
               f.write(f"{fi}[{mcid},{ip}]")
               f.close()
           # Edition checker and ID register
           if mce == "java":
                try:
                    with MCRcon(server_address, server_pass, 25575) as mcr:
                        cm = f"whitelist add {mcid}"
                        log = mcr.command(cm)
                        print(log)
                    print("registerd java user, scucess.")
                    return template("check",mcid=mcid,mce=mce,servername=servername)
                except:
                    return template("error",errormessage="不明なエラーが発生しました。サーバー管理者へお問い合わせください。")
           else:
                try:
                    with MCRcon(server_address, server_pass, 25575) as mcr:
                        cm = f"fwhitelist add {geyser_prefix}{mcid}"
                        log = mcr.command(cm)
                        print(log)
                    print("registerd be user, scucess.")
                    return template("check",mcid=mcid,mce=mce,servername=servername)
                except:
                    return template("error",errormessage="不明なエラーが発生しました。サーバー管理者へお問い合わせください。")
    else:
        # No CAPTCHA
        print("no captched user,abort.")
        return template("error",errormessage="申し訳ございませんが CAPTCHA が確認できませんでした。\nひとつ前のページに戻って、再度実行してください。")

run(host="localhost", port=7080,debug=False)
