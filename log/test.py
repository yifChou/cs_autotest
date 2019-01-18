a = "pic_storage\\picture\\tms\\airtransp_manage\\update_data\\expect\\tdh_123-20181225.png"
b = a[a.find("expect\\")+7:]
c = a[0:a.find("expect\\")+7]
print(b,c)