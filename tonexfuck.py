import requests

cookies = {
    '_ym_d': '1654265136',
    '_ym_uid': '1654265136686751528',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    'XSRF-TOKEN': 'eyJpdiI6IjVYMnU0c2FSOXM0MDNtcURpMDVaNGc9PSIsInZhbHVlIjoiTGtZSm1nMVB1U2hhZXpmQ0xIY0w5cWt4NFFLRFdQTVE4ZkR2SzVoTEx4YVJCem5hSkpOWXp0TWdEU1diNXIwemV0azNCNnhqWVh3SkdYbXBPRlpvQzNobXJrZEZ6YnBPWVlGdVlsNzY2MS80WTVkUEgvVStOV2FRSityUnByQW0iLCJtYWMiOiJiNTA0OWM2ZTMwYzRiYTI1MzUyNTNkMTIzNDE5OTY4YTc0NzQ2MjAyNzU2NjY3YWMzMDA0MWUxZGZlZjY5NGIzIiwidGFnIjoiIn0%3D',
    'tonex_session': 'eyJpdiI6IkpsNVhZY1A2SnVMMEpjWG9sNTMrK3c9PSIsInZhbHVlIjoiNUJaSkY5ZnAvQUJpMDZUcUtaUkQ4WTZpeVdyNmhhMGhhMDUvRHRCSk5HWU1HSEJSOGNBYlVGL240VTVHWVRuSFh3TlNEWG1Dd2d6ZDdidklXakFkVTIwZWFTUytHSUw1REhUZ2Z3N1FQSjdhVW1UTERSVXJyUnVNYm1jV2tIalMiLCJtYWMiOiI1NGFjNDBlOGI0MGIzMDA1NTAyNzlkM2E4YmZlMWZjNDY1MGIwNDU4MzZhNWQ1ZjA5ZmY4NTZmMjBhNDJlNjkzIiwidGFnIjoiIn0%3D',
}

headers = {
    'Host': 'tonex.app',
    # 'Content-Length': '47',
    'Sec-Ch-Ua': '"-Not.A/Brand";v="8", "Chromium";v="102"',
    'Accept': 'application/json',
    'X-Xsrf-Token': 'eyJpdiI6IjVYMnU0c2FSOXM0MDNtcURpMDVaNGc9PSIsInZhbHVlIjoiTGtZSm1nMVB1U2hhZXpmQ0xIY0w5cWt4NFFLRFdQTVE4ZkR2SzVoTEx4YVJCem5hSkpOWXp0TWdEU1diNXIwemV0azNCNnhqWVh3SkdYbXBPRlpvQzNobXJrZEZ6YnBPWVlGdVlsNzY2MS80WTVkUEgvVStOV2FRSityUnByQW0iLCJtYWMiOiJiNTA0OWM2ZTMwYzRiYTI1MzUyNTNkMTIzNDE5OTY4YTc0NzQ2MjAyNzU2NjY3YWMzMDA0MWUxZGZlZjY5NGIzIiwidGFnIjoiIn0=',
    'Sec-Ch-Ua-Mobile': '?0',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Origin': 'https://tonex.app',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://tonex.app/@laeda1984',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'Cookie': '_ym_d=1654265136; _ym_uid=1654265136686751528; _ym_isad=2; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6IjVYMnU0c2FSOXM0MDNtcURpMDVaNGc9PSIsInZhbHVlIjoiTGtZSm1nMVB1U2hhZXpmQ0xIY0w5cWt4NFFLRFdQTVE4ZkR2SzVoTEx4YVJCem5hSkpOWXp0TWdEU1diNXIwemV0azNCNnhqWVh3SkdYbXBPRlpvQzNobXJrZEZ6YnBPWVlGdVlsNzY2MS80WTVkUEgvVStOV2FRSityUnByQW0iLCJtYWMiOiJiNTA0OWM2ZTMwYzRiYTI1MzUyNTNkMTIzNDE5OTY4YTc0NzQ2MjAyNzU2NjY3YWMzMDA0MWUxZGZlZjY5NGIzIiwidGFnIjoiIn0%3D; tonex_session=eyJpdiI6IkpsNVhZY1A2SnVMMEpjWG9sNTMrK3c9PSIsInZhbHVlIjoiNUJaSkY5ZnAvQUJpMDZUcUtaUkQ4WTZpeVdyNmhhMGhhMDUvRHRCSk5HWU1HSEJSOGNBYlVGL240VTVHWVRuSFh3TlNEWG1Dd2d6ZDdidklXakFkVTIwZWFTUytHSUw1REhUZ2Z3N1FQSjdhVW1UTERSVXJyUnVNYm1jV2tIalMiLCJtYWMiOiI1NGFjNDBlOGI0MGIzMDA1NTAyNzlkM2E4YmZlMWZjNDY1MGIwNDU4MzZhNWQ1ZjA5ZmY4NTZmMjBhNDJlNjkzIiwidGFnIjoiIn0%3D',
}

json_data = {
    'uuid': 'ce755b4f-c386-4759-ad0f-c5157f669a12',
}

response = requests.post('https://tonex.app/api/v1/post/viewed', cookies=cookies, headers=headers, json=json_data, verify=False)