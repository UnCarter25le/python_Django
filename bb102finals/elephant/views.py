from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.utils import timezone
from datetime import datetime
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse








from elephant.models import maplist,daanburglar,daanpets,daangogoro,daannoise,daannarrowroadway,daantemple,daanroomtest,daanpolice,daanfiredepart,daanpets10000,daanpetsall,tucheng3km10000,tucheng5km10000,tucheng5km,daanfuneral,daangas,daanmarkets
def index(request):
    return render(request, "elephant/test/index.html", locals())
# Create your views here.

def index_puli(request):       #一次取得所有標記
	all=maplist.objects.all()  #取得所有景點
	return render(request, "elephant/test/index_puli.html", locals())


def index_googlemap(request):   #加入地標的功能
	all=maplist.objects.all() 
	if request.method == "POST":		#如果是以POST方式才處理
		mess = request.POST['username'] #取得表單輸入資料
		# location = get_location(mess)
		location1={"la":25.0339031,"ln":121.5623212}
		location2={"la":25.0345301,"ln":121.5621122}
		location3={"la":25.0345301,"ln":121.5690642}
		locations=[location1,location2,location3]
	else:
		mess="表單資料尚未送出!"	
	return render(request, "elephant/test/index_googlemap.html", locals())




def googlemap1(request):#可加入標記（可用在分類選屋展現設施）
	
	if request.method == "POST":		#如果是以POST方式才處理
		mess = request.POST['username'] #取得表單輸入資料
		# location = get_location(mess)
	else:
		mess="表單資料尚未送出!"	
	return render(request, "elephant/test/googlemap_1.html", locals())

def googlemap2(request):  #圖跳出來就定標（可用在目的地選屋）
	if request.method == "POST":		#如果是以POST方式才處理
		mess = request.POST['username'] #取得表單輸入資料
		# location = get_location(mess)
	else:
		mess="表單資料尚未送出!"	
	return render(request, "elephant/test/googlemap_2.html", locals())

def googlemap3(request):
	if request.method == "POST":		#如果是以POST方式才處理
		mess = request.POST['username'] #取得表單輸入資料
		# location = get_location(mess)
	else:
		mess="表單資料尚未送出!"	
	return render(request, "elephant/test/googlemap_3.html", locals())


def daan_burglar(request):   #加入地標的功能
	all=daanburglar.objects.all() 
	if request.method == "POST":		#如果是以POST方式才處理
		mess = request.POST['username'] #取得表單輸入資料
		# location = get_location(mess)
		location1={"la":25.0339031,"ln":121.5623212}
		location2={"la":25.0345301,"ln":121.5621122}
		location3={"la":25.0345301,"ln":121.5690642}
		locations=[location1,location2,location3]
	else:
		mess="表單資料尚未送出!"	
	return render(request, "elephant/test/daan_burglar_googlemap.html", locals())


def daan_pets(request):   #加入地標的功能
	all=daanpets.objects.all() 
	if request.method == "POST":		#如果是以POST方式才處理
		mess = request.POST['username'] #取得表單輸入資料
		# location = get_location(mess)
		location1={"la":25.0339031,"ln":121.5623212}
		location2={"la":25.0345301,"ln":121.5621122}
		location3={"la":25.0345301,"ln":121.5690642}
		locations=[location1,location2,location3]
	else:
		mess="表單資料尚未送出!"	
	return render(request, "elephant/test/daan_pets_googlemap.html", locals())


def daan_gogoro(request):   #加入地標的功能
	all=daangogoro.objects.all() 
	if request.method == "POST":		#如果是以POST方式才處理
		mess = request.POST['username'] #取得表單輸入資料
		# location = get_location(mess)
		location1={"la":25.0339031,"ln":121.5623212}
		location2={"la":25.0345301,"ln":121.5621122}
		location3={"la":25.0345301,"ln":121.5690642}
		locations=[location1,location2,location3]
	else:
		mess="表單資料尚未送出!"	
	return render(request, "elephant/test/daan_gogoro_googlemap.html", locals())

def daan_noise(request):   #加入地標的功能
	all=daannoise.objects.all() 
	if request.method == "POST":		#如果是以POST方式才處理
		mess = request.POST['username'] #取得表單輸入資料
		# location = get_location(mess)
		location1={"la":25.0339031,"ln":121.5623212}
		location2={"la":25.0345301,"ln":121.5621122}
		location3={"la":25.0345301,"ln":121.5690642}
		locations=[location1,location2,location3]
	else:
		mess="表單資料尚未送出!"	
	return render(request, "elephant/test/daan_noise_googlemap.html", locals())

def daan_narrowroadway(request):   #加入地標的功能
	all=daannarrowroadway.objects.all() 
	if request.method == "POST":		#如果是以POST方式才處理
		mess = request.POST['username'] #取得表單輸入資料
		# location = get_location(mess)
		location1={"la":25.0339031,"ln":121.5623212}
		location2={"la":25.0345301,"ln":121.5621122}
		location3={"la":25.0345301,"ln":121.5690642}
		locations=[location1,location2,location3]
	else:
		mess="表單資料尚未送出!"	
	return render(request, "elephant/test/daan_narrowroadway_googlemap.html", locals())

