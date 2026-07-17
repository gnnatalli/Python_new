from pprint import pprint
from pymongo import MongoClient  # pip install pymongo

from local_settings import MONGODB_URL_WRITE

with MongoClient(MONGODB_URL_WRITE) as client:

    relativeMass = {
    "Mercury": 0.33,
    "Venus": 4.87,
    "Earth": 5.97,
    "Mars": 0.642,
    "Jupiter": 1898,
    "Saturn": 568,
    "Uranus": 86.8,
    "Neptune": 102
}

    for name, mass in relativeMass.items():

        client['ich_edit']['planets_Naty'].update_one(
          { "name": name },
          { "$set": { "relativeMass": mass } },

        );



    result = client['ich_edit']['planets_Naty'].aggregate([
        {
            '$match': {
                'surfaceTemperatureC': {
                    '$gt': 50
                }
            }
        }, {
            '$count': 'count_Planet'
        }
    ])

    print(*result, sep='\n')