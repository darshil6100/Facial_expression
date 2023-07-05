from rest_framework.response import Response
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class Error_messages():

    def empty_url(self,url_path):
        if url_path == '':
                return Response({
                'status':'Fail',
                'Error_message':'Please Provide URL'},status=400),
            
        else:
            pass
    
    def invalid_type(self,url_path):

        val = URLValidator()
        if url_path != "":
    
            try:
                val(url_path)

            except ValidationError:
                return Response({
                    'status':'Fail',
                    'Error_message':'Enter valid url',
                })
        
        else:
            pass

    def name_error(self,data):
        if "url" in data:
            pass
        else:
            return Response({
                'status':'Fail',
                'Error_message':'key is absent',
            })
   

