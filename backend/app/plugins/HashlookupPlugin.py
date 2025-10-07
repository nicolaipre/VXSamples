from future.plugins import Plugin

# https://circl.lu/services/hashlookup/

# curl -X 'GET' 'https://hashlookup.circl.lu/info' -H 'accept: application/json'

# curl -X 'GET' 'https://hashlookup.circl.lu/lookup/md5/8ED4B4ED952526D89899E723F3488DE4' -H 'accept: application/json'

# curl -X 'GET'   'https://hashlookup.circl.lu/lookup/sha1/FFFFFDAC1B1B4C513896C805C2C698D9688BE69F'   -H 'accept: application/json' | jq .

# curl -s -X 'GET'   'https://hashlookup.circl.lu/lookup/sha256/301c9ec7a9aadee4d745e8fd4fa659dafbbcc6b75b9ff491d14cbbdd840814e9'   -H 'accept: application/json' | jq

# supports bulk search


# Aka Hashlookup

# https://hashlookup.io/


class CIRCLPlugin(Plugin):
    def __init__(self):
        pass
