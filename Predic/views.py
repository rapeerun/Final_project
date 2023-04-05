from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults

def predict(request):
    return render(request, 'predic.html')

# chance of success

def predict_success(request):

    if request.method == 'POST':
        print('Success')
        # Patient info
        Patient_ID = str(request.POST.get('Patient_ID'))
        Patient_Age = int(request.POST.get('Patient_Age'))
        Patient_Gender = int(request.POST.get('Patient_Gender'))
        Patient_Blood_Pressure = int(request.POST.get('Patient_Blood_Pressure'))
        Patient_Heartrate = int(request.POST.get('Patient_Heartrate'))


        # unpickle model converting bjects into byte streams and vice versa
        mod=pd.read_pickle("new_model.pickle")

        #  prediction of the model
   
    rst = mod.predict([[Patient_ID, Patient_Age, Patient_Gender, Patient_Blood_Pressure, Patient_Heartrate]])

    Heart_Disease = rst[0]

    PredResults.objects.create(Patient_ID=Patient_ID, Patient_Age=Patient_Age, Patient_Gender=Patient_Gender,
                                   Patient_Blood_Pressure=Patient_Blood_Pressure, Patient_Heartrate=Patient_Heartrate, Heart_Disease=Heart_Disease)

    return JsonResponse({'rst': Heart_Disease, 'Patient_ID': Patient_ID,
                             'Patient_Age': Patient_Age, 'Patient_Gender': Patient_Gender, 'Patient_Blood_Pressure': Patient_Blood_Pressure, 'Patient_Heartrate': Patient_Heartrate},
                            safe=False)


def show_results(request):
    
    info_display= {"dataset": PredResults.objects.all()}
    return render(request, "result.html", info_display)


   

