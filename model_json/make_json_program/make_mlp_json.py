import json

def make_json():
    json_value = {
        
    } 
    with open('./model_json/json/mlp.json', 'w') as f:
        json.dump(json_value, f, ensure_ascii=False)

if __name__ == "__main__":
    make_json()
