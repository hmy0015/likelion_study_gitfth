def get_web(url):
	"""URL을 넣으면 페이지 내용을 돌려주는 함수"""
	import urllib.request # urllib라는 라이브러리를 가져와
	response = urllib.request.urlopen(url) # 받은 url을 열고
	data = response.read() # 데이터를 읽어
	decoded = data.decode('utf-8') # 사람이 읽을 수 있도록 디코딩
	return decode # 값을 반환
	
url = input('웹 페이지 주소? ') # url을 입력받음
content = get_web(url)
print(content)