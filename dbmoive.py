from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://mo:jae@cluster0.joa3ijk.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

# 1. 가버나움 평점 들고오기
# find_one() 사용

movie = db.movies.find_one({'title':'가버나움'})
star = movie['star']

# 2. 가버나움 평점과 같은영화의 제목들
movie2 = list(db.movies.find({},{'_id':False}))
# {'star' : star} 도 가능함

for i in range (1,50):
    if star == movie2[i]['star']:
        print(movie2[i]['title'])



# 3. 평점 등의 숫자는 현재 문자열로 있음
#따라서 먼저 문자열0 으로 바꾸어 주어야 한다.
db.movies.update_one({'title':'가버나움'}, { '$set':{'star':'0'}})