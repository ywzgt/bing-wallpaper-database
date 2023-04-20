#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import os

import bing_image


def main():
    country = ['zh-CN','en-US','ja-JP','fr-FR','de-DE','es-ES','en-GB','it-IT','pt-BR']
    for i in country:
        data = bing_image.get_json_data(i)
        date = data.get('end_date')

        dirname = 'json' + '/' + i.lower() + '/' + date[0:4] + '/' + date[4:6]
        name = date[6:8]
        filename = dirname + '/' + name + '.json'
        os.makedirs(dirname, exist_ok=True)

        with open(filename, 'w') as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()



"""
from datetime import datetime

        date = datetime.strptime(data.get('date'), '%Y-%m-%d')

        dirname = i.lower() + '/' + date.strftime("%Y/%m")
        name = date.strftime("%d")
"""
