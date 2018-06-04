import json
def lambda_handler(event, context):
    body = {
    'packages' : { 
        'transportation': {
          'foundations' : ['103', '105', '104'],
          'default_foundation' : '103',
          'slides' : ['102', '106'],
          'default_slide' : '106'
          },
        'affordable housing': {
          'foundations' : ['105', '104'],
          'default_foundation' : '105',
          'slides' : ['101', '102'],
          'default_slide' : '101'
          },
        'neighborhoods': {
          'foundations' : ['104'],
          'default_foundation' : '104',
          'slides' : ['101', '102', '106'],
          'default_slide' : '102'
          } 
    },
    'slides': {
        '101': {
          'name': 'sweeps',
          'endpoint': 'https://0uv7y2d29i.execute-api.us-east-2.amazonaws.com/mockslide101/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'heat map',
          'attributes': {
            'primary': {
              'field': None,
              'name': None
            },
            'secondary': {
              'field': None,
              'name': None
            },
          }
        },
        '102': {
          'name': 'bus stops',
          'endpoint': 'https://hsqxipv6u8.execute-api.us-east-2.amazonaws.com/mockslide102/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'dot map',
          'attributes': {
            'primary': {
              'field': 'avg_wait',
              'name': 'average wait time'
            },
            'secondary': {
              'field': 'route',
              'name': 'bus route'
            },
          }
        }, 
        '106': {
          'name': 'bike lanes',
          'endpoint': 'https://cekaghbj2k.execute-api.us-east-2.amazonaws.com/mockslide106',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'line map',
          'attributes': {
            'primary': {
              'field': 'avg_bike_speed',
              'name': 'average bike speed'
            },
            'secondary': {
              'field': 'shape_leng',
              'name': 'length of lane'
            },
          }
        }     
    }, 
    'foundations': {
        '103': {
          'name': 'zip codes',
          'endpoint': 'https://ctyhsin0r2.execute-api.us-east-2.amazonaws.com/mockfoundation103',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'choropleth',
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
          'visualization': 'choropleth',
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
          'visualization': 'choropleth',
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
  } 
    return {
      'statusCode': 200, 
      'body': json.dumps(body)
      }