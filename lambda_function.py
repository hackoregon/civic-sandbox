from urllib import request, parse
import json
import package_info as local_package_info_file


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
def update_local_packge_info_file():  
  for remote_context_url_base in package_info_contexts.values():
    # formulate the url of the remote context's package definitions endpoint
    package_info_endpoint = parse.urljoin(remote_context_url_base, package_info_endpoint_url_suffix)

    with request.urlopen(package_info_endpoint) as endpoint_url:
      # fetch any packages defined at the remote context
      remote_package_info = json.loads(endpoint_url.read().decode())
      # add any remotely-defined packages to the local copy
      local_package_info_file.packages.update(remote_package_info['packages'])
      local_package_info_file.foundations.update(remote_package_info['foundations'])
      local_package_info_file.slides.update(remote_package_info['slides'])


"""
 The hander function used when the lambda url is invoked. Returns the package definitions
 dictionary in JSON format.
"""
def lambda_handler(event, context):
  # update the local package definitions with any fetched from the remote contexts
  update_local_packge_info_file()

  body = {
    'packages' : local_package_info_file.packages,
    'slides': local_package_info_file.slides, 
    'foundations': local_package_info_file.foundations,
  }

  return {
    'statusCode': 200, 
    'body': body
  }

if __name__ == "__main__":
  lambda_handler(None, None)