import json
import os

import click
from google.protobuf import json_format

import replay_pb2

DIR = os.path.dirname(os.path.abspath(__file__))
DFAULT_INFILE=f"{DIR}/Trains_vs_Orcust_2.yrpX.pb"

def _print_as_json(infile=DFAULT_INFILE):
    replay = replay_pb2.Replay()
    # print(dir(replay_pb2))
    # breakpoint()
    with open(infile, "rb") as f:
        txt = f.read()
        replay.ParseFromString(txt)
        out = json_format.MessageToDict(replay)
        print(json.dumps(out))
    return out

@click.group()
def cli():
    pass


@cli.command()
@click.argument("infile", default=DFAULT_INFILE)
def print_as_json(infile):
    _print_as_json(infile)

if __name__ == "__main__":
    cli()
