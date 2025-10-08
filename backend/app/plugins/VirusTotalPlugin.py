from future.plugins import Plugin
import requests
import os


class VirusTotalPlugin(Plugin):
    def __init__(self):
        self.lol = "lol"

    def lookup(self, hash: str):
        api_key = os.getenv("VIRUSTOTAL_API_KEY")
        url = f"https://www.virustotal.com/api/v3/files/{hash}"
        response = requests.get(url, headers={"x-apikey": api_key})
        return response.json()

# https://www.virustotal.com/gui/file/631b8003b56f1381af44cf157d7c08aaa8f958909a3feab4f1b245eeca7427a1


"""
{
	"data": {
	"id": "0dea6f77da9bdfd6985c3cd30c6c174d791d106ce55dd5f57a2f212ab5477c67",
	"type": "file",
	"links": {
		"self": "https://www.virustotal.com/api/v3/files/0dea6f77da9bdfd6985c3cd30c6c174d791d106ce55dd5f57a2f212ab5477c67"
	},
	"attributes": {
		"tlsh": "T116F0A46112332FD18804C8BBC6810090E1931270D9EEF4BAFFE23B45BD8A881BD516E2",
		"type_description": "Text",
		"tags": ["text"],
		"last_modification_date": 1726643066,
		"meaningful_name": "FIN7_IOCs_IPs.txt",
		"magic": "ASCII text",
		"sha256": "0dea6f77da9bdfd6985c3cd30c6c174d791d106ce55dd5f57a2f212ab5477c67",
		"first_submission_date": 1726635851,
		"type_tag": "text",
		"reputation": 0,
		"magika": "TXT",
		"size": 612,
		"ssdeep": "12:M7PPpvyr9gq0K37NLrjdFVgRCqbshdU+KJZJnUicL4HVN:MNQ9gcrNLXDdU+cZJnUCHVN",
		"md5": "6406484fbd7c8d985e40365d3c4e2d31",
		"type_extension": "txt",
		"last_submission_date": 1726636105,
		"times_submitted": 3,
		"unique_sources": 2,
		"last_analysis_date": 1726635851,
		"type_tags": ["text"],
		"last_analysis_stats": {
			"malicious": 0,
			"suspicious": 0,
			"undetected": 63,
			"harmless": 0,
			"timeout": 0,
			"confirmed-timeout": 0,
			"failure": 0,
			"type-unsupported": 14
		},
		"last_analysis_results": {
			"Bkav": {
				"method": "blacklist",
				"engine_name": "Bkav",
				"engine_version": "2.0.0.1",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"Lionic": {
				"method": "blacklist",
				"engine_name": "Lionic",
				"engine_version": "8.16",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
				"tehtris": {
				"method": "blacklist",
				"engine_name": "tehtris",
				"engine_version": None, "engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
				"MicroWorld-eScan": {
				"method": "blacklist",
				"engine_name": "MicroWorld-eScan",
				"engine_version": "14.0.409.0",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
				"ClamAV": {
				"method": "blacklist",
				"engine_name": "ClamAV",
				"engine_version": "1.4.1.0",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"CTX": {
				"method": "blacklist",
				"engine_name": "CTX",
				"engine_version": "2024.8.29.1",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"CAT-QuickHeal": {
				"method": "blacklist",
				"engine_name": "CAT-QuickHeal",
				"engine_version": "22.00",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"Skyhigh": {
				"method": "blacklist",
				"engine_name": "Skyhigh",
				"engine_version": "v2021.2.0+4045",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"ALYac": {
				"method": "blacklist",
				"engine_name": "ALYac",
				"engine_version": "2.0.0.10",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"Malwarebytes": {
				"method": "blacklist",
				"engine_name": "Malwarebytes",
				"engine_version": "4.5.5.54",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"Zillya": {
				"method": "blacklist",
				"engine_name": "Zillya",
				"engine_version": "2.0.0.5196",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"Sangfor": {
				"method": "blacklist",
				"engine_name": "Sangfor",
				"engine_version": "2.25.10.0",
				"engine_update": "20240912",
				"category": "undetected",
				"result": None
			},
			"CrowdStrike": {
				"method": "blacklist",
				"engine_name": "CrowdStrike",
				"engine_version": "1.0",
				"engine_update": "20230417",
				"category": "undetected",
				"result": None
			},
			"K7GW": {
				"method": "blacklist",
				"engine_name": "K7GW",
				"engine_version": "12.189.53300",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"K7AntiVirus": {
				"method": "blacklist",
				"engine_name": "K7AntiVirus",
				"engine_version": "12.189.53300",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"Arcabit": {
				"method": "blacklist",
				"engine_name": "Arcabit",
				"engine_version": "2022.0.0.18",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"Baidu": {
				"method": "blacklist",
				"engine_name": "Baidu",
				"engine_version": "1.0.0.2",
				"engine_update": "20190318",
				"category": "undetected",
				"result": None
			},
			"VirIT": {
				"method": "blacklist",
				"engine_name": "VirIT",
				"engine_version": "9.5.789",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"Symantec": {
				"method": "blacklist",
				"engine_name": "Symantec",
				"engine_version": "1.22.0.0",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"ESET-NOD32": {
				"method": "blacklist",
				"engine_name": "ESET-NOD32",
				"engine_version": "29907",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"TrendMicro-HouseCall": {
				"method": "blacklist",
				"engine_name": "TrendMicro-HouseCall",
				"engine_version": "10.0.0.1040",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"Avast": {
				"method": "blacklist",
				"engine_name": "Avast",
				"engine_version": "23.9.8494.0",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"Cynet": {
				"method": "blacklist",
				"engine_name": "Cynet",
				"engine_version": "4.0.1.1",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"Kaspersky": {
				"method": "blacklist",
				"engine_name": "Kaspersky",
				"engine_version": "22.0.1.28",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"BitDefender": {
				"method": "blacklist",
				"engine_name": "BitDefender",
				"engine_version": "7.2",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"NANO-Antivirus": {
				"method": "blacklist",
				"engine_name": "NANO-Antivirus",
				"engine_version": "1.0.146.25796",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"ViRobot": {
				"method": "blacklist",
				"engine_name": "ViRobot",
				"engine_version": "2014.3.20.0",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"Tencent": {
				"method": "blacklist",
				"engine_name": "Tencent",
				"engine_version": "1.0.0.1",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"Emsisoft": {
				"method": "blacklist",
				"engine_name": "Emsisoft",
				"engine_version": "2024.1.0.53752",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"F-Secure": {
				"method": "blacklist",
				"engine_name": "F-Secure",
				"engine_version": "18.10.1547.307",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"DrWeb": {
				"method": "blacklist",
				"engine_name": "DrWeb",
				"engine_version": "7.0.65.5230",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"VIPRE": {
				"method": "blacklist",
				"engine_name": "VIPRE",
				"engine_version": "6.0.0.35",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"TrendMicro": {
				"method": "blacklist",
				"engine_name": "TrendMicro",
				"engine_version": "11.0.0.1006",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"CMC": {
				"method": "blacklist",
				"engine_name": "CMC",
				"engine_version": "2.4.2022.1",
				"engine_update": "20240915",
				"category": "undetected",
				"result": None
			},
			"Sophos": {
				"method": "blacklist",
				"engine_name": "Sophos",
				"engine_version": "2.5.5.0",
				"engine_update": "20240913",
				"category": "undetected",
				"result": None
			},
			"Ikarus": {
				"method": "blacklist",
				"engine_name": "Ikarus",
				"engine_version": "6.3.23.0",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
				"FireEye": {
				"method": "blacklist",
				"engine_name": "FireEye",
				"engine_version": "35.47.0.0",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"Jiangmin": {
				"method": "blacklist",
				"engine_name": "Jiangmin",
				"engine_version": "16.0.100",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
				"Varist": {
				"method": "blacklist",
				"engine_name": "Varist",
				"engine_version": "6.6.1.3",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"Avira": {
				"method": "blacklist",
				"engine_name": "Avira",
				"engine_version": "8.3.3.20",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"Antiy-AVL": {
				"method": "blacklist",
				"engine_name": "Antiy-AVL",
				"engine_version": "3.0",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"Kingsoft": {
				"method": "blacklist",
				"engine_name": "Kingsoft",
				"engine_version": "None",
				"engine_update": "20240725",
				"category": "undetected",
				"result": None
			},
			"Gridinsoft": {
				"method": "blacklist",
				"engine_name": "Gridinsoft",
				"engine_version": "1.0.188.174",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"Xcitium": {
				"method": "blacklist",
				"engine_name": "Xcitium",
				"engine_version": "37055",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"Microsoft": {
				"method": "blacklist",
				"engine_name": "Microsoft",
				"engine_version": "1.1.24080.9",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"SUPERAntiSpyware": {
				"method": "blacklist",
				"engine_name": "SUPERAntiSpyware",
				"engine_version": "5.6.0.1032",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"ZoneAlarm": {
				"method": "blacklist",
				"engine_name": "ZoneAlarm",
				"engine_version": "1.0",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"GData": {
				"method": "blacklist",
				"engine_name": "GData",
				"engine_version": "A:25.38908B:27.37496",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"Google": {
				"method": "blacklist",
				"engine_name": "Google",
				"engine_version": "1726632027",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"AhnLab-V3": {
				"method": "blacklist",
				"engine_name": "AhnLab-V3",
				"engine_version": "3.26.1.10507",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"Acronis": {
				"method": "blacklist",
				"engine_name": "Acronis",
				"engine_version": "1.2.0.121",
				"engine_update": "20240328",
				"category": "undetected",
				"result": None
			},
			"McAfee": {
				"method": "blacklist",
				"engine_name": "McAfee",
				"engine_version": "6.0.6.653",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"TACHYON": {
				"method": "blacklist",
				"engine_name": "TACHYON",
				"engine_version": "2024-09-18.01",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"VBA32": {
				"method": "blacklist",
				"engine_name": "VBA32",
				"engine_version": "5.0.0",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"Zoner": {
				"method": "blacklist",
				"engine_name": "Zoner",
				"engine_version": "2.2.2.0",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"Rising": {
				"method": "blacklist",
				"engine_name": "Rising",
				"engine_version": "25.0.0.28",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"Yandex": {
				"method": "blacklist",
				"engine_name": "Yandex",
				"engine_version": "5.5.2.24",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"huorong": {
				"method": "blacklist",
				"engine_name": "huorong",
				"engine_version": "089e4ee:089e4ee:7aa142f:7aa142f",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"MaxSecure": {
				"method": "blacklist",
				"engine_name": "MaxSecure",
				"engine_version": "1.0.0.1",
				"engine_update": "20240916",
				"category": "undetected",
				"result": None
			},
			"Fortinet": {
				"method": "blacklist",
				"engine_name": "Fortinet",
				"engine_version": "None",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"AVG": {
				"method": "blacklist",
				"engine_name": "AVG",
				"engine_version": "23.9.8494.0",
				"engine_update": "20240918",
				"category": "undetected",
				"result": None
			},
			"Panda": {
				"method": "blacklist",
				"engine_name": "Panda",
				"engine_version": "4.6.4.2",
				"engine_update": "20240917",
				"category": "undetected",
				"result": None
			},
			"alibabacloud": {
				"method": "blacklist",
				"engine_name": "alibabacloud",
				"engine_version": "2.2.0",
				"engine_update": "20240910",
				"category": "undetected",
				"result": None
			},
			"McAfeeD": {
				"method": "blacklist",
				"engine_name": "McAfeeD",
				"engine_version": "1.2.0.7977",
				"engine_update": "20240918",
				"category": "type-unsupported",
				"result": None
			},
			"Avast-Mobile": {
				"method": "blacklist",
				"engine_name": "Avast-Mobile",
				"engine_version": "240917-00",
				"engine_update": "20240917",
				"category": "type-unsupported",
				"result": None
			},
			"SymantecMobileInsight": {
				"method": "blacklist",
				"engine_name": "SymantecMobileInsight",
				"engine_version": "2.0",
				"engine_update": "20240103",
				"category": "type-unsupported",
				"result": None
			},
			"BitDefenderFalx": {
				"method": "blacklist",
				"engine_name": "BitDefenderFalx",
				"engine_version": "2.0.936",
				"engine_update": "20240128",
				"category": "type-unsupported",
				"result": None
			},
			"Elastic": {
				"method": "blacklist",
				"engine_name": "Elastic",
				"engine_version": "4.0.163",
				"engine_update": "20240917",
				"category": "type-unsupported",
				"result": None
			},
			"DeepInstinct": {
				"method": "blacklist",
				"engine_name": "DeepInstinct",
				"engine_version": "5.0.0.8",
				"engine_update": "20240905",
				"category": "type-unsupported",
				"result": None
			},
			"APEX": {
				"method": "blacklist",
				"engine_name": "APEX",
				"engine_version": "6.576",
				"engine_update": "20240916",
				"category": "type-unsupported",
				"result": None
			},
			"Paloalto": {
				"method": "blacklist",
				"engine_name": "Paloalto",
				"engine_version": "0.9.0.1003",
				"engine_update": "20240918",
				"category": "type-unsupported",
				"result": None
			},
			"Trapmine": {
				"method": "blacklist",
				"engine_name": "Trapmine",
				"engine_version": "4.0.16.213",
				"engine_update": "20240826",
				"category": "type-unsupported",
				"result": None
			},
			"Alibaba": {
				"method": "blacklist",
				"engine_name": "Alibaba",
				"engine_version": "0.3.0.5",
				"engine_update": "20190527",
				"category": "type-unsupported",
				"result": None
			},
				"Webroot": {
				"method": "blacklist",
				"engine_name": "Webroot",
				"engine_version": "1.0.0.403",
				"engine_update": "20240918",
				"category": "type-unsupported",
				"result": None
			},
				"Cylance": {
				"method": "blacklist",
				"engine_name": "Cylance",
				"engine_version": "3.0.0.0",
				"engine_update": "20240905",
				"category": "type-unsupported",
				"result": None
			},
			"SentinelOne": {
				"method": "blacklist",
				"engine_name": "SentinelOne",
				"engine_version": "24.2.1.1",
				"engine_update": "20240417",
				"category": "type-unsupported",
				"result": None
			},
			"Trustlook": {
				"method": "blacklist",
				"engine_name": "Trustlook",
				"engine_version": "1.0",
				"engine_update": "20240918",
				"category": "type-unsupported",
				"result": None
			}
		},
		"total_votes": {
			"harmless": 0, "malicious": 0
		},
		"sha1": "4ab308adea689549080c50be816bf96baad9411e",
		"trid": [
			{
				"file_type": "file seems to be plain text/ASCII",
				"probability": 0.0
			}
		],
		"names": [
			"FIN7_IOCs_IPs.txt"
		]
	}
	}
}
"""
