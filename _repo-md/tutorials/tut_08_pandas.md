---
title: Episode 8 — The Data Room
subtitle: Programming with Python · Tutorial 08
---


The investor wasn't impressed by a slide. She was impressed by *data*. So she
slides a USB stick across the table: **every order, two full weeks.** "Impress
me." That stick is now a real file, `orders.csv`, with eighty rows: too many to
eyeball, too many for a hand-written loop. This week you learn the tool built
for exactly this: **pandas**. You'll load a whole spreadsheet into one
*DataFrame*, filter it with boolean masks, combine conditions with `&`, add a
derived column on a safe copy, and answer per-zone questions with `groupby`.
Tobi, meanwhile, has discovered AI. Your real job is to **supervise** it and
catch the confident nonsense.

## Work on the notebook

<a href="../notebooks/nb_08_lab_dataroom/" class="btn btn-primary">Open in browser</a>
[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/beyondsimulations/Introduction-to-Python/blob/main/notebooks/nb_08_lab_dataroom.py)

**Open in browser (recommended):** runs entirely on your machine, in this tab:
no account, no installation, and after it loads no internet is needed.

> **If the notebook won't boot**
>
> This lab loads pandas, which is fetched over the network the first time. If the
> notebook fails to boot with a network error, **reload the page once**
> (Cmd/Ctrl + R). That almost always fixes it.

> **How your work is saved (read this once)**
>
> Your progress lives **in this browser tab**. If you **reload** the page
> (Cmd/Ctrl + R) your work is still there. But if you **close the tab and open
> the link again later, you start from a clean notebook**. There is no
> cross-device sync in the browser, and clearing browser data or private mode
> also wipes it.
>
> So: **download your `.py` before you leave** (menu → Download → *Download Python
> code*). That download is the *only* guaranteed copy. Handing in files works
> exactly like this in the checkpoints, so you get to practice the motion every
> week. Note: a downloaded `.py` is for submission and backup. You can't upload
> it back into the browser editor.

**Open in molab:** marimo's free cloud (account required). Your copy saves to
your account and reopens on **any device**. Choose this if you know you'll
switch computers or want to be certain nothing is lost. Optional: nothing
graded ever requires it.

<!-- PUBLISH AFTER SESSION VIII (see docs/authoring-conventions.md → Solution notebooks):
## Solutions

[Solutions notebook (read-only)](../notebooks/sol_08_lab_dataroom/){.btn}
-->
