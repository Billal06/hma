import requests, json, sys, time, threading

s = []
f = []

def check(key, jml):
	sec="2463478a-0ade-43ad-8152-07070242caed"
	cookies = {
		'SECURITY_TOKEN': sec,
		's_cc': 'true',
		'IDT2': 'IDTN-170483-GSLDkwYphOuoY7QFtoCijVdjHXwwowklxSO35445',
	}
	headers = {
		'Connection': 'keep-alive',
		'Content-Type': 'application/json',
		'Accept': '*/*',
		'Origin': 'https://my.hidemyass.com',
		'Referer': 'https://my.hidemyass.com/en-eu/',
		'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6',
		'User-Agent': '',
	}
	data = '{"correlationId":128,"operationName":"activateLicense","serviceName":"LicenseController","payload":["%s"],"securityToken":"2463478a-0ade-43ad-8152-07070242caed"}' % (key)
	url = "https://my.hidemyass.com/LicenseController/activateLicense"
	r = requests.post(url, data=data, headers=headers, cookies=cookies)
	j = json.loads(r.text)
#	print (j)
	errorData = j["errorData"][0]
	if errorData["errorCode"] != 400:
		print ("Success -> "+str(key))
		s.append(key)
	else:
#		print ("Failed -> "+str(key))
		f.append(key)
	print ("\rTry: %s/%s, Success: %s" % (len(f), jml, len(s)), end="", flush=True)

def jalan(kata, waktu):
	for a in kata+"\n":
		sys.stdout.write(a)
		sys.stdout.flush()
		time.sleep(waktu)

def banner():
	b = """
            .''  ╦ ╦╔╦╗╔═╗  ╔═╗╦ ╦╔═╗╔═╗╦╔═╔═╗╦═╗
  ._.-.___.' (`\ ╠═╣║║║╠═╣  ║  ╠═╣║╣ ║  ╠╩╗║╣ ╠╦╝
 //(        ( `' ╩ ╩╩ ╩╩ ╩  ╚═╝╩ ╩╚═╝╚═╝╩ ╩╚═╝╩╚═
'/ )\ ).__. )    Author: Billal | Thanks: Widhisec
' <' `\ ._/'\    Cyber Ghost ID | Black Coder Crush
   `   \     \ """
	return b

if __name__ == "__main__":
	jalan(banner(), 0.01)
	file = input("\nFile License: ")
	try:
		o = open(file, "r").read()
		for a in o.splitlines():
			th = threading.Thread(target=check, args=(a, len(o.splitlines())))
			th.start()
	except Exception as E:
		print ("Errro -> "+str(E))
		sys.exit()
