---
title: AI Tools
subtitle: How and when to use AI in this course
---


<!-- Facts on this page re-verified against the live web on 2026-07-11; Zed student plan and Mistral Vibe sections on 2026-09-03. -->

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
| **Session VI** | Mistral account + API key, Zed student plan application | AI becomes allowed; the GitHub account is old enough now |
| **Before Session X** | Install uv, Zed, Mistral Vibe and the GitHub CLI | Session X builds on a working toolchain |

*Menu paths and program terms on this page are current as of September 2026.*

## The guaranteed free setup: Mistral

This path costs nothing and needs no credit card. Do this one first.

### 1. Create a free Le Chat account

Go to [chat.mistral.ai](https://chat.mistral.ai) and sign up. **Le Chat** is Mistral's chat assistant (the equivalent of ChatGPT or Claude in your browser). The free tier is enough for asking questions, explaining errors and drafting code.

### 2. Get a free La Plateforme API key

If you later want AI *inside your editor* (see the Zed section below), you need an API key.

1.  Go to [console.mistral.ai](https://console.mistral.ai) and sign in with the same account.
2.  Choose the free **"Experiment"** tier when prompted.
3.  Open the **API Keys** page and create a new key.
4.  Copy the key somewhere safe. Mistral Vibe, the AI agent in your editor, asks for it later. **The key is shown only once**, right when you create it, and cannot be displayed again. If you miss it, you have to generate a new one.

> **Warning**
>
> **Free-tier data is used for training by default.** On the free tiers, both your Le Chat conversations and your API inputs and outputs may be used to improve Mistral's models unless you opt out. In your Mistral account settings (the Admin Console at [admin.mistral.ai](https://admin.mistral.ai)), find the **privacy** section and turn off the use of your data for training; there may be one switch for Le Chat and a separate one for the API, so check both. Do this before you paste real coursework into either.

## The Zed student plan (Session VI)

Zed is the editor we use from Session X on. If you are an enrolled student, Zed gives you its paid plan for free, and you apply for it in **Session VI**, well before you need it:

1.  Go to [dashboard.zed.dev/education/apply](https://dashboard.zed.dev/education/apply) and **sign in with GitHub**. Zed requires the GitHub account to be **at least 30 days old**, which is why you created it in Session I.
2.  Submit your **KLU e-mail address** for verification. This can take up to 72 hours.
3.  Once verified you get **12 months of Zed Pro**: unlimited edit predictions and **\$10/month in AI token credits**. Details at [zed.dev/education](https://zed.dev/education).

> **Note**
>
> **The 12 months expire.** After 12 months the Student plan automatically downgrades to the free plan. It is a great head start, not a permanent free ride, so don't build a habit that depends on the credits lasting forever. This is exactly why the Mistral path above matters: it stays free, and nothing in the course depends on the plan.

If your KLU address isn't recognized by the verification system, or your GitHub account is still too young, **ask me**. Both can be resolved.

## AI inside Zed: Mistral Vibe (before Session X)

The AI you program with in Part III is **[Mistral Vibe](https://github.com/mistralai/mistral-vibe)**, Mistral's coding agent. It runs inside Zed's agent panel and uses the API key from Session VI. **Nothing in this section is needed before Session IX.** Do it as part of the Session IX pre-work, after the [git and gh setup](git-basics.qmd#one-time-setup) and [installing uv](uv.qmd):

1.  **Install Zed** from [zed.dev](https://zed.dev) (macOS, Windows, Linux), run the installer, and open it once to confirm it launches.

2.  **Install Vibe** in a terminal. uv is already on your machine, so one command works on every system:

    ``` bash
    uv tool install mistral-vibe
    ```

3.  **Give it your key.** Run `vibe` once in the terminal; it asks for the API key and saves it for future runs. Type `exit` to leave.

4.  **Tell Zed about it.** In Zed, open the command palette (`Cmd/Ctrl+Shift+P`), run **`zed: open settings`**, and add this inside the outer braces. The file already has entries, so put a comma after the last existing one before you paste; JSON insists on it, and a missing comma is the classic first-timer error here:

    ``` json
    "agent_servers": {
      "Mistral Vibe": {
        "type": "custom",
        "command": "vibe-acp",
        "args": [],
        "env": {}
      }
    }
    ```

5.  **Try it.** Open the agent panel (the sparkle icon at the bottom right, or **`agent: new thread`** in the command palette), pick Mistral Vibe from the agent dropdown, and ask it something about an open file. If it answers, you're ready for Session X.

> **Warning**
>
> **Already paying for ChatGPT or Claude?** You may use those in Zed's own agent under their own rules, but the course teaches and supports one path: Mistral Vibe. One trap to know: a **Claude Pro/Max subscription does not work** in Zed's built-in Anthropic provider, which bills separate API credits. Use the free Mistral key.

## The course chatbot

The chat widget in the sidebar stays available in Part II as well. The difference: in Part I it hints and explains; in Part II it will give you **full code** on request, because by then working with AI-generated code is part of what you are learning. It knows the course material, so it is often the fastest way to get an answer that fits what we have actually covered.

## Recap

You now have:

1.  A GitHub account from Session I, old enough for the Zed student plan.
2.  A free Le Chat account for questions and explanations.
3.  A free La Plateforme API key (with the training opt-out done) that powers Mistral Vibe in Zed.
4.  A Zed student plan application on its way, and Vibe installed before Session X.
5.  The one habit that applies everywhere: a one-line AI-disclosure note on every submission that used AI.
