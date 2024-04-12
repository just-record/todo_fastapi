import yaml

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._load_config()
        return cls._instance

    @classmethod
    def _load_config(cls):
        with open("core/config.yaml", "r") as file:
            cls.config = yaml.safe_load(file)

    @classmethod
    def get_config(cls):
        return cls.config