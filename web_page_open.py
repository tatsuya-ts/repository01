import webbrowser

#開くブラウザの指定　パスはブラウザのexeファイルのある場所を記載する 
browser = webbrowser.get('"C:\\Users\\ユーザ名\\AppData\\Local\\Vivaldi\\Application\\vivaldi.exe" %s')

#開きたいURLを変数に格納
YAHOONEWS = 'https://news.yahoo.co.jp'

openList = [YAHOONEWS]

for url in openList:
     browser.open(url)
