from encodings import utf_8
from kavenegar import * 
from django.contrib.auth.mixins import UserPassesTestMixin



def send_otp_code(phone_number,code):
    try:
        api = KavenegarAPI('kooft') 
        params = { '' : '',
         'receptor': phone_number,
          'message' : f'کد تایید شما {code}'
           } 
        response = api.sms_send( params)
        b=b'APIException[403] \xda\xa9\xd8\xaf \xd8\xb4\xd9\x86\xd8\xa7\xd8\xb3\xd8\xa7\xd8\xa6\xdb\x8c \xd9\x85\xd8\xb9\xd8\xaa\xd8\xa8\xd8\xb1 \xd9\x86\xd9\x85\xdb\x8c \xd8\xa8\xd8\xa7\xd8\xb4\xd8\xaf '
        
        print(response)
    except APIException as e:
           
        print(type(e))
    except HTTPException as e:
        
        print(type(e))




class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated  and self.request.user.is_admin

