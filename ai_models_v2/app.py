# import requests
# import json
# from time import sleep
# import os
# from model_parser import ModelParser
# # from ferris_cli.v2.services.config import Consul
#
print("bora executing")
# 
# headers = {
#     'Authorization': 'Token 254bee43c2f2a16fdf32c8620ee3914a4b294c93',
# }
#
# next = "https://api.replicate.com/v1/models"
#
# print("before while")
# while next:
#     response = requests.get(next, headers=headers)
#
#     dc = response.json()
#     next = dc['next']
#
#     for model in dc['results']:
#         try:
#             input_form_params = ModelParser().extract_prediction_endpoint_parameters(
#                 model['latest_version']['openapi_schema'])
#
#             model_data = {
#                 "cover_image_url": model.get("cover_image_url", ""),
#                 "created_at": model.get("created_at", ""),
#                 "description": model.get("description", ""),
#                 "github_url": model.get("github_url", ""),
#                 "input_params": input_form_params,
#                 "license_url": model.get("license_url", ""),
#                 "name": model.get("name", ""),
#                 "owner": model.get("owner", ""),
#                 "url": model.get("url", ""),
#                 "visibility": model.get("visibility", "")
#             }
#
#             print(model_data)
#             Consul().put_item(f"ai_models/{model['name']}", json.dumps(model_data))
#
#         except Exception as e:
#             print(e)
#             pass
#
#     sleep(5)
# print("after while")
