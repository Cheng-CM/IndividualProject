import yaml
def callConfig(name: str) -> str:
    with open("mongo-config.yml", "r") as stream:
        mongo = yaml.safe_load(stream)
        return mongo[name]