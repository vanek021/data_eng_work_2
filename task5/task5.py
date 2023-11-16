import os
import csv
import json
import pickle
import msgpack
import numpy as np

AREA_ID_FIELD = 'area_id'
AREA_NAME_FIELD = 'area_name'
REPORTING_DISTRICT_FIELD = 'reporting_district'
VICTIM_AGE_FIELD = 'victim_age'
VICTIM_SEX_FIELD = 'victim_sex'
VICTIM_DESCENT_FIELD = 'victim_descent'
PREMISE_DESC_FIELD = 'premise_description'

with open('./task5/Traffic_Collision_Data_from_2010_to_Present.csv', newline='\n', encoding='utf-8') as file:
    items = list()
    reader = csv.reader(file, delimiter=',')

    next(reader, None)

    for row in reader:
        item = {
            AREA_ID_FIELD: int(row[4]),
            AREA_NAME_FIELD: row[5],
            REPORTING_DISTRICT_FIELD: int(row[6]),
            VICTIM_AGE_FIELD: int(row[10]) if row[10] != '' else None,
            VICTIM_SEX_FIELD: row[11],
            VICTIM_DESCENT_FIELD: row[12],
            PREMISE_DESC_FIELD: row[14]
        }

        items.append(item)

    area_id_items = list(map(lambda i: i[AREA_ID_FIELD], items))
    reporting_district_items = list(map(lambda i: i[REPORTING_DISTRICT_FIELD], items))
    age_items = list(filter(lambda y: y is not None, map(lambda x: x[VICTIM_AGE_FIELD], items)))

    stat = {
        AREA_ID_FIELD: {
            'min': min(area_id_items),
            'max': max(area_id_items),
            'sum': sum(area_id_items),
            'avg': np.average(area_id_items),
            'st_dev': np.std(area_id_items)
        },
        REPORTING_DISTRICT_FIELD: {
            'min': min(reporting_district_items),
            'max': max(reporting_district_items),
            'sum': sum(reporting_district_items),
            'avg': np.average(reporting_district_items),
            'st_dev': np.std(reporting_district_items)
        },
        VICTIM_AGE_FIELD: {
            'min': min(age_items),
            'max': max(age_items),
            'sum': sum(age_items),
            'avg': np.average(age_items),
            'st_dev': np.std(age_items)
        },
        AREA_NAME_FIELD: {},
        VICTIM_SEX_FIELD: {},
        VICTIM_DESCENT_FIELD: {},
        PREMISE_DESC_FIELD: {}
    }

    area_name_freq = {}
    victim_sex_freq = {}
    victim_descent_freq = {}
    premise_desc_freq = {}

    for item in items:
        stat[AREA_NAME_FIELD][item[AREA_NAME_FIELD]] = stat[AREA_NAME_FIELD].get(item[AREA_NAME_FIELD], 0) + 1
        stat[VICTIM_SEX_FIELD][item[VICTIM_SEX_FIELD]] = stat[VICTIM_SEX_FIELD].get(item[VICTIM_SEX_FIELD], 0) + 1
        stat[VICTIM_DESCENT_FIELD][item[VICTIM_DESCENT_FIELD]] = stat[VICTIM_DESCENT_FIELD].get(item[VICTIM_DESCENT_FIELD], 0) + 1
        stat[PREMISE_DESC_FIELD][item[PREMISE_DESC_FIELD]] = stat[PREMISE_DESC_FIELD].get(item[PREMISE_DESC_FIELD], 0) + 1

    # Результат
    with open("./task5/stat.json", "w") as r_json:
        r_json.write(json.dumps(stat))

    # Данные json
    with open("./task5/data.json", "w") as r_json:
        r_json.write(json.dumps(items))

    # Данные pkl
    with open("./task5/data.pkl", "wb") as r_p:
        r_p.write(pickle.dumps(items))

    # Данные msgpack
    with open("./task5/data.msgpack", "wb") as r_msgpack:
        r_msgpack.write(msgpack.dumps(items))

    # Данные CSV - исходные

    # Размеры
    print(f"json     = {os.path.getsize('./task5/data.json')}")
    print(f"msgpack  = {os.path.getsize('./task5/data.msgpack')}")
    print(f"pkl      = {os.path.getsize('./task5/data.pkl')}")
    print(f"csv      = {os.path.getsize('./task5/Traffic_Collision_Data_from_2010_to_Present.csv')}")

    #json     = 81450671
    #msgpack  = 60204230
    #pkl      = 24696988
    #csv      = 98628283