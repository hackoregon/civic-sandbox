import json
def lambda_handler(event, context):
    body = {
    'packages' : { 
        'Greenspace': {
          'description': '',
          #'View of trees, parks, gardens, trails, and greenways per neighborhood.',
          'foundations' : ['024','007'],
          'default_foundation' : '024',
          'slides' : ['003', '004', '005'],
          'default_slide' : ['003', '004']
          },
        'Food Access': {
          'description': '',
          #'View of grocery locations, community gardens, and transit stops per neighborhood.',
          'foundations' : ['028', '044'],
          'default_foundation' : '044',
          'slides' : ['009', '010', '005', '014'],
          'default_slide' : '010'
          },
        'Sweeps': {
          'description': '',
          #'View of reports of camps, camp sweeps, and household data per neighborhood.',
          'foundations' : ['045', '007', '024', '025', '026','027'],
          'default_foundation' : '045',
          'slides' : ['012', '013', '011', '003', '004'],
          'default_slide' : ['012',]
          },
        'Bikes': {
          'description': '',
          #'View of daily bike estimates bike counts, bike routes, greenways, and multiuse trails per neighborhood',
          'foundations' : ['007'],
          'default_foundation' : '007',
          'slides' : ['001', '002', '008', '035', '036'],
          'default_slide' : ['001', '002']
          },
        'Disaster Resilience': {
          'description': '',
          #'description. description. description.',
          'foundations' : ['029', '030', '033', '034'],
          'default_foundation' : '029',
          'slides' : ['016'],
          'default_slide' : ['016']
          },
        'Evictions': {
          'description': '',
          #'Eviction, rent, income, and property values by census blockgroup.',
          'foundations' : ['018', '019', '020', '021', '022', '043'],
          'default_foundation' : '020',
          'slides' : ['014',  '009', '011', '017'],
          'default_slide' : ['011']
          },
        'Voters': {
          'description': '',
          #'Voters by age.',
          'foundations' : ['037', '038', '039', '040', '041'],
          'default_foundation' : '037',
          'slides' : ['009',  '004', '008', '002'],
          'default_slide' : []
          },
        'Transportation': {
          'description': '',
          #'Transporation Package',
          'foundations' : ['042'],
          'default_foundation' : '042',
          'slides' : ['031', '032', '015'],
          'default_slide' : ['031', '032', '015',]
          },
    },
    'slides': {
        '001': {
          'name': 'bike parking',
          'endpoint': 'http://service.civicpdx.org/neighborhood-development/sandbox/slides/bikeparking/',
          'visualization': 'ScatterPlotMap',
        },
        '002': {
          'name': 'bike lanes',
          'endpoint': 'http://service.civicpdx.org/neighborhood-development/sandbox/slides/bikelanes/',
          'visualization': 'PathMap',
        }, 
        '003': {
          'name': 'parks',
          'endpoint': 'http://service.civicpdx.org/neighborhood-development/sandbox/slides/parks/',
          'visualization': 'PolygonPlotMap',
        },
        '004': {
          'name': 'multi-use trails',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/multiusetrails/',
          'visualization': 'PathMap',
        },    
        '005': {
          'name': 'community gardens',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/communitygardens/',
          'visualization': 'SmallPolygonMap',
        },    
        '008': {
          'name': 'bike greenways',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/bikegreenways/',
          'visualization': 'PathMap',
        }, 
        '009': {
          'name': 'rail stops',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/railstops/',
          'visualization': 'ScatterPlotMap',
        }, 
        '010': {
          'name': 'grocery stores',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/retailgrocers/',
          'visualization': 'ScatterPlotMap',
        },
        '011': {
          'name': 'demolitions',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/demolitions/',
          'visualization': 'ScatterPlotMap',
        },
        '012': {
          'name': 'camp sweeps',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/campsweeps/',
          'visualization': 'ScatterPlotMap',
        },
        '013': {
          'name': 'camp reports',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/campreports/',
          'visualization': 'ScatterPlotMap',
        },
        '014': {
          'name': 'bus stops',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/busstops/',
          'visualization': 'ScatterPlotMap',
        },
        '015': {
          'name': 'Change in Ridership by Route',
          'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/slides/routechange/',
          'visualization': 'PathMap',
        },
        '016': {
          'name': 'points of interest',
          'endpoint':'http://service.civicpdx.org/disaster-resilience/sandbox/slides/poi/',
          'visualization': 'IconMap',
        },
        '017': {
          'name': 'Building Permits',
          'endpoint':'http://service.civicpdx.org/housing-affordability/sandbox/slides/permits/',
          'visualization': 'ScreenGridMap',
        },
        '031': {
          'name': 'Safety Hotline',
          'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/slides/safetyhotline/',
          'visualization': 'ScatterPlotMap',
        },
        '032': {
          'name': 'Crashes',
          'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/slides/crashes/',
          'visualization': 'ScatterPlotMap',
        },
        '035': {
          'name': 'Bike Counts',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/bikecounts/',
          'visualization': 'ScatterPlotMap',
        },
        '036': {
          'name': 'Bike Estimates',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/slides/bikeestimates/',
          'visualization': 'ScatterPlotMap',
        },
    }, 
    'foundations': {
        '007': {
          'name': 'Total Population',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/population/',
          'visualization': 'ChoroplethMap',
        },
        '018': {
          'name': 'Median Houshold Income',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/income/',
          'visualization': 'ChoroplethMap',
        },
        '019': {
          'name': 'Median Gross Rent',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/grossrent/',
          'visualization': 'ChoroplethMap',
        },
        '020': {
          'name': 'Evictions',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/evictions/',
          'visualization': 'ChoroplethMap',
        },
        '021': {
          'name': 'Renter Occupied Households',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/renteroccupied/',
          'visualization': 'ChoroplethMap',
        },
        '022': {
          'name': 'Rent Burden',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/rentburden/',
          'visualization': 'ChoroplethMap',
        },
        '024': {
          'name': 'Households with Children',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/under18/',
          'visualization': 'ChoroplethMap',
        },
        '025': {
          'name': 'Households with Seniors',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/over65/',
          'visualization': 'ChoroplethMap',
        },
        '026': {
          'name': 'Householders Living Alone',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/livingalone/',
          'visualization': 'ChoroplethMap',
        },
        '027': {
          'name': 'Owner Occupied Households',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/owneroccupied/',
          'visualization': 'ChoroplethMap',
         },
        '028': {
          'name': 'Percent Renter Occupied',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/pctrenteroccupied/',
          'visualization': 'ChoroplethMap',
        },
        '029': {
          'name': 'Shaking Intensity',
          'endpoint':'http://service.civicpdx.org/disaster-resilience/sandbox/foundations/shaking/',
          'visualization': 'ChoroplethMap',
        },
        '030': {
          'name': 'Wet Season Mean Deformation Intensity',
          'endpoint':'http://service.civicpdx.org/disaster-resilience/sandbox/foundations/liquefaction/',
          'visualization': 'ChoroplethMap',
        },
        '033': {
          'name': 'Dry Season Mean Deformation Intensity',
          'endpoint':'http://service.civicpdx.org/disaster-resilience/sandbox/foundations/landslide/',
          'visualization': 'ChoroplethMap',
        },
        '034': {
          'name': 'Census Reponse Rate',
          'endpoint':'http://service.civicpdx.org/disaster-resilience/sandbox/foundations/censusresponse/',
          'visualization': 'ChoroplethMap',
        },
        '037': {
          'name': 'Voters 18 to 25',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/voters18to25/',
          'visualization': 'ChoroplethMap',
        },
        '038': {
          'name': 'Voters 26 to 32',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/voters26to32/',
          'visualization': 'ChoroplethMap',
        },
        '039': {
          'name': 'Voters 33 to 39',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/voters33to39/',
          'visualization': 'ChoroplethMap',
        },
        '040': {
          'name': 'Voters 40 to 49',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/voters40to49/',
          'visualization': 'ChoroplethMap',
        },
        '041': {
          'name': 'Voters 50 plus',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/voters50plus/',
          'visualization': 'ChoroplethMap',
        },
        '042': {
          'name': 'Change in Ridership by Census Block',
          'endpoint':'http://service.civicpdx.org/transportation-systems/sandbox/foundations/blockchange/',
          'visualization': 'ChoroplethMap',
        },
        '043': {
          'name': 'Eviction Rate',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/evictionrate/',
          'visualization': 'ChoroplethMap',
        },
        '044': {
          'name': 'Poverty Rate',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/povertyrate/',
          'visualization': 'ChoroplethMap',
        },
        '045': {
          'name': 'Camp Reports',
          'endpoint':'http://service.civicpdx.org/neighborhood-development/sandbox/foundations/reportsbymonth/',
          'visualization': 'ChoroplethMap',
        },
    },
 }
    return {
      'statusCode': 200, 
      'body': body
      }