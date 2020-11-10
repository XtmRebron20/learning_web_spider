'''
使用Respoense对象的cookies属性获取cookies信息
返回的类型是RequestsCookiesJar类型
要使用items（）方法转换为元祖列表进行打印
'''
# import requests

# r = requests.get('https://www.baidu.com')
# print(r.cookies)

# for key,value in r.cookies.items():
#     print(key + '=' + value)

'''
这是一个使用cookie登录知乎的例子
将Cookis包含在请求头中
可以看到返回的Response中带有登陆后才可以见到的信息
'''
import requests

headers = {
    'Cookie':'_zap=42663803-ec2b-4419-816c-519cb6c7ebc1; '
        'd_c0="ACCcj91JJxKPTv2xpmJiYjOEnYlyDO1vNYY=|1604654254"; '
        '_xsrf=djQgPs6hUSaDdPcwarIuc7kkAbB09Gbj; '
        'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1604654257,1604736260; '
        'capsion_ticket="2|1:0|10:1604736258|14:capsion_ticket|44:YzBjOWQ'
        'xNzEzYWFjNGJhZmI1YzQ0NmNiY2M3ZThkMWM=|6665498fae959ed8ff86c3293be'
        '2dead7c028e399bdf85fd77ace9cff60c3d49"; SESSIONID=j5fkI35mSRzqguQl'
        'mwm642DjWoGTXygcS9hz9G0Oi1v; JOID=VVoQBkvqvQoqbC81fujvXk_Zrx9uhY9s'
        'RCIZBxO-6ndbDl1hFevvqXduLTJ7WwFOiOpRbieTDl5D5_DiLI4RTn4=; osd=UFscC'
        '03vvAYnaio0cuXpW07VohlrhINhQicYCx6473ZXA1tkFOfir3JvIT99XgBChexUbyueC'
        'FtC6_3kKY8dQ3g=; z_c0="2|1:0|10:1604736274|4:z_c0|92:Mi4xcmoxeUFnQUFB'
        'QUFBSUp5UDNVa25FaVlBQUFCZ0FsVk5FcU9UWUFEbm9uNG4zaXlPNGZBamRMTXVuWUFtWG'
        'hLRDZR|17dd59a4f07079a3fc0b55464a6c8796a8e449097639628d94b0da387500727b"; '
        'unlock_ticket="ABAKkDQbRAkmAAAAYAJVTRpcpl_Uhykl8gmhWTSbu3GegI_qnl3MHA=="; '
        'tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1604736276; KLBRSID=37f2e8'
        '5292ebb2c2ef70f1d8e39c2b34|1604736276|1604736258',
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)