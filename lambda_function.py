from urllib import request, parse
import json
from packages import packages, slides, foundations


# base url for each backend context
package_info_contexts = {
  #'disaster-resilience' :  'http://0.0.0.0:8000/disaster-resilience'
  'disaster-resilience' :   'https://service.civicpdx.org/disaster-resilience/'
}

# endpoint suffix for package info definitions at each backend repo
package_info_endpoint_url_suffix = 'sandbox/package_info/'

"""
 For each backend context defined in package_info_contexts, call the civic-sandbox/get_packages
 endpoint to fetch any package definitions located at that context, and update the local 
 copy with those package definitions.
"""
def update_packages_infos():  
  for remote_context_url_base in package_info_contexts.values():
    # formulate the url of the remote context's package definitions endpoint
    package_info_endpoint = parse.urljoin(remote_context_url_base, package_info_endpoint_url_suffix)

    with request.urlopen(package_info_endpoint) as endpoint_url:
      # fetch any packages defined at the remote context
      package_info = json.loads(endpoint_url.read().decode())
      # add any remotely-defined packages to the local copy
      packages.update(package_info['packages'])
      foundations.update(package_info['foundations'])
      slides.update(package_info['slides'])


"""
 The hander function used when the lambda url is invoked. Returns the package definitions
 dictionary in JSON format.
"""
def lambda_handler(event, context):
  # update the local package definitions with any fetched from the remote contexts
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

if __name__ == "__main__":
  lambda_handler(None, None)