import json
def lambda_handler(event, context):
    body = {
    'packages' : { 
        'Greenspace': {
          'description': 'View of trees, parks, gardens, trails, and greenways per neighborhood.',
          'foundations' : ['007'],
          'default_foundation' : '007',
          'slides' : ['003', '004', '005'],
          'default_slide' : ['003', '004']
          },
        'Food Access': {
          'description': 'View of grocery locations, community gardens, and transit stops per neighborhood.',
          'foundations' : ['007'],
          'default_foundation' : '007',
          'slides' : ['009', '010', '005'],
          'default_slide' : '010'
          },
        'Sweeps': {
          'description': 'View of reports of camps, camp sweeps, and household data per neighborhood.',
          'foundations' : ['007'],
          'default_foundation' : '007',
          'slides' : ['012', '013', '011', '003', '004'],
          'default_slide' : ['012', '013']
          },
    },
    'slides': {
        '001': {
          'name': 'bike parking',
          'endpoint': 'http://service.civicpdx.org/neighborhood-development/sandbox/slides/bikeparking/',
          'description': 'Bike Parking: This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ScatterPlotMap',
        },
        '002': {
          'name': 'bike lanes',
          'endpoint': 'http://service.civicpdx.org/neighborhood-development/sandbox/slides/bikelanes/',
          'description': 'Bike Lanes: This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'PathMap',
        }, 
        '003': {
          'name': 'parks',
          'endpoint': 'http://service.civicpdx.org/neighborhood-development/sandbox/slides/parks/',
          'description': 'Parks: This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'PolygonPlotMap',
        },
        '004': {
          'name': 'multi-use trails',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/multiusetrails/',
          'description': 'Multi-use Trails: This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'PathMap',
        },    
        '005': {
          'name': 'community gardens',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/communitygardens/',
          'description': 'Community Gardens: This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'SmallPolygonMap',
        },    
        '008': {
          'name': 'bike greenways',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/bikegreenways/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'PathMap',
        }, 
        '009': {
          'name': 'rail stops',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/railstops/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ScatterPlotMap',
        }, 
        '010': {
          'name': 'grocery stores',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/retailgrocers/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ScatterPlotMap',
        },
        '011': {
          'name': 'demolitions',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/retailgrocers/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ScatterPlotMap',
        },
        '012': {
          'name': 'camp sweeps',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/campsweeps/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ScreenGridMap',
        },
        '013': {
          'name': 'camp reports',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/campreports/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ScatterPlotMap',
        },
    }, 
    'foundations': {
        '006': {
          'name': 'Property Value',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/taxlotblockgroups/',
          'description': 'Property Value: This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '007': {
          'name': 'Total Population',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/population/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
    },
 }
    return {
      'statusCode': 200, 
      'body': body
      }