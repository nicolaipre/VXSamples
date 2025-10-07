from future.plugins import Plugin

# opentip.kaspersky.com

"""
# curl 'https://opentip.kaspersky.com/ui/lookup' \
-H 'Accept: application/json, text/plain, */*' \
    - H 'Accept-Language: en-US,en;q=0.9' \
    - H 'Connection: keep-alive' \
    - H 'Content-Type: application/octet-stream' \
    - b 'Kjwgc9myC=8HsUon8o32vmeQzDDdTJFUfQEn4MB1jDi0sjg9IUWt17ImlwIjoiQUFBQUFBQUFBQUFBQVAvL1ZOUG96Zz09IiwgInVzZXJVaWQiOiJBd1ptUHZJa25pckQ4MWkyZkJlY0hRPT0iLCAiY3JlYXRlZCI6IjE3NTk4NzY4MTk2ODgiLCAiSVBwb29sIjpbIkFBQUFBQUFBQUFBQUFQLy9WTlBvemc9PSJdLCAiZGVhZGxpbmUiOiIxNzU5OTYzMjE5Njg4In0=' \
    - H 'Origin: https://opentip.kaspersky.com' \
    - H 'Referer: https://opentip.kaspersky.com/?tab=lookup' \
    - H 'Sec-Fetch-Dest: empty' \
    - H 'Sec-Fetch-Mode: cors' \
    - H 'Sec-Fetch-Site: same-origin' \
    - H 'Sec-GPC: 1' \
    - H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36' \
    - H 'sec-ch-ua: "Chromium";v="140", "Not=A?Brand";v="24", "Brave";v="140"' \
    - H 'sec-ch-ua-mobile: ?0' \
    - H 'sec-ch-ua-platform: "Linux"' \
    - -data-raw '{"query":"0dea6f77da9bdfd6985c3cd30c6c174d791d106ce55dd5f57a2f212ab5477c67","silent":false}'
"""


class KasperskyPlugin(Plugin):
    def __init__(self):
        pass
