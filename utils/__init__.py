#coding=utf8
import json
from django.core.serializers.json import DjangoJSONEncoder
def convertjson(result):
    try:
        result =  json.dumps(result, ensure_ascii=False, separators=(',',':'), cls=DjangoJSONEncoder)
    except Exception as e:
        print(e)
    return result