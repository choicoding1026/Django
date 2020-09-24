from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

# Create your views here.
def loginForm(request):
    
    return render(request, "loginForm.html")

def loginGET(request):
    userId = request.GET.get("userId", "default") # key 값이 다른 경우 default 값 출력
    userPw = request.GET.get("userPw")
    phone = request.GET.getlist("phone")
    print(userId,userPw,phone)
    user = {}
    user['userId'] = userId
    user['userPw'] = userPw
    user['phone'] = phone
    return render(request, "loginInfo.html", user)

def loginPOST(request):
    userId = request.POST.get("userId")
    userPw = request.POST.get("userPw")
    phone = request.POST.getlist("phone")
    print(userId,userPw,phone)
    return render(request, "loginInfo.html")

def login99(request):
    print("request", request)
    print("WSGIReqest", dir(WSGIRequest))
    print("WSGIRequest.COOKIES", request.COOKIES)
    print("WSGIRequest.FILES", request.FILES)
    print("WSGIRequest.GET", request.GET)
    print("WSGIRequest.POST", request.POST)
    print("WSGIRequest.__class__", request.__class__)
    print("WSGIRequest.__delattr__", request.__delattr__)
    print("WSGIRequest.__dict__", request.__dict__)
    print("WSGIRequest.__dir__", request.__dir__)
    print("WSGIRequest.__doc__", request.__doc__)
    print("WSGIRequest.__eq__", request.__eq__)
    print("WSGIRequest.__format__", request.__format__)
    print("WSGIRequest.body", request.body)
    print("WSGIRequest.content_params", request.content_params)
    
    '''
    WSGIReqest [24/Sep/2020 13:22:50] "GET /main/login/?userId=abc&userPw=abc HTTP/1.1" 200 152
    ['COOKIES', 'FILES', 'GET', 'POST', '__class__',
     '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
      '__format__', '__ge__', '__getattribute__', '__gt__',
       '__hash__', '__init__', '__init_subclass__', '__iter__',
        '__le__', '__lt__', '__module__', '__ne__', '__new__',
         '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
          '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
           '_current_scheme_host', '_encoding', '_get_full_path',
            '_get_post', '_get_raw_host', '_get_scheme',
             '_initialize_handlers', '_load_post_and_files',
              '_mark_post_parse_error', '_set_content_type_params',
               '_set_post', '_upload_handlers', 'accepted_types',
                'accepts', 'body', 'build_absolute_uri',
                 'close', 'encoding', 'get_full_path',
                  'get_full_path_info', 'get_host', 'get_port',
                   'get_raw_uri', 'get_signed_cookie', 'headers',
                    'is_ajax', 'is_secure', 'parse_file_upload',
                     'read', 'readline', 'readlines', 'scheme',
                      'upload_handlers']

    '''
    return render(request, "loginInfo.html")
