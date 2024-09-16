#!/bin/bash

echo "python'un >=3.8 versiyonlarinda calisir"
echo "default olarak x olan kullanici adi ve sifreleri değiştirmeyi unutmayin"

echo "env oluşturuluyor"
python3.8 -m venv myenv
echo "env başarıyla oluşturuldu"

echo "env içine giriliyor"
cd myenv
cd bin
chmod +x activate
source activate
cd ..
cd ..
echo "env aktif. gerekli modüller indiriliyor"
pip install --upgrade pip
pip install -r requirements.txt
echo "modülller  indirildi"

echo "ilk dosyaya giriliyor"
cd 1
echo "ilk dosya için .exe oluşturuluyor"
pyinstaller --onefile --noconsole --icon=ico.ico autoLoginToyo1.py -y
echo "ilk dosya için .exe oluşturuldu"
cd ..
cd 2
echo "ikinci dosya için .exe oluşturuluyor"
pyinstaller --onefile --noconsole --icon=ico.ico autoLoginToyo2.py -y
echo "ikinci dosya için .exe oluşturuldu"