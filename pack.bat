pyinstaller -n="PhotoSelector" --noconsole -F main.py
xcopy /Q /S /Y /I .\resources .\dist\resources