import pyqrcode

s = "www.quickoffice.co.ke"

url = pyqrcode.create(s)

url.svg('my_file1.svg', scale=8)