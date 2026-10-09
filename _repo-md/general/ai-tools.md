---
title: AI Tools
subtitle: How and when to use AI in this course
---


<!-- Facts on this page re-verified against the live web on 2026-07-11; Zed student plan and Mistral Vibe sections on 2026-09-03. Mistral naming (Le Chat is now Vibe, La Plateforme is now Studio), the free plan, the sign-in/key route and both opt-out paths re-read from Mistral's pricing, docs and help pages on 2026-10-09. Free sign-up (no phone number asked), both opt-out switches, the `vibe` browser sign-in and the install from Zed's agent registry clicked through with a fresh free account by Tobias the same day. -->

## The course policy

The course runs a phased AI policy, and the rules are different in each part.

- **Part I (Sessions I-V): no AI.** You learn to read, write and debug Python yourself. The only assistant you may use is the **course chatbot** (the widget in the sidebar), and in Part I it deliberately explains and hints rather than handing you finished code.
- **Part II (Sessions VI-IX): AI is allowed and taught.** From Session VI we work *with* AI on purpose. Checkpoints 4 and 5 explicitly allow AI.
- **Part III (Sessions X-XIII): AI is encouraged**, with disclosure. Use what makes you productive on your project.

> **Important**
>
> **The disclosure rule.** Every submission that used AI says so. In Part II that is a one-line note on the submission saying what the AI was used for (Part I is AI-free, so there is nothing to disclose). For example: *"Used AI to explain a `KeyError` and to draft the docstring for `load_data()`."* In Part III it lives in a short section of your project repo's `README`: which tools you used, what for, and what you verified yourself. This is not about catching anyone out. Being able to say clearly what a tool did for you is part of using it well.

The rest of this page shows you how to get a working, **zero-cost** AI setup. It costs nothing and needs no credit card. Everything happens on a schedule:

| When | What | Why then |
|------------------------|------------------------|------------------------|
| **Session I** | Free [GitHub](https://github.com) account | Zed's student plan only accepts GitHub accounts **older than 30 days**, and your project lives on GitHub from Session X |
| **Session VI** | Free Mistral account with the training opt-out, Zed student plan application | AI becomes allowed; the GitHub account is old enough now |
| **Session VII (in class)** | Install uv, Zed and Mistral Vibe | From Session VIII the labs run on your own machine |
| **Before Session X** | Install git and the GitHub CLI | Session X puts your project on GitHub |

*Menu paths and program terms on this page are current as of October 2026.*

## The guaranteed free setup: Mistral

This path costs nothing and needs no credit card. Do this one first.

### 1. Create a free Mistral account

Go to [chat.mistral.ai](https://chat.mistral.ai) and sign up. You land in **Vibe**, Mistral's assistant (the equivalent of ChatGPT or Claude in your browser). It used to be called *Le Chat*, so older guides and videos still use that name. The free plan is enough for asking questions, explaining errors and drafting code. It limits how many messages and coding sessions you get.

The same account later signs you in to the AI agent *inside your editor* (see the Zed section below). You don't need a separate API key for that.

### 2. Turn off training on your data

> **Warning**
>
> **On the free plan your data is used for training by default.** Your Vibe conversations, and anything sent through the API, may be used to improve Mistral's models unless you opt out. There are **two separate switches** in the Admin panel at [admin.mistral.ai](https://admin.mistral.ai):
>
> 1.  Under **Manage**, select **Vibe**. In its **Privacy** section, turn off *Allow your interactions to be used to train our models*.
> 2.  Open the **Privacy** menu in the left navigation bar. Under **Anonymous improvement data**, turn that switch off as well. It covers the API, the route programs use to talk to Mistral's models.
>
> Do both before you paste real coursework anywhere.

## The Zed student plan (Session VI)

Zed is the editor we use from Session VIII on, and we install it together in class in Session VII. If you are an enrolled student, Zed gives you its paid plan for free, and you apply for it in **Session VI**, well before you need it:

1.  Go to [dashboard.zed.dev/education/apply](https://dashboard.zed.dev/education/apply) and **sign in with GitHub**. Zed requires the GitHub account to be **at least 30 days old**, which is why you created it in Session I.
2.  Submit your **KLU e-mail address** for verification. This can take up to 72 hours.
3.  Once verified you get **12 months of Zed Pro**: unlimited edit predictions and **\$10/month in AI token credits**. Details at [zed.dev/education](https://zed.dev/education).

> **Note**
>
> **The 12 months expire.** After 12 months the Student plan automatically downgrades to the free plan. It is a great head start, not a permanent free ride, so don't build a habit that depends on the credits lasting forever. This is exactly why the Mistral path above matters: it stays free, and nothing in the course depends on the plan.

If your KLU address isn't recognized by the verification system, or your GitHub account is still too young, **ask me**. Both can be resolved.

## AI inside Zed: Mistral Vibe (Session VII, in class)

The AI you program with from Session VIII is **[Mistral Vibe](https://docs.mistral.ai/vibe/code/overview)**, Mistral's coding agent (Mistral's own pages call this mode *Vibe Code*). It runs inside Zed's agent panel on your free Mistral account from Session VI. **We do this together in class in Session VII**, after [installing uv](uv.qmd). You don't need to do it earlier:

1.  **Install Zed** from [zed.dev](https://zed.dev) (macOS, Windows, Linux), run the installer, and open it once to confirm it launches.

2.  **Install Vibe** in a terminal. uv is already on your machine, so one command works on every system:

    ``` bash
    uv tool install mistral-vibe
    ```

    If the terminal then says `vibe` is not found, run `uv tool update-shell`, then close and reopen the terminal.

3.  **Sign in.** Run `vibe` once in the terminal. The setup asks you to sign in with your Mistral account in the browser; use the account from Session VI. It saves the sign-in for future runs. Type `exit` to leave. If the sign-in does not work, create a key under **Code › Vibe CLI** at [chat.mistral.ai/code/extensions](https://chat.mistral.ai/code/extensions), copy it right away, and paste it when the setup asks. That key works on the free plan too.

4.  **Add it to Zed.** In Zed, open the command palette (`Cmd/Ctrl+Shift+P`) and run **`zed: acp registry`**. Find **Mistral Vibe** in the list and install it.

5.  **Try it.** Open the agent panel (the sparkle icon at the bottom right, or **`agent: new thread`** in the command palette), pick Mistral Vibe from the agent dropdown, and ask it something about an open file. If it answers, you're ready for Session VIII.

> **Warning**
>
> **Already paying for ChatGPT or Claude?** You may use those in Zed's own agent under their own rules, but the course teaches and supports one path: Mistral Vibe. One trap to know: a **Claude Pro/Max subscription does not work** in Zed's built-in Anthropic provider, which bills separate API credits. Use the free Mistral account.

## The course chatbot

The chat widget in the sidebar stays available in Part II as well. The difference: in Part I it hints and explains; in Part II it will give you **full code** on request, because by then working with AI-generated code is part of what you are learning. It knows the course material, so it is often the fastest way to get an answer that fits what we have actually covered.

## Recap

You now have:

1.  A GitHub account from Session I, old enough for the Zed student plan.
2.  A free Mistral account for questions and explanations in Vibe, with both training switches turned off.
3.  A Zed student plan application on its way.
4.  From Session VII: Zed, with Mistral Vibe in its agent panel.
5.  The one habit that applies everywhere: a one-line AI-disclosure note on every submission that used AI.
