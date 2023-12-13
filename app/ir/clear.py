import os
import argparse

from configs.flask_config import flask_cfg


def clear_server_cache(verbose=False):
    cache_path = os.path.join(
        flask_cfg['static_path'], 
        flask_cfg["cache_cfg"]['cache_path'])
    for curdir, dirs, files in os.walk(cache_path):
        for fname in files:
            os.remove(os.path.join(curdir, fname))
            if verbose:
                print("- cache file <{}> under [{}] removed".format(fname, curdir))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", action="store_true", default=False)
    args = parser.parse_args()

    clear_server_cache(args.v)

