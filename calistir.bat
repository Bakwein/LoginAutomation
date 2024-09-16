py.exe -m venv myenv
cd myenv
cd Scripts
call activate
cd ..
cd ..
py.exe -m pip install --upgrade pip
pip install -r req_win.txt
cd 1
pyinstaller --onefile --noconsole --icon=ico.ico autoLoginToyo1.py
cd ..
cd 2
pyinstaller --onefile --noconsole --icon=ico.ico autoLoginToyo2.py
