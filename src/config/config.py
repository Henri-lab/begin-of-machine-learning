import yaml

def load_config(filepath):
    """loading YAML config file"""
    with open(filepath, 'r') as f:
        config = yaml.safe_load(f)
    return config

config = load_config('config/settings.yaml')