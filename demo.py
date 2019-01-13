"""
!/usr/bin/env python
-*- coding: utf-8 -*-
@Time    : 2019/1/11 16:19
@Author  : jiajia
@File    : demo.py
"""
import base64
from fontTools.ttLib import TTFont
base64_string = "d09GRgABAAAAAAgkAAsAAAAAC7gAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAABHU1VCAAABCAAAADMAAABCsP6z7U9TLzIAAAE8AAAARAAAAFZW7ldVY21hcAAAAYAAAAC8AAACTEL0xmVnbHlmAAACPAAAA5YAAAQ0l9+jTWhlYWQAAAXUAAAALwAAADYT2/M2aGhlYQAABgQAAAAcAAAAJAeKAzlobXR4AAAGIAAAABIAAAAwGhwAAGxvY2EAAAY0AAAAGgAAABoG3gW2bWF4cAAABlAAAAAfAAAAIAEZADxuYW1lAAAGcAAAAVcAAAKFkAhoC3Bvc3QAAAfIAAAAXAAAAI/xSePjeJxjYGRgYOBikGPQYWB0cfMJYeBgYGGAAJAMY05meiJQDMoDyrGAaQ4gZoOIAgCKIwNPAHicY2Bk0mWcwMDKwMHUyXSGgYGhH0IzvmYwYuRgYGBiYGVmwAoC0lxTGBwYKr7fY9b5r8MQw6zDcAUozAiSAwDnzgvneJzFkjEOgzAMRX8KpS106NhD9CxMnIOZE3Rh7UmYuiIOwYaUCQkFITHASH9ilkqwto5eJNuRbf0YwBGARx7EB9QbCtYKRpWLewhd3MeT/h03Rs7IdKHrNu9KE5t+SMZqSudmWfhiP7NlihW3js2cELCTjwMu7BlxVjtJsFPpB6b+1/rbru5+rV5EshWOqAuB+kHXApVEmwvUFF0p2D83sUCdYXqBimNIBLsfYyXYXlMq2N2ZGwHhB2osSiR4nEWTz2/adhjGv19T4ZRQQoaNC2kBA7ENJMHxLwI4hkKgzU9GggkhLQ1RS2m2tlnUdGkbbS37IbXT/oDuMmmHXaodeu+kaT1tnbYc9gdM2nW3Reolgn1tiOaDpdcHP5/3eZ4XQAB6/wABEAADICGShI/gAHqg+XqH/QHCAIyTtJTQLAkNJhSJCQWtOKtBwU0SVtwBcYcFh++67LBtjEsyqRIZWVQzS7B+9uD3AzpG5HlOoN4bqlT8Pk88Lgf4hYszN+cXirbW7T19clmgMhw9eZ46h+QsiOUYA0iTAH4wCYCLkSXF0MF9EIkFWWNOEG5RMDiCVgvhptCg9KdXH+6+3tvJFTp/XsoW+ZzEh+h869KF4HgwEhDJSOWTMvyc23n/9r2lNue+nrt2qKnNYuN7KRPwN/LZ7jO2QLhIgn2yWkYsmLn/CfYbsAHERsu0DMVRkQyR7KgF5ru/wuKVZrP218syPOry5Zcn6NuPfd96/8Ie2iGG/PRBRCexyDI8QQmKPDAPAYsC5YPIP3OxUJBhOyOXFU1nI6o3bHMkNzKKOGerOZOpSkqYloXpzOVn7euHZ39ZzFUPWc62DNOzfEbLjdTj097zta1F98jV4rXPduugz947hl3EEAATCIkxAYysSA0BIT8dEEnKkonhpiBhcsqGifAbOxmWooEoZT8X2BTXD1M3cnefL+U/0hXZ3n3BFhilXHpQwdwSNU75kxfXlOmpTit/f/bb10eNVX6q0n07ocfqy/Pr1T6HmWcIxAduoAppcBZKrBW3mgwIwfDAIGIZFpoOkQTlFpSvhlU+mmYdVhx64hOJjUefbs/tq+kHJV1SbLC9OpOuRqIPSz+o8rgme5WxoTPWqNf7ZOfOF4tfd55/p0/FdZhe2misFCOx9f873cPeABfqlkyTqLlWPGS02qh2HB6F8nOiyzO0CUed/rQvS2N39UK4+fBxtv5BtKUe3EteZQYZH2NnsJ9RS08z7gfrokkaH3hs7Ic2+tI2r2Rr1XwsT6wV4I3u32xgLtR4mix8vD2rDb0p5LZfVBm/De5WfnJTT29tXVlXZuqnGZ4MbgG40P1BM6zB1Rn/RpcgKE6WQdlGPd72yl76gtNpd4zdLN1Si/Xyo7Uo9zg8CZudhZXKZjSr3sm02JW1hdrbV/f34VY6JeZOPdlHOnbU8tAoumfZdEOE+7VAm5ufGeOGkxjvU516UPDwFAD/Af534MIAAHicY2BkYGAAYmmtvsfx/DZfGbhZGEDgRlz4fgT9/w0LA9N5IJeDgQkkCgAmYArJAHicY2BkYGDW+a/DEMPCAAJAkpEBFfAAADNiAc14nGNhAIIUBgYmHeIwADeMAjUAAAAAAAAADABGAIwAqADqAS4BdgGaAcwCAAIaAAB4nGNgZGBg4GEwYGBmAAEmIOYCQgaG/2A+AwAOgwFWAHicZZG7bsJAFETHPPIAKUKJlCaKtE3SEMxDqVA6JCgjUdAbswYjv7RekEiXD8h35RPSpcsnpM9grhvHK++eOzN3fSUDuMY3HJyee74ndnDB6sQ1nONBuE79SbhBfhZuoo0X4TPqM+EWungVbuMGb7zBaVyyGuND2EEHn8I1XOFLuE79R7hB/hVu4tZpCp+h49wJt7BwusJtPDrvLaUmRntWr9TyoII0sT3fMybUhk7op8lRmuv1LvJMWZbnQps8TBM1dAelNNOJNuVt+X49sjZQgUljNaWroyhVmUm32rfuxtps3O8Hort+GnM8xTWBgYYHy33FeokD9wApEmo9+PQMV0jfSE9I9eiXqTm9NXaIimzVrdaL4qac+rFWGMLF4F9qxlRSJKuz5djzayOqlunjrIY9MWkqvZqTRGSFrPC2VHzqLjZFV8af3ecKKnm3mCH+A9idcsEAeJxtyzsOgCAQBNAd/KCIhxERbOV3Fxs7E49vXFqneclkhgTVKPqPhkCDFh16SAwYoTBBYyY88r7OHG1my2bZIy6fxbnaL8lXg2H9HuovJ975xLti4kr0AiqQF/I="
bin_data = base64.decodebytes(base64_string.encode())
print(bin_data)
with open('asd.woff', 'wb')as f:
    f.write(bin_data)

font_maoyan = TTFont('asd.woff')
font_maoyan.saveXML('asd.xml')