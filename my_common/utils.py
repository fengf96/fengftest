# coding:utf-8

import json

from django.shortcuts import HttpResponse


def render_json(res_dict):
    return HttpResponse(json.dumps(res_dict), content_type='application/json')