import json

def criar_json(**kwargs):
    return json.dumps(kwargs)

assert criar_json(test="porvilow") == '{"test": "porvilow"}'
