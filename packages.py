"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  Old "un-decentralized" style of locating all package definitions, for all packages for all backend repos
  in one monolithic dictionary inside the civic-sandbox's lambda_function endpoint. This has been replaced
  by the new decentralized style of locating package defitions for each backend repo in the respective 
  backend repo's 'sandbox/package_info/' endpoint. While the lamda_function's location is still at the 
  same place, it now fetches each backend repo's package definitions from the backend repo's 
  'sandbox/package_info/' endpoint in a transparent manner.    
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
 Package Definitions 
"""
packages = {  
}


"""
 Slides: 
 Used in formulating the package definitions
"""
slides = { 
}

"""
 Foundations:
 Used in formulating the package definitions
"""
foundations = {
}

package_info = {
    'packages' : packages,
    'slides' : slides,
    'foundations' : foundations
    }