#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install qrcode


# In[ ]:


import qrcode

inputLink = input("Enter Link for QR Code Generator ; ")
qr = qrcode.QRCode(version = 1,box_size=10, border=2)
qr.add_data(inputLink)
qr.make(fit = True)
img = qr.make_image(fill_color = "black", bacl_color = "white" )

img.save("QR CODE.png")
print("Done")


# In[ ]:




