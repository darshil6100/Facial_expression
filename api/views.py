import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser
from django.views.decorators.csrf import csrf_exempt
import cv2
from .models import *
import urllib
from django.conf import settings
from .common import Error_messages
# Create your views here.


class Framework_View(APIView):
    parser_classes = ['MultipartParser','JSONParser']
    @csrf_exempt
    def post(self,request):

        try: 
            content_type = request.headers.get("Content-Type")
            if content_type == "application/json":
                data = request.data
            else:
                return Response({
                    'status':'Fail',
                    'Error message':'Request data must be in json format',
                })
            input_url = "url"
            url_path = data.get(input_url)   #getting the url
            
            print("=============",content_type)     
            # print("*******************", request.data)
            

                 #Throws error when there is empty url
            if Error_messages.empty_url(self,url_path):
                return Error_messages.empty_url(self,url_path)
                 
                #Throws error when all keys are not present
            elif Error_messages.name_error(self,data):
                return Error_messages.name_error(self,data) 

                #Throws error when url is not valid
            elif Error_messages.invalid_type(self,url_path):
                return Error_messages.invalid_type(self,url_path)

            else:
                pass

            head,tail = os.path.split(url_path) #splitting the url 
            #print(tail)
                    
            #downloading the image
            opener=urllib.request.build_opener() 
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            path = os.path.join(settings.BASE_DIR,"Images")
            local_path= os.path.join(path,tail)
            urllib.request.urlretrieve(url_path,local_path)

                #opening the image
            img = cv2.imread(local_path)

                #load models
            Prediction_model = Emotion_predictior.Model

                #preprocessing the image
            image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (224,224)) #resizing the image
            image = np.array(image)/255 #scalling the image data
            image = np.expand_dims(image, axis= 0)

                #predicting the value
            Prediction = Prediction_model.predict(image)
            Prediction_label = np.argmax(Prediction)
            label_list = ['anger','contempt','disgust','fear','happy','sadness','surprise']

            return Response({
                'status': 'success',
                'Prediction': label_list[Prediction_label],
            }, status = 200)   

        except Exception as e:
            message = str(e)
            # print("============",type(message))
            return Response({
                'status':'Fail',
                'Error Message': message,
            },status = 400)








