from urllib import request, parse
import json
import package_info as local_package_info


remote_package_info_contexts = {
  #'disaster-resilience' :  'http://0.0.0.0:8000/disaster-resilience'
  'disaster-resilience' :   'https://service.civicpdx.org/disaster-resilience/'
}

remote_package_info_endpoint_suffix = 'sandbox/package_info/'


def update_local_package_info():  
  for remote_context_url_base in remote_package_info_contexts.values():
    # formulate the url of the remote context's package definitions endpoint
    remote_package_info_endpoint = parse.urljoin(remote_context_url_base, remote_package_info_endpoint_suffix)

    with request.urlopen(remote_package_info_endpoint) as remote_endpoint_url:
      # fetch any packages defined at the remote context
      remote_package_info = json.loads(remote_endpoint_url.read().decode())
      # add any remotely-defined packages to the local copy
      local_package_info.packages.update(remote_package_info['packages'])
      local_package_info.foundations.update(remote_package_info['foundations'])
      local_package_info.slides.update(remote_package_info['slides'])


def lambda_handler(event, context):
  # update the local package definitions with any fetched from the remote contexts
  update_local_package_info()

  body = {
    'packages' : local_package_info.packages,
    'slides': local_package_info.slides, 
    'foundations': local_package_info.foundations,
  }

  return {
    'statusCode': 200, 
    'body': body
  }
