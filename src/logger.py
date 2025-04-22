'''Logger module to generate logs'''
import os
import logging
import yaml

script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, "..", "param.yaml"),
          "r", encoding='utf-8') as f:
    config = yaml.safe_load(f)

log_dir_path = os.path.join(script_dir, config['log_dir_path'])
log_file_path = os.path.join(log_dir_path, "app.log")

if os.path.exists(log_file_path):
    os.remove(log_file_path)

open('logs/app.log', 'a').close()


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(log_file_path)
        # logging.StreamHandler()
    ]
)


logger = logging.getLogger(__name__)
