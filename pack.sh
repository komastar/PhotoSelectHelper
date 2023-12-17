rm -rf dist build
pyinstaller -F main.py --noconsole -n="PhotoSelector"
cp -R resources dist/resources
