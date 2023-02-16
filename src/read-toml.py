import tomllib

with open("./test.toml", "rb") as f:
    config = tomllib.load(f)
    print(config)
