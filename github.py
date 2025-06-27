# Menentukan persentase penumpang laki-laki dan perempuan yang selamat
import pandas as pd
data = pd.read_csv('kapal_titanic.csv')
human = data['sex'].count()
frameLaki = data[data['sex'] == 'male'] 
framePerempuan = data[data['sex'] == 'female'] 
jumLakiSelamat = frameLaki[frameLaki['survived'] == 1].shape[0]
jumPerempuanSelamat = framePerempuan[framePerempuan['survived'] == 1].shape[0]
presenSelamatLaki = (jumLakiSelamat/human)*100
presenSelamatPerempuan = (jumPerempuanSelamat/human)*100
print(presenSelamatLaki, presenSelamatPerempuan)