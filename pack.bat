pyinstaller -n="PhotoSelector" --noconsole -F main.py
xcopy /Q /S /Y .\resources .\dist\resources