def deep_get(dictionary, keys, default=None):
    from functools import reduce
    # https://stackoverflow.com/a/46890853/4004697 for safely getting nested values
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."),
                  dictionary)
