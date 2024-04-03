# Fuzzy Logic
![image](https://github.com/IqbalSetyawan/fuzzy-logic/assets/163812051/0873097f-3c07-4d9f-97ad-286f0da87569)

Kode di atas adalah implementasi sistem kontrol logika fuzzy untuk mengevaluasi kualitas restoran berdasarkan tiga faktor: makanan, pelayanan, dan kebersihan. Fuzzy logic memungkinkan kita untuk menggambarkan kualitas restoran secara tidak pasti atau tidak tegas, sehingga memungkinkan untuk menangkap ketidakpastian dan kompleksitas dalam penilaian manusia terhadap kualitas restoran.

Pertama-tama, kita memuat data restoran dari file Excel yang diberikan. Kemudian, kita mendefinisikan variabel input (makanan, pelayanan, dan kebersihan) dan output (kualitas) 
![image](https://github.com/IqbalSetyawan/fuzzy-logic/assets/163812051/3b2f6755-2861-438e-ad4c-08fd85b4d83f)

beserta fungsi keanggotaannya menggunakan library skfuzzy. Fungsi keanggotaan ini memodelkan bagaimana variabel input dan output berkaitan dengan label-labellnya (misalnya, "poor", "average", "good").
![image](https://github.com/IqbalSetyawan/fuzzy-logic/assets/163812051/d2d87087-c567-4748-8c11-1f8ca79e6e73)

Selanjutnya, kita mendefinisikan rules yang menghubungkan variabel input dengan variabel output. Rules ini mencerminkan aturan logika fuzzy berdasarkan pengalaman atau pengetahuan yang dimiliki. Dalam kasus ini, rules tersebut menyatakan bahwa jika makanan buruk, pelayanan buruk, dan kebersihan buruk, maka kualitas restoran akan buruk, dan sebagainya.
![image](https://github.com/IqbalSetyawan/fuzzy-logic/assets/163812051/9cb9ad63-b830-4e29-962e-4037f660595b)

Setelah itu, kita membuat kontrol sistem menggunakan rules yang telah ditentukan. Control system ini akan digunakan untuk mensimulasikan evaluasi kualitas restoran berdasarkan input yang diberikan.
![image](https://github.com/IqbalSetyawan/fuzzy-logic/assets/163812051/d7c2df50-4b6f-4a91-9709-ffc37493471b)

Kemudian, kita iterasi melalui setiap restoran dalam data, menghitung tingkat kualitas menggunakan kontrol sistem yang telah dibuat, 
![image](https://github.com/IqbalSetyawan/fuzzy-logic/assets/163812051/36aa7e61-31a2-412c-ae67-747f3887abb9)

dan mencetak hasilnya. 
![image](https://github.com/IqbalSetyawan/fuzzy-logic/assets/163812051/82ada929-5cb4-47aa-ba87-3ce3663b2412)

Deskripsi kualitas (buruk, standar, baik) ditentukan berdasarkan tingkat kualitas yang dihasilkan.
![image](https://github.com/IqbalSetyawan/fuzzy-logic/assets/163812051/794b3d6b-4179-462a-8f87-b6b92c977f55)


Penjelasan command-command yang digunakan:

1. `import pandas as pd`: Mengimpor library pandas untuk manipulasi data.
2. `import numpy as np`: Mengimpor library numpy untuk operasi numerik.
3. `import skfuzzy as fuzz`: Mengimpor library skfuzzy sebagai fuzz.
4. `from skfuzzy import control as ctrl`: Mengimpor modul kontrol dari skfuzzy.
5. `data = pd.read_excel('data_restaurant.xlsx')`: Memuat data restoran dari file Excel.
6. `ctrl.Antecedent()`: Membuat variabel input fuzzy.
7. `ctrl.Consequent()`: Membuat variabel output fuzzy.
8. `automf()`: Menggunakan metode automf untuk menghasilkan fungsi keanggotaan secara otomatis.
9. `ctrl.Rule()`: Membuat aturan fuzzy.
10. `ctrl.ControlSystem()`: Membuat kontrol sistem fuzzy.
11. `ctrl.ControlSystemSimulation()`: Membuat simulasi sistem kontrol fuzzy.
12. `input['variabel'] = nilai`: Memberikan nilai pada variabel input.
13. `compute()`: Menghitung output dari sistem kontrol fuzzy.
14. `output['variabel']`: Mendapatkan nilai output dari sistem kontrol fuzzy.
15. `print()`: Mencetak hasil evaluasi kualitas restoran.
