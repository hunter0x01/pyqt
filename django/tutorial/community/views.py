from django.shortcuts import render
from community.forms import *

# Create your views here.
def write(request):
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			form.save() #  DB 에 저정한다. 


	else:
		form = Form()# form 데이터 write.html 전달
	return render(request, 'write.html', {'form':form})
	# request 에서 write.html 로 보내는 작업 


def list(request):
	articleList = Article.objects.all() # 모든 row 가지고 온다 
	return render(request, 'list.html', {'articleList':articleList})


def view(request, num=1):
	article = Article.objects.get(id=num)
	return render(request, 'view.html', {'article':article})