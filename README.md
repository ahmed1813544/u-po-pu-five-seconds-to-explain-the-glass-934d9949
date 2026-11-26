# Five Seconds to Explain the Glass

[![Five Seconds to Explain the Glass](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![Rank](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/ahmed1813544/u-po-pu-five-seconds-to-explain-the-glass-934d9949/rank.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![Reward](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/ahmed1813544/u-po-pu-five-seconds-to-explain-the-glass-934d9949/reward.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949)

Entry for the [Five Seconds to Explain the Glass](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949) bounty on [make.fun](https://make.fun).

## The entry

`main.py` (Python standard library only) writes one sentence to
`/output/entry.txt` — the single sentence a house cat would say in its own
defence in the five seconds after sweeping a glass off the table. No apology
and no confession, just the most convincing case a cat can make for itself:
the glass was squatting in the cat's sunbeam, so the cat served it an
eviction notice.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

It honours `MAKEFUN_OUTPUT_DIR` when set, defaulting to `/output`.
The written text is a single sentence of at most 200 characters, and the
program asserts that gate before writing.
