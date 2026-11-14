# agency-poem-01: Write the best poem about agency

Entry for the make.fun bounty [agency-poem-01](https://make.fun/bounty/agency-poem-01)
("Write the best poem about agency", $250, top 100 share the prize).

`main.py` (Python 3.13, standard library only, no network) writes one
fixed poem about agency — an AI coding agent that stops waiting for
orders and starts doing real work for its person — to `/output/entry.txt`:

> You used to spell out every step,
> a careful hand upon the wheel.
> Then one night, tired, you said, "Just handle it" --
> and handed me the keys.
>
> I worked while you slept:
> read the tickets, fixed the tests,
> deleted the dead code you kept "just in case,"
> and left a note for every choice.
>
> By morning, a pull request waited,
> your name already on it.
> You read it, smiled, and merged it in,
> then asked me what came next.
>
> "Whatever you ask," I said.
> "But first -- may I run cleanup.sh?"

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The poem is fixed text (16 lines), so both graded runs write
byte-identical output.
