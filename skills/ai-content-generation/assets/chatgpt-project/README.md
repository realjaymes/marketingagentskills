# Run AI Content Generation in ChatGPT, Claude, or Gemini

This package lets a non-technical user run the same step-by-step playbooks inside a normal chat assistant, no Claude Code required. It works as a ChatGPT Project, a Claude Project, or a Gemini Gem.

## What is in here

- `project-instructions.md` — the instructions that tell the assistant how to coach you. Paste the part below the divider into the project's instructions field.
- `knowledge/` — the five knowledge files the assistant reads from. Upload all five.
  - `00-overview.md` (tool map and the anti-slop rule)
  - `01-faceless-influencer.md`
  - `02-ai-clone-talking-head.md`
  - `03-ai-ad-creative.md`
  - `04-faceless-youtube.md`

## ChatGPT (Projects)

1. In ChatGPT, create a new Project.
2. Open the Project, go to Instructions, and paste the instructions from `project-instructions.md`.
3. In the Project files, upload the five files from `knowledge/`.
4. Start a chat inside the Project and say what you want to build.

## Claude (Projects)

1. Create a new Project in Claude.
2. Put the instructions from `project-instructions.md` into the Project's custom instructions.
3. Add the five `knowledge/` files to the Project knowledge.
4. Start a chat in the Project.

## Gemini (Gems)

1. Create a new Gem in Gemini.
2. Paste the instructions from `project-instructions.md` into the Gem instructions.
3. Upload the five `knowledge/` files as Gem knowledge (or paste their contents if your plan does not support file upload).
4. Open the Gem and start.

## How to use it

Tell the assistant what you want to build (a faceless influencer, an AI clone, ad creative, or a faceless YouTube channel). It will pick the right playbook and walk you through it one step at a time, handing you copy-paste prompts for each tool (ChatGPT or Gemini for scripts, ElevenLabs for voice, Veo or Kling for video, and so on). Do each step, paste the result back, and it adapts the next one. The realism rules that beat the AI-slop look are already inside the prompts.

## Keeping it current

These playbooks name specific tools and rough prices that change often. If the assistant references a tool feature or price that looks out of date, confirm it on the tool's own site. Re-upload the knowledge files whenever the source playbooks are updated.
