import os
import ProxyCloud

BOT_TOKEN = '5867281966:AAEfBMW4rj8J1g5e8AvqM2RVIVouHD0iYqU' #Aqui va el token del bot
API_ID =  12569968 #Tu api id de telegram
API_HASH = '2d5b54d8745cab19f3bf12cfd77c4897' #Tu api id de telegram
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','Rebelde59').split(';')

static_proxy = 'socks5h://KHDKKGYGJDJEGKYHJDGFGGYJIJIDRDGGLGGJKH' #agrega si kieres tener un proxy statico Con @raydel0307 si kieres comprar un proxy
PROXY = ProxyCloud.parse(static_proxy)

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
  
#Lo siguiente son las tablas de la base de datos de usarios, 
#es obligatorio agregar a aquellos usarios estaticos puestos en el main.py
#los agregados mediante /add no es necesario
#ponerlos valor 0 siempre

space = {}
space['insomnioh'] = 0
