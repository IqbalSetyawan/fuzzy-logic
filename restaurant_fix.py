import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

data = pd.read_excel('data_restaurant.xlsx')

makanan = ctrl.Antecedent(np.arange(1, 11, 1), 'makanan')
pelayanan = ctrl.Antecedent(np.arange(1, 11, 1), 'pelayanan')
kebersihan = ctrl.Antecedent(np.arange(1, 11, 1), 'kebersihan')
kualitas = ctrl.Consequent(np.arange(1, 11, 1), 'kualitas')

makanan.automf(3)
pelayanan.automf(3)
kebersihan.automf(3)
kualitas.automf(3)

rule1 = ctrl.Rule(makanan['poor'] & pelayanan['poor'] & kebersihan['poor'], kualitas['poor'])
rule2 = ctrl.Rule(makanan['poor'] & pelayanan['average'] & kebersihan['poor'], kualitas['poor'])
rule3 = ctrl.Rule(makanan['poor'] & pelayanan['good'] & kebersihan['poor'], kualitas['poor'])
rule4 = ctrl.Rule(makanan['average'] & pelayanan['poor'] & kebersihan['poor'], kualitas['poor'])
rule5 = ctrl.Rule(makanan['average'] & pelayanan['average'] & kebersihan['poor'], kualitas['poor'])
rule6 = ctrl.Rule(makanan['average'] & pelayanan['good'] & kebersihan['poor'], kualitas['average'])
rule7 = ctrl.Rule(makanan['good'] & pelayanan['poor'] & kebersihan['poor'], kualitas['poor'])
rule8 = ctrl.Rule(makanan['good'] & pelayanan['average'] & kebersihan['poor'], kualitas['average'])
rule9 = ctrl.Rule(makanan['good'] & pelayanan['good'] & kebersihan['poor'], kualitas['good'])
rule10 = ctrl.Rule(makanan['poor'] & pelayanan['poor'] & kebersihan['average'], kualitas['poor'])
rule11 = ctrl.Rule(makanan['poor'] & pelayanan['average'] & kebersihan['average'], kualitas['average'])
rule12 = ctrl.Rule(makanan['poor'] & pelayanan['good'] & kebersihan['average'], kualitas['average'])
rule13 = ctrl.Rule(makanan['average'] & pelayanan['poor'] & kebersihan['average'], kualitas['poor'])
rule14 = ctrl.Rule(makanan['average'] & pelayanan['average'] & kebersihan['average'], kualitas['average'])
rule15 = ctrl.Rule(makanan['average'] & pelayanan['good'] & kebersihan['average'], kualitas['good'])
rule16 = ctrl.Rule(makanan['good'] & pelayanan['poor'] & kebersihan['average'], kualitas['average'])
rule17 = ctrl.Rule(makanan['good'] & pelayanan['average'] & kebersihan['average'], kualitas['good'])
rule18 = ctrl.Rule(makanan['good'] & pelayanan['good'] & kebersihan['average'], kualitas['good'])
rule19 = ctrl.Rule(makanan['poor'] & pelayanan['poor'] & kebersihan['good'], kualitas['average'])
rule20 = ctrl.Rule(makanan['poor'] & pelayanan['average'] & kebersihan['good'], kualitas['average'])
rule21 = ctrl.Rule(makanan['poor'] & pelayanan['good'] & kebersihan['good'], kualitas['good'])
rule22 = ctrl.Rule(makanan['average'] & pelayanan['poor'] & kebersihan['good'], kualitas['average'])
rule23 = ctrl.Rule(makanan['average'] & pelayanan['average'] & kebersihan['good'], kualitas['good'])
rule24 = ctrl.Rule(makanan['average'] & pelayanan['good'] & kebersihan['good'], kualitas['good'])
rule25 = ctrl.Rule(makanan['good'] & pelayanan['poor'] & kebersihan['good'], kualitas['good'])
rule26 = ctrl.Rule(makanan['good'] & pelayanan['average'] & kebersihan['good'], kualitas['good'])
rule27 = ctrl.Rule(makanan['good'] & pelayanan['good'] & kebersihan['good'], kualitas['good'])

kualitas_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
                                    rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18,
                                    rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27])
kualitas_sim = ctrl.ControlSystemSimulation(kualitas_ctrl)

hasil_penilaian = []
tingkatan = []

for nomor_restoran in data['nomor_restoran']:
    restaurant_data = data[data['nomor_restoran'] == nomor_restoran]
    makanan_val = restaurant_data['makanan'].values[0]
    pelayanan_val = restaurant_data['pelayanan'].values[0]
    kebersihan_val = restaurant_data['kebersihan'].values[0]

    kualitas_sim.input['makanan'] = makanan_val
    kualitas_sim.input['pelayanan'] = pelayanan_val
    kualitas_sim.input['kebersihan'] = kebersihan_val
    kualitas_sim.compute()
    nilai = kualitas_sim.output['kualitas']

    if nilai < 4:
        deskripsi = 'Buruk'
    elif nilai >= 4 and nilai <= 7:
        deskripsi = 'Standar'
    else:
        deskripsi = 'Baik'

    nilai = (kualitas_sim.output['kualitas'])
    hasil_penilaian.append(nilai)
    tingkatan.append(deskripsi)
    print(f"Nomor Restaurant {nomor_restoran}")
    print(f"Nilai: {nilai}")
    print(f"Tingkatan: {deskripsi}\n")

data['Nilai'] = hasil_penilaian
data['Tingkatan'] = tingkatan
data.to_excel('hasil_penilaian.xlsx', index=False)
