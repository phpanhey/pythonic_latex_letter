import argparse
import json

def main():
    config = get_config()

def get_config():
 config_file_name = parse_args()["config"] 
 with open(config_file_name) as config_file:
    return json.load(config_file)

def parse_args():
    parser = argparse.ArgumentParser()    
    parser.add_argument("--config", default="config.json")    
    return vars(parser.parse_args())
    
if __name__ == "__main__":
    main()