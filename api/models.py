from django.db import models
import os
from tensorflow import keras
from django.conf import settings
# Create your models here.

class Emotion_predictior(models.Model):

    model_path = os.path.join(settings.MODELS,"Emotion_predictor.h5")
    Model = keras.models.load_model(model_path)
