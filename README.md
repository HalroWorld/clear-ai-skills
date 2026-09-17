# clear-ai-skills

<p align="center">
  <a href="README.md">English</a> · <a href="README.ko.md">한국어</a>
</p>

A pair of skills that turn everyday phrasing into precise requests for an AI, and dense technical answers into explanations people can actually follow.

## Skills

### `intent-clarifier`

Restates casual, vague, or rambling requests as something an AI can act on.

- Separates the goal, the constraints, and the expected deliverable.
- Maps UI described in plain words — "the menu that slides in from the side" — to its real name, such as "drawer".
- Reframes CSS symptoms like "the page shifts sideways on my phone" around the observed problem and the desired result.
- Handles server, network, frontend, backend, and language symptoms the same way, without appending causes or fixes that have not been verified.
- Triggers automatically when the user states a desired outcome — "I wish it would…", "I want…", "ask it to…", or the Korean equivalents — and the target, scope, or conditions are unclear.
- Returns the restated request and its open questions in the language you wrote in.
- Numbers open questions `1.`, `2.`, `3.`. When a question splits into alternatives, it lists them and marks the recommended one with `(추천)` and a one-line reason.
- Confirms the restated request before treating it as final.

### `simple-explanation`

Judges how hard an answer is to follow, then explains technical or unfamiliar material in plain Korean before the user has to ask.

- Applies automatically, with no "explain it simply" request needed.
- Answers in the language you wrote in.
- Leads with the conclusion.
- Unpacks UI terms: "drawer → the menu that slides in from the side of the screen".
- Unpacks CSS terms: "padding → the space inside a box".
- Unpacks development terms: "timeout → the state where something took too long and the wait was abandoned".
- Preserves what is done, what is planned, what is unconfirmed, and any condition that matters.

Both skills ship with dictionaries covering 36 UI elements, 42 CSS symptoms, and 34 development terms. They are wired so that only the entries relevant to a given question or answer get read.

### Language

Every dictionary entry carries both Korean and English phrasing, and both skills **answer in whatever language you wrote in** — English in, English out; Korean in, Korean out. Language-independent judgement notes, such as candidate causes and the criteria separating one term from a similar one, are written in Korean only and translated into your language when answering.

### Development domain examples

The [development dictionary](shared/development-dictionary.md) gives a clarified-request example and a plain-language example for each of five domains.

| Domain | What the user said | What `intent-clarifier` produces | What `simple-explanation` unpacks |
| --- | --- | --- | --- |
| Server / ops | "Works locally, dies when I deploy" | Investigate why the app exits in the deployed environment and fix it so it runs | Environment variable → a configuration value the program needs at run time |
| Network | "Connects from home but not from the office" | Investigate why the office network cannot reach it and resolve the cause | Timeout → the state where something took too long and the wait was abandoned |
| Frontend | "I want my draft to survive a refresh" | Make an in-progress draft persist across a page refresh | State → the current data that decides how the screen behaves and what it shows |
| Backend / data | "Pressing save twice creates two copies of the post" | Investigate why repeated saves duplicate a post and prevent the duplication | Authorization → deciding whether a signed-in user is allowed to perform this action |
| Languages / runtime | "I'm passing an input field value and it says it needs a number" | Investigate the mismatch between the input value and the expected numeric type, and handle it correctly | Exception → the mechanism that reports an error raised during execution |

Covers fundamentals for JavaScript, TypeScript, Python, Java, Go, and Rust. Naming a symptom and diagnosing its actual cause are kept distinct.

## Install

<details>
<summary><strong>Codex plugin</strong></summary>

Register the marketplace and install the plugin.

```bash
codex plugin marketplace add HalroWorld/clear-ai-skills
codex plugin add clear-ai-skills@clear-ai-skills
```

In a new conversation:

```text
$clear-ai-skills:intent-clarifier Clean this request up so an AI can act on it.
$clear-ai-skills:simple-explanation Explain the answer below in plain terms.
```

To install by hand, copy the skill folders you want from `plugins/clear-ai-skills/skills/` into `~/.codex/skills/`.

</details>

<details>
<summary><strong>Claude Code plugin</strong></summary>

Register the marketplace and install the plugin in Claude Code.

```text
/plugin marketplace add HalroWorld/clear-ai-skills
/plugin install clear-ai-skills@clear-ai-skills
```

Then invoke a skill:

```text
/clear-ai-skills:intent-clarifier Clean this request up so an AI can act on it.
/clear-ai-skills:simple-explanation Explain the answer below in plain terms.
```

Claude may also reach for a skill on its own when the request matches its description.

### Staying up to date

Auto-update is **off by default** for third-party marketplaces. Turn it on once and updates arrive on their own.

1. Run `/plugin`
2. Open the **Marketplaces** tab and select `clear-ai-skills`
3. Choose **Enable auto-update**

Updates land in the background shortly after a session starts; when a new version arrives you are prompted to run `/reload-plugins`. To pull one immediately:

```text
/plugin marketplace update clear-ai-skills
/plugin update clear-ai-skills
```

You can copy the skill folders into `~/.claude/skills/` instead of installing the plugin, but this is not recommended. The copy never updates, and it shadows the plugin skill of the same name, so `/intent-clarifier` keeps running the old version. See the [official Claude Code plugin documentation](https://code.claude.com/docs/en/plugins) for the precedence rules.

</details>

## License

This project is distributed under the [MIT License](LICENSE).

## Credits

Parts of the UI and CSS dictionaries are based on the [Giting UI menu](https://giting.kr/skills/ui-menu) and [CSS symptom dictionary](https://giting.kr/skills/css-menu). The original copyright and MIT license notices are included under each skill's `references/`.
