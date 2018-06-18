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
          'foundations' : ['028'],
          'default_foundation' : '028',
          'slides' : ['009', '010', '005', '014'],
          'default_slide' : '010'
          },
        'Sweeps': {
          'description': 'View of reports of camps, camp sweeps, and household data per neighborhood.',
          'foundations' : ['007', '024', '025', '026','027'],
          'default_foundation' : '007',
          'slides' : ['012', '013', '011', '003', '004'],
          'default_slide' : ['012', '013']
          },
        'Bikes': {
          'description': 'View of daily bike estimates bike counts, bike routes, greenways, and multiuse trails per neighborhood',
          'foundations' : ['007'],
          'default_foundation' : '007',
          'slides' : ['001', '002', '008', '035', '036'],
          'default_slide' : ['012', '013']
          },
        'Disaster Resilience': {
          'description': 'description. description. description.',
          'foundations' : ['029', '030', '033', '034'],
          'default_foundation' : '029',
          'slides' : ['016'],
          'default_slide' : ['016']
          },
        'Placeholder': {
          'description': 'for slides and foundations not yet in defined packages',
          'foundations' : ['006'],
          'default_foundation' : '007',
          'slides' : ['016',  '017'],
          'default_slide' : ['016']
          },
        'Evictions': {
          'description': 'Eviction, rent, income, and property values by census blockgroup.',
          'foundations' : ['018', '019', '020', '021', '022'],
          'default_foundation' : '018',
          'slides' : ['014',  '009', '011'],
          'default_slide' : ['011']
          },
        'Voters': {
          'description': 'Voters by age.',
          'foundations' : ['037', '038', '038', '040', '041'],
          'default_foundation' : '037',
          'slides' : ['009',  '004', '008', '002'],
          'default_slide' : []
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
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/demolitions/',
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
        '014': {
          'name': 'bus stops',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/busstops/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ScatterPlotMap',
        },
        '016': {
          'name': 'points of interest',
          'endpoint':'http://service.civicpdx.org/disaster-resilience/sandbox/slides/poi/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'IconMap',
        },
        '017': {
          'name': 'Building Permits',
          'endpoint':'http://service.civicpdx.org/housing-affordability/sandbox/slides/permits/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ScreenGridMap',
        },
        '031': {
          'name': 'Safety Hotline',
          'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/slides/safetyhotline/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ScatterPlotMap',
        },
        '032': {
          'name': 'Crashes',
          'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/slides/crashes/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ScatterPlotMap',
        },
        '035': {
          'name': 'Bike Counts',
          'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/slides/bikecounts/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description.',
          'visualization': 'ScatterPlotMap',
        },
        '036': {
          'name': 'Bike Estimates',
          'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/slides/bikeestimates/',
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
        '015': {
          'name': 'Housholds with Children',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/under18/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '018': {
          'name': 'Median Houshold Income',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/income/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '019': {
          'name': 'Median Gross Rent',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/grossrent/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '020': {
          'name': 'Evictions',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/evictions/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '021': {
          'name': 'Renter Occupied Households',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/renteroccupied/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '022': {
          'name': 'Rent Burden',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/rentburden/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '024': {
          'name': 'Households with Children',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/under18/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '025': {
          'name': 'Households with Seniors',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/over65/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '026': {
          'name': 'Housholders Living Alone',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/livingalone/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '027': {
          'name': 'Owner Occupied Housholds',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/owneroccupied/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
         },
        '028': {
          'name': 'Percent Renter Occupied',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/pctrenteroccupied/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '029': {
          'name': 'Shaking Intensity',
          'endpoint':'http://service.civicpdx.org/disaster-resilience/sandbox/foundations/shaking/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '030': {
          'name': 'Wet Season Mean Deformation Intensity',
          'endpoint':'http://service.civicpdx.org/disaster-resilience/sandbox/foundations/liquefaction/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '033': {
          'name': 'Dry Season Mean Deformation Intensity',
          'endpoint':'http://service.civicpdx.org/disaster-resilience/sandbox/foundations/landslide/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '034': {
          'name': 'Census Reponse Rate',
          'endpoint':'http://service.civicpdx.org/disaster-resilience/sandbox/foundations/censusresponse/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '037': {
          'name': 'Voters 18 to 25',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/voters18to25/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '038': {
          'name': 'Voters 26 to 32',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/voters26to32/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '039': {
          'name': 'Voters 33 to 39',
          'endpoint':'http://service.civicpdx.org/disaster-resilience/sandbox/foundations/voters33to39/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '040': {
          'name': 'Voters 40 to 49',
          'endpoint':'http://service.civicpdx.org/disaster-resilience/sandbox/foundations/voters40to49/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
        '041': {
          'name': 'Voters 50 plus',
          'endpoint':'http://service.civicpdx.org/disaster-resilience/sandbox/foundations/voters50plus/',
          'description': 'This is a fake description. This is a fake description. This is a fake description. This is a fake description. ',
          'visualization': 'ChoroplethMap',
        },
    },
 }
    return {
      'statusCode': 200, 
      'body': body
      }