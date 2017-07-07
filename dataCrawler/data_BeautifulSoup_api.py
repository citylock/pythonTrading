from bs4 import BeautifulSoup


html_doc = """
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title"><b>The Dormouse's story</b></p>
        
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        
        <p class="story">...</p>
        """

soup = BeautifulSoup(html_doc, 'html.parser')

# html 을 보기 편하게 정렬해준다.
print (soup.prettify())


# tag 이름만 가지고 원하는 데이터를 뽑을수 있다
print (soup.head)


# 각각의 태그는 타이틀과 내용으로 분리할수 있다
print (soup.title)
print (soup.title.name)
print (soup.title.string)


print (soup.p['class'])

# 찾고자 하는 첫번째 TAG 만 선택해서 보여준다
print (soup.a)


print (soup.find_all('a'))

print (soup.find(id='link3'))


for link in soup.find_all('a'):
    print (link.get('href'))


# 화면에 찍히는 문자만 따로 보여준다
print (soup.get_text())

