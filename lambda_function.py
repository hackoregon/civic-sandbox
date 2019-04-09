from urllib import request, parse, error
import json
from packages import packages, foundations, slides


# base url for each backend context
package_info_contexts = {
  'disaster-resilience' :     'https://service.civicpdx.org/disaster-resilience/',
#  'disaster-resilience' :    'http://0.0.0.0:8000/disaster-resilience/',
#  'transportation-systems' : 'https://service.civicpdx.org/transportation-systems/',
#  'transportation-systems' :  'http://0.0.0.0:8000/transportation-systems/',  
}

# endpoint suffix for package info definitions at each backend repo
package_info_endpoint_url_suffix = 'sandbox/packages/'

# For each backend context defined in package_info_contexts, call the civic-sandbox/get_packages
# endpoint and update the local copy with any package definitions fetched from that remote context.
def update_packages_infos():  
  for remote_context_url_base in package_info_contexts.values():
    # contruct the url of the remote context's package definitions endpoint
    package_info_endpoint = parse.urljoin(remote_context_url_base, package_info_endpoint_url_suffix)

    try:
      with request.urlopen(package_info_endpoint) as endpoint_url:
        # fetch any packages defined at the remote context
        package_info = json.loads(endpoint_url.read().decode())
        # add any remotely-defined packages to the local copy
        packages.update(package_info['packages'])
        foundations.update(package_info['foundations'])
        slides.update(package_info['slides'])      
    except error.HTTPError as he:
      print(he.msg)
      if he.code == 404:  # no response from package_info_endpoint        
        pass
    except error.URLError as ue:        
        print(ue.reason)  # some other error from package_info_endpoint, e.g. connection refused        


# The hander function used when the lambda url is invoked. Returns the package definitions
# dictionary in JSON format.
def lambda_handler(event, context):
  update_packages_infos()

  body = {
    'packages' : packages,
    'slides': slides, 
    'foundations': foundations,
  }

  return {
    'statusCode': 200, 
    'body': body
  }
