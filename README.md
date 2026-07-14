# Marketing Agent Skills

29 AI agent skills for marketing tasks, built for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and similar AI coding assistants (Cursor, Windsurf, Codex, Cline, Roo Code).

---

I'm [James](https://www.jamespraise.xyz), founder of [Marketing In Action](https://marketinginaction.xyz) and a Product & Growth Marketing consultant with close to a decade of startup experience. I've been a founding marketer multiple times, building marketing functions and systems from scratch.

This repo is the Claude skills version of the [MIA Resources](https://marketinginaction.xyz/resources/) I have developed (100+ marketing templates and AI prompt frameworks for execution and consistent high-quality outputs from AI tools like ChatGPT Projects, Claude Projects, Gemini Gems, Custom GPTs & OpenAI Assistants).

These skills make it easier to unify and apply the knowledge and prompts from the knowledge files and custom GPTs/prompts.

**New to Claude Code?** Read the [Claude Code for Marketers](https://marketinginaction.xyz/resources/claude-code-for-marketers/) guide. It walks you through setting up Claude Code, understanding key concepts, and installing these skills step by step. No coding experience needed.

I am currently experimenting with vibe coding, and this is one of the projects I'm building with that knowledge. You can also check out the vibe-coded repo of the MIA website here: [github.com/realjaymes/marketinginaction](https://github.com/realjaymes/marketinginaction)

---

## What are Skills?

Skills are markdown files that give AI agents specialized knowledge to execute specific marketing tasks. Each skill contains frameworks, best practices, and structured approaches that help Claude produce better, more consistent outputs for marketing work.

See demo:

<a href="https://youtu.be/jUd-FlWWeOA">
  <img src="https://img.youtube.com/vi/jUd-FlWWeOA/maxresdefault.jpg" alt="Watch the demo" width="100%">
</a>

---

## Available Skills

| Skill | Description |
|-------|-------------|
| [ad-creative](skills/ad-creative) | Generate, iterate, and scale ad creative (headlines, descriptions, primary text, full ad variations) for any paid advertising platform |
| [agent-skill-builder](skills/agent-skill-builder) | Create new Claude skills from scratch or translate ChatGPT projects into the Claude skill format |
| [ai-content-generation](skills/ai-content-generation) | Step-by-step, copy-paste-prompt playbooks for AI image and video content: faceless influencer, AI clone and talking head, AI ad creative (including UGC), and faceless YouTube. Ships with a ChatGPT, Claude, and Gemini project package |
| [ai-humanizer](skills/ai-humanizer) | Detect AI-written text, provide line-by-line recommendations, and rewrite content to sound genuinely human |
| [case-study-builder](skills/case-study-builder) | Create professional case studies, engagement summaries, and project summaries |
| [clay-gtm-outbound](skills/clay-gtm-outbound) | Design and optimize Clay-powered GTM workflows for prospecting, signal detection, and outbound automation |
| [copy-anatomy](skills/copy-anatomy) | Reverse-engineer copy into reusable templates by identifying core components and extracting frameworks |
| [customer-segments](skills/customer-segments) | Create customer and user segment documents divided by traits, behaviors, and lifecycle stages |
| [experimentation](skills/experimentation) | Design, prioritize, execute, and review growth experiments using the ICEEE framework |
| [icp-persona](skills/icp-persona) | Generate ICP and buyer/user persona documents for B2B and B2C products |
| [landing-page](skills/landing-page) | Create landing page copy using modular section templates for homepages, feature pages, and campaigns |
| [lifecycle-marketing-campaigns](skills/lifecycle-marketing-campaigns) | Create lifecycle marketing campaign flows for SaaS, digital products, and service businesses |
| [marketing-advantages](skills/marketing-advantages) | Identify product marketing advantages and develop strategies across PLG, Market/Ecosystem, and Brand categories |
| [marketing-product-ideas](skills/marketing-product-ideas) | Generate marketing and product ideas grounded in behavioral principles and proven PLG experiments |
| [n8n-automation](skills/n8n-automation) | Design, build, debug, and document n8n workflows and AI agent automations |
| [openclaw](skills/openclaw) | Design, build, debug, and document OpenClaw workflows and AI assistant configurations |
| [performance-marketing](skills/performance-marketing) | Plan, review, and optimize paid campaigns across Google, Meta, LinkedIn, TikTok, YouTube, Reddit, X, Snapchat |
| [portfolio-positioning](skills/portfolio-positioning) | Position, audit, or launch into a multi-product company. Forces a brand architecture decision (branded house / house of brands / endorsed) before producing core narrative, per-product positioning cascade, messaging hierarchy, and launch sequencing |
| [press-release](skills/press-release) | Create complete press release packages with newsworthiness evaluation and multiple headlines |
| [product-launch-gtm](skills/product-launch-gtm) | Guide end-to-end product and feature launch planning with launch sizing, GTM strategy, and success measurement |
| [product-marketing-metrics](skills/product-marketing-metrics) | Build a product marketing measurement framework: north star, metric tree, funnel-stage and PMM-outcome metrics, leading vs lagging indicators, attribution, and a fill-in measurement plan, with worked examples across business models |
| [product-messaging](skills/product-messaging) | Create complete messaging frameworks including value propositions, taglines, and elevator pitches |
| [product-onboarding-activation](skills/product-onboarding-activation) | Design complete onboarding, activation, retention, and expansion lifecycles for SaaS products |
| [product-positioning](skills/product-positioning) | Create complete positioning frameworks with target customers, competitive differentiation, and market categories |
| [remotion](skills/remotion) | Create programmatic videos in React with a structured 7-step process from creative brief to rendered output |
| [saas-landing-pages](skills/saas-landing-pages) | Generate complete SaaS landing page drafts using 7 framework templates for different page types |
| [seo-audit](skills/seo-audit) | Audit, review, and diagnose SEO issues across technical, on-page, content quality, and authority dimensions |
| [skill-to-prompt](skills/skill-to-prompt) | Convert Claude skills into ChatGPT Project format (prompt instructions + knowledge files as .docx) |
| [tweetclaw-social-automation](skills/tweetclaw-social-automation) | Design and run safety-first X/Twitter workflows through TweetClaw: search tweets, search tweet replies, post tweets, export audiences, monitor mentions, and manage giveaway draws |
| [vibe-coding](skills/vibe-coding) | Guide beginner-to-intermediate developers through web development, Claude skills creation, and AI-assisted coding |

---

## Installation

### For Claude Web & Desktop Users

Claude.ai (the web app) and the Claude desktop app support skills via **Settings → Capabilities → Skills**. Each skill is uploaded individually as a `.zip` file (or a single `SKILL.md` for one-file skills). You cannot upload a folder containing multiple skills at once. That is a constraint of how Claude.ai imports skills today.

**Download pre-zipped skills from Releases**

1. Open the [latest Release](https://github.com/realjaymes/marketingagentskills/releases/latest)
2. Download the individual `.zip` files for the skills you want (for example, `product-positioning.zip`). To grab everything in one go, download `all-skills.zip` and unzip it once. You will get all of the individual skill `.zip` files inside, ready to upload as-is
3. In Claude, go to **Settings → Capabilities → Skills**, click **Upload skill**, and select the `.zip` for each skill you want to install

### For Claude Code Users

**Option 1: Ask Claude Code to install (simplest)**

If you already have Claude Code running, just paste this prompt:

```
Clone the marketing skills repo from https://github.com/realjaymes/marketingagentskills and copy all the skills from the skills/ folder into ~/.claude/skills/ so I can use them.
```

Claude will run the commands for you. Approve each step when prompted.

**Option 2: Terminal one-liner**

Open Terminal (search "Terminal" in Spotlight) and paste:

```bash
git clone https://github.com/realjaymes/marketingagentskills.git ~/Downloads/marketingagentskills && cp -r ~/Downloads/marketingagentskills/skills/* ~/.claude/skills/
```

**Option 3: Git submodule (for developers)**

```bash
git submodule add https://github.com/realjaymes/marketingagentskills.git .claude/marketingagentskills
```

---

## Usage

Once installed, just describe what you need in Claude Code. Claude will automatically use the relevant skill.

**Examples:**

- "Create positioning for my B2B SaaS product"
- "Build a messaging framework for our new feature launch"
- "Help me plan our Product Hunt launch"
- "Generate landing page copy for our homepage"
- "Create an ICP document for our target customers"
- "Design a lifecycle email campaign for trial users"
- "Build a Clay workflow for outbound prospecting"
- "Make this copy sound less like AI wrote it"

You can also invoke skills directly:

```
/product-positioning for a project management tool
/product-messaging for our AI writing assistant
/landing-page homepage for a B2B analytics platform
/icp-persona for enterprise software buyers
/experimentation design a pricing page test
```

---

## Skill Categories

### Strategy & Positioning
`portfolio-positioning` `product-positioning` `product-messaging` `product-marketing-metrics` `product-launch-gtm` `marketing-advantages`

### Content & Copy
`ad-creative` `landing-page` `saas-landing-pages` `press-release` `copy-anatomy` `ai-humanizer` `ai-content-generation`

### Research & Segmentation
`icp-persona` `customer-segments` `case-study-builder`

### Growth & Experimentation
`experimentation` `marketing-product-ideas` `performance-marketing` `lifecycle-marketing-campaigns` `product-onboarding-activation`

### SEO
`seo-audit`

### Automation & Technical
`clay-gtm-outbound` `n8n-automation` `openclaw` `remotion` `tweetclaw-social-automation` `vibe-coding`

### Meta Skills
`agent-skill-builder`

---

## Forks and Attribution

Some skills in this repo are enhanced forks of skills from other open marketing-skills repos. They are credited here, in the skill's `metadata.upstream` frontmatter, and in an `## Attribution` section inside the skill's `SKILL.md`.

| Skill | Upstream | Upstream Version Forked From | What's Added |
|---|---|---|---|
| [seo-audit](skills/seo-audit) | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills/tree/main/skills/seo-audit) | 2.0.0 | Comprehensive ~2,900-line SEO reference (`references/seo-comprehensive-reference.md`) covering technical, on-page, off-page, analytics, GEO/AEO, scenario playbooks, and the programmatic-API-first tool stack including DataforSEO. Preserved title-tag guidance noting that SERPs append brand names automatically. |

If you maintain an upstream skill listed here and want to discuss merging changes back, get in touch via the contact links below.

---

## Contributing

If you have feedback or think there's a skill that should be included, drop me a note on [Twitter/X](https://x.com/realjaymes) or [LinkedIn](https://www.linkedin.com/in/jamespraise).

---

## Find Me

- Website: [jamespraise.xyz](https://www.jamespraise.xyz)
- LinkedIn: [linkedin.com/in/jamespraise](https://www.linkedin.com/in/jamespraise)
- X (Twitter): [x.com/realjaymes](https://x.com/realjaymes)

## Find MIA

- MIA Website: [marketinginaction.xyz](https://marketinginaction.xyz)
- MIA Newsletter: [newsletter.marketinginaction.xyz](https://newsletter.marketinginaction.xyz/)
- MIA Academy: [marketinginaction.xyz/academy](https://marketinginaction.xyz/academy/)
- MIA Resources: [marketinginaction.xyz/resources](https://marketinginaction.xyz/resources/)

---

## License

MIT License. See [LICENSE](LICENSE) for details.
