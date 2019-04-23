from urllib import request, parse, error
import json
from packages import package_info
import traceback


remote_package_info_contexts = {
  #'transportation-systems' :   'http://0.0.0.0:8000/transportation-systems/',
  'transportation-systems' :    'https://service.civicpdx.org/transportation-systems/',
  #'disaster-resilience' :      'http://0.0.0.0:8000/disaster-resilience/',
  'disaster-resilience' :       'https://service.civicpdx.org/disaster-resilience/',
  #'neighborhood-development' :  'http://0.0.0.0:8000/neighborhood-development/',
  'neighborhood-development' : 'https://service.civicpdx.org/neighborhood-development/',
  #'housing-affordability' :     'http://0.0.0.0:8000/housing-affordability/',
  'housing-affordability' :    'https://service.civicpdx.org/housing-affordability/',
}

remote_package_info_endpoint_suffix = 'sandbox/package_info/'


def update_local_package_info():  
  for remote_context_url_base in remote_package_info_contexts.values():
    # formulate the url of the remote context's package definitions endpoint
    remote_package_info_endpoint = parse.urljoin(remote_context_url_base, remote_package_info_endpoint_suffix)

    try:
      with request.urlopen(remote_package_info_endpoint) as remote_endpoint_url:
        # fetch any packages defined at the remote context
        remote_package_info = json.loads(remote_endpoint_url.read().decode()) 
               
        package_info['packages'].update(remote_package_info['packages'])
        package_info['foundations'].update(remote_package_info['foundations'])
        package_info['slides'].update(remote_package_info['slides'])
    except error.HTTPError as he:
      traceback.print_exc()
    except error.URLError as ue:
      traceback.print_exc()

def lambda_handler(event, context):
  # update the local package definitions with any fetched from the remote contexts
  update_local_package_info()

  return {
    'statusCode': 200, 
    'body': package_info
  }