def daan_temple(request):   #加入地標的功能
	all=daantemple.objects.all() 
	if request.method == "POST":		#如果是以POST方式才處理
		mess = request.POST['username'] #取得表單輸入資料
		# location = get_location(mess)
		location1={"la":25.0339031,"ln":121.5623212}
		location2={"la":25.0345301,"ln":121.5621122}
		location3={"la":25.0345301,"ln":121.5690642}
		locations=[location1,location2,location3]
	else:
		mess="表單資料尚未送出!"	
	return render(request, "elephant/test/daan_temple_googlemap.html", locals())

# def daan_suite(request):   #加入地標的功能
# 	all=daansuite.objects.all() 
# 	if request.method == "POST":		#如果是以POST方式才處理
# 		mess = request.POST['username'] #取得表單輸入資料
# 		# location = get_location(mess)
# 		location1={"la":25.0339031,"ln":121.5623212}
# 		location2={"la":25.0345301,"ln":121.5621122}
# 		location3={"la":25.0345301,"ln":121.5690642}
# 		locations=[location1,location2,location3]
# 	else:
# 		mess="表單資料尚未送出!"	
# 	return render(request, "elephant/test/daan_suite_googlemap.html", locals())

def daan_room_test(request):   #加入地標的功能
	all=daanroomtest.objects.all() 
	if request.method == "POST":		#如果是以POST方式才處理
		mess = request.POST['username'] #取得表單輸入資料
		# location = get_location(mess)
		location1={"la":25.0339031,"ln":121.5623212}
		location2={"la":25.0345301,"ln":121.5621122}
		location3={"la":25.0345301,"ln":121.5690642}
		locations=[location1,location2,location3]
	else:
		mess="表單資料尚未送出!"	
	return render(request, "elephant/test/daan_room_test_googlemap.html", locals())


def city_01(request):       #一次取得所有標記
	# all=maplist.objects.all()  #取得所有景點
	return render(request, "elephant/city_01.html", locals())
def city_02(request):       #一次取得所有標記
	# all=maplist.objects.all()  #取得所有景點
	return render(request, "elephant/city_02.html", locals())
def city_03(request):       #一次取得所有標記
	# all=maplist.objects.all()  #取得所有景點
	return render(request, "elephant/city_03.html", locals())
def city_04(request):       #一次取得所有標記
	# all=maplist.objects.all()  #取得所有景點
	return render(request, "elephant/city_04.html", locals())
def city_05(request):       #一次取得所有標記
	# all=maplist.objects.all()  #取得所有景點
	return render(request, "elephant/city_05.html", locals())


def district(request):       #一次取得所有標記
	all_burglar = daanburglar.objects.all()  #取得所有景點
	all_room = daanroomtest.objects.all() 
	all_temple = daantemple.objects.all() 
	all_noise = daannoise.objects.all() 
	all_narrowroadway = daannarrowroadway.objects.all() 
	all_pets = daanpets.objects.all() 
	all_gogoro = daangogoro.objects.all() 
	all_police = daanpolice.objects.all()
	all_firedepart = daanfiredepart.objects.all()
	all_daanpets10000 = daanpets10000.objects.all()
	# all_daanpets10000_1 = daanpets10000.objects.get(mapLandlord="許先生")
	all_daanpetsall = daanpetsall.objects.all()
	all_daanfuneralall = daanfuneral.objects.all()
	all_daangas = daangas.objects.all()
	all_daanmarkets = daanmarkets.objects.all()

	if request.method == "POST":		#如果是以POST方式才處理
		mess = request.POST['username'] #取得表單輸入資料
	else:
		mess="表單資料尚未送出!"	
	return render(request, "elephant/district.html", locals())

def one_by_case(request):       #一次取得所有標記

	return render(request, "elephant/one_by_case.html", locals())

def track_list(request):       #一次取得所有標記
	all_daanpets10000 = daanpets10000.objects.all()
	all_burglar = daanburglar.objects.all()  #取得所有景點
	all_room = daanroomtest.objects.all() 
	all_temple = daantemple.objects.all() 
	all_noise = daannoise.objects.all() 
	all_narrowroadway = daannarrowroadway.objects.all() 
	all_pets = daanpets.objects.all() 
	all_gogoro = daangogoro.objects.all() 
	all_police = daanpolice.objects.all()
	all_firedepart = daanfiredepart.objects.all()
	all_daanpetsall = daanpetsall.objects.all()
	all_daangas = daangas.objects.all()
	all_daanfuneralall = daanfuneral.objects.all()
	all_daanmarkets = daanmarkets.objects.all()
	return render(request, "elephant/track_list.html", locals())
def home(request):       #一次取得所有標記
	# all=maplist.objects.all()  #取得所有景點
	return render(request, "elephant/home.html", locals())

def object_select(request):       #一次取得所有標記
	# all=maplist.objects.all()  #取得所有景點
	all_tucheng5km = tucheng5km.objects.all()  #取得所有景點
	all_tucheng5km10000 = tucheng5km10000.objects.all()  #取得所有景點
	all_tucheng3km10000 = tucheng3km10000.objects.all()  #取得所有景點
	return render(request, "elephant/object_select.html", locals())

def tucheng_test(request):       #一次取得所有標記
	# all=maplist.objects.all()  #取得所有景點
	return render(request, "elephant/test/tucheng_test.html", locals())