# Fuzzy Logic

Kode di atas adalah implementasi sistem kontrol logika fuzzy untuk mengevaluasi kualitas restoran berdasarkan tiga faktor: makanan, pelayanan, dan kebersihan. Fuzzy logic memungkinkan kita untuk menggambarkan kualitas restoran secara tidak pasti atau tidak tegas, sehingga memungkinkan untuk menangkap ketidakpastian dan kompleksitas dalam penilaian manusia terhadap kualitas restoran.

Pertama-tama, kita memuat data restoran dari file Excel yang diberikan. Kemudian, kita mendefinisikan variabel input (makanan, pelayanan, dan kebersihan) dan output (kualitas) 

<img width="750px" src="Screenshot 2024-04-03 132424.png">

beserta fungsi keanggotaannya menggunakan library skfuzzy. Fungsi keanggotaan ini memodelkan bagaimana variabel input dan output berkaitan dengan label-labellnya (misalnya, "poor", "average", "good").
<img width="750px" src="Screenshot 2024-04-03 132551.png">

Selanjutnya, kita mendefinisikan rules yang menghubungkan variabel input dengan variabel output. Rules ini mencerminkan aturan logika fuzzy berdasarkan pengalaman atau pengetahuan yang dimiliki. Dalam kasus ini, rules tersebut menyatakan bahwa jika makanan buruk, pelayanan buruk, dan kebersihan buruk, maka kualitas restoran akan buruk, dan sebagainya.

<img width="750px" src="Screenshot 2024-04-03 133245.png">

Setelah itu, kita membuat kontrol sistem menggunakan rules yang telah ditentukan. Control system ini akan digunakan untuk mensimulasikan evaluasi kualitas restoran berdasarkan input yang diberikan.

<img width="750px" src="Screenshot 2024-04-03 133757.png">

Kemudian, kita iterasi melalui setiap restoran dalam data, menghitung tingkat kualitas menggunakan kontrol sistem yang telah dibuat, 

<img width="750px" src="Screenshot 2024-04-03 133852.png">

dan mencetak hasilnya. 

<img width="750px" src="Screenshot 2024-04-03 133927.png">

Deskripsi kualitas (buruk, standar, baik) ditentukan berdasarkan tingkat kualitas yang dihasilkan.

<img width="750px" src="Screenshot 2024-04-03 133947.png">

Berikut adalah hasilnya :

<img width="750px" src="Screenshot 2024-04-03 143714.png">

Dan berikut adalah hasil di file excelnya :

<img width="750px" src="Screenshot 2024-04-03 143811.png">

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
16. `data.to_excel()`: Mencetak data terkait ke dalam file excel
