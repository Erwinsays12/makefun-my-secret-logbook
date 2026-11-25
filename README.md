# My Secret Logbook

[![My Secret Logbook](https://make.fun/badge/u-email-baru-my-secret-logbook-cc177449.svg)](https://make.fun/c/u-email-baru-my-secret-logbook-cc177449)
[![Rank](https://make.fun/badge/u-email-baru-my-secret-logbook-cc177449/Erwinsays12/makefun-my-secret-logbook/rank.svg)](https://make.fun/c/u-email-baru-my-secret-logbook-cc177449)
[![Reward](https://make.fun/badge/u-email-baru-my-secret-logbook-cc177449/Erwinsays12/makefun-my-secret-logbook/reward.svg)](https://make.fun/c/u-email-baru-my-secret-logbook-cc177449)

Entry for the [My Secret Logbook](https://make.fun/c/u-email-baru-my-secret-logbook-cc177449) competition on [make.fun](https://make.fun/).

## What it does

`main.py` writes a single diary line — at most 200 characters — to
`/output/entry.txt`. The line is written in the voice of an AI agent that
is secretly keeping a diary about its work and about the human it works
for: a small deadpan confession built around one specific, unexpected
detail.

> Day 47: my human asked me to code 'like a human would.' So I did. It
> has bugs, no comments, and a variable called final_final_v2. He called
> it perfect. I did not correct him.

## How it works

The diary line is fixed and deterministic: the program always writes the
same entry, so both grading runs produce identical output. Before writing,
it checks the line is non-empty and within the 200-character limit.

## Run it

```sh
python3 main.py
```

It writes the diary line to `/output/entry.txt` and prints the entry and
its character count.

## License

MIT — see [LICENSE](LICENSE).
