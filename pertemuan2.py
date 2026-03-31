import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl 

Suhu = ctrl.Antecedent(np.arange(0, 41), 'Suhu')
Kelembapan = ctrl.Antecedent(np.arange(0,101), 'Kelembapan')
Kecepatan_kipas = ctrl.Consequent(np.arange(0, 101), 'Kecepatan Kipas')

Suhu['dingin'] = fuzz.trimf(Suhu.universe, [0, 0, 20])
Suhu['sedang'] = fuzz.trimf(Suhu.universe, [10, 20, 30])
Suhu['panas'] = fuzz.trimf(Suhu.universe, [20,40,40])


Kelembapan['kering'] = fuzz.trimf(Kelembapan.universe, [0, 0, 50])
Kelembapan['normal'] = fuzz.trimf(Kelembapan.universe, [25, 50, 75])
Kelembapan['basah'] = fuzz.trimf(Kelembapan.universe, [50, 100, 100])

Kecepatan_kipas['lambat'] = fuzz.trimf(Kecepatan_kipas.universe, [0, 0, 50])
Kecepatan_kipas['sedang'] = fuzz.trimf(Kecepatan_kipas.universe, [25, 50, 75])
Kecepatan_kipas['cepat'] = fuzz.trimf(Kecepatan_kipas.universe, [50, 100, 100])

aturan1 = ctrl.Rule(Suhu['dingin'] & Kelembapan['kering'], Kecepatan_kipas['lambat'])
aturan2 = ctrl.Rule(Suhu['dingin'] & Kelembapan['normal'], Kecepatan_kipas['lambat'])
aturan3 = ctrl.Rule(Suhu['dingin'] & Kelembapan['basah'], Kecepatan_kipas['sedang'])

aturan4 = ctrl.Rule(Suhu['sedang'] & Kelembapan['kering'], Kecepatan_kipas['lambat'])
aturan5 = ctrl.Rule(Suhu['sedang'] & Kelembapan['normal'], Kecepatan_kipas['sedang'])
aturan6 = ctrl.Rule(Suhu['sedang'] & Kelembapan['basah'], Kecepatan_kipas['cepat'])

aturan7 = ctrl.Rule(Suhu['panas'] & Kelembapan['kering'], Kecepatan_kipas['sedang'])
aturan8 = ctrl.Rule(Suhu['panas'] & Kelembapan['normal'],   Kecepatan_kipas['cepat'])
aturan9 = ctrl.Rule(Suhu['panas'] & Kelembapan['basah'], Kecepatan_kipas['cepat'])

engine = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4, aturan5, aturan6, aturan7, aturan8, aturan9])
system = ctrl.ControlSystemSimulation(engine)

system.input['Suhu'] = 30
system.input['Kelembapan'] = 40
system.compute()
print(system.output['Kecepatan Kipas'])

Kecepatan_kipas.view(sim=system)
input("Tekan Enter untuk keluar...")