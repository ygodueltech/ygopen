```
poetry install

poetry run python say.py print-as-json

poetry run python say.py print-as-json Trains_vs_Orcust_2.yrpX.pb
```

also can use above makefile

```
make -s runpy INFILE=~/Downloads/Trains_vs_Orcust_2.yrpX.pb > asjson.json
```

`-s` is to silence echoing commands
