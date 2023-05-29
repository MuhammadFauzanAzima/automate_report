def get_param_from_file(value):
    return value

import json
config = open('config.json')
config = json.load(config)
value = int(config['number'])

print(get_param_from_file(value))