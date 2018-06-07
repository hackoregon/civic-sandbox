import json
def lambda_handler(event, context):
    body = {
    'packages' : { 
        'transportation': {
          'description': 'Transportation: This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'foundations' : ['103', '105', '104'],
          'default_foundation' : '103',
          'slides' : ['102', '106'],
          'default_slide' : '106'
          },
        'affordable housing': {
          'description': 'Transportation: This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'foundations' : ['105', '104'],
          'default_foundation' : '105',
          'slides' : ['101', '102'],
          'default_slide' : '101'
          },
        'neighborhoods': {
          'description': 'Transportation: This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'foundations' : ['104'],
          'default_foundation' : '104',
          'slides' : ['101', '102', '106'],
          'default_slide' : '102'
          }
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
        '101': {
          'name': 'sweeps',
          'endpoint': 'https://0uv7y2d29i.execute-api.us-east-2.amazonaws.com/mockslide101/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ScreenGridMap',
        },
        '102': {
          'name': 'bus stops',
          'endpoint': 'https://hsqxipv6u8.execute-api.us-east-2.amazonaws.com/mockslide102/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ScatterPlotMap',
        }, 
        '106': {
          'name': 'bike lanes',
          'endpoint': 'https://cekaghbj2k.execute-api.us-east-2.amazonaws.com/mockslide106',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'PathMap',
        }   
    }, 
    'foundations': {
        '001': {
          'name': 'Property Value',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/taxlotblockgroups/',
          'description': 'Property Value: This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
          }
        },
        '103': {
          'name': 'zip codes',
          'endpoint': 'https://ctyhsin0r2.execute-api.us-east-2.amazonaws.com/mockfoundation103',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ChoroplethMap',
          'attributes': {
            'primary': {
              'field': 'happy_index',
              'name': 'average happy index rating'
            },
            'secondary': {
              'field': 'parks',
              'name': 'number of parks'
            },
          }
        },
        '104': {
          'name': 'neighborhoods',
          'endpoint': 'https://rnc45keyjk.execute-api.us-east-2.amazonaws.com/mockfoundation104',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ChoroplethMap',
          'attributes': {
            'primary': {
              'field': 'name',
              'name': 'neighborhood name'
            },
            'secondary': {
              'field': None,
              'name': None
            },
          }
        },
        '105': {
          'name': 'voter precincts',
          'endpoint': 'https://qfvf1wpc3l.execute-api.us-east-2.amazonaws.com/mockfoundation105',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ChoroplethMap',
          'attributes': {
            'primary': {
              'field': 'avg_voter_turnout_pct',
              'name': 'average voter turnout' 
            },
            'secondary': {
              'field': 'median_income',
              'name': 'median income'
            },
          }
        }, 
    }
    return {
      'statusCode': 200, 
      'body': body
      }