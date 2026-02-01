# Marketing Agent Skills

20 AI agent skills for marketing tasks, built for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and similar AI coding assistants (Cursor, Windsurf, Cline, Roo Code).

---

I'm [James](https://www.jamespraise.xyz), founder of [Marketing In Action](https://marketinginaction.xyz) and a Product & Growth Marketing consultant with close to a decade of startup experience. I've been a founding marketer multiple times, building marketing functions and systems from scratch.

I am currently experimenting with vibe coding, and this is one of the projects I'm building with that knowledge.

This repo is the Claude skills version of the [MIA Resources](https://marketinginaction.xyz/resources/) I have developed:

1. **Product Marketing Templates & Resources Library**: 50+ Product & Growth Marketing templates, frameworks, and resources to execute marketing with clarity.
2. **AI Prompt Frameworks & Templates for Marketers**: 50+ frameworks and templates that marketers and founders use to produce consistent, high-quality outputs from AI tools like ChatGPT Projects, Claude Projects, Gemini Gems, Custom GPTs & OpenAI Assistants.

These skills make it easier to unify and apply the knowledge and prompts from the knowledge files and custom GPTs/prompts.

You can also check out the vibe-coded repo of the MIA website here: [github.com/realjaymes/marketinginaction](https://github.com/realjaymes/marketinginaction)

---

## What are Skills?

Skills are markdown files that give AI agents specialized knowledge to execute specific marketing tasks. Each skill contains frameworks, best practices, and structured approaches that help Claude produce better, more consistent outputs for marketing work.

---

## Available Skills

| Skill | Description |
|-------|-------------|
| [agent-skill-builder](skills/agent-skill-builder) | Create new Claude skills from scratch or translate ChatGPT GPT projects into the Claude skill format |
| [ai-humanizer](skills/ai-humanizer) | Detect AI-written text, provide line-by-line recommendations, and rewrite content to sound genuinely human |
| [case-study-builder](skills/case-study-builder) | Create professional case studies, engagement summaries, and project summaries |
| [clay-gtm-outbound](skills/clay-gtm-outbound) | Design and optimize Clay-powered GTM workflows for prospecting, signal detection, and outbound automation |
| [copy-anatomy](skills/copy-anatomy) | Reverse-engineer copy into reusable templates by identifying core components and extracting frameworks |
| [customer-segments](skills/customer-segments) | Create customer and user segment documents divided by traits, behaviors, and lifecycle stages |
| [experimentation](skills/experimentation) | Design, prioritize, execute, and review growth experiments using the ICEEE framework |
| [icp-persona](skills/icp-persona) | Generate ICP and buyer/user persona documents for B2B and B2C products |
| [landing-page](skills/landing-page) | Create landing page copy using modular section templates for homepages, feature pages, and campaigns |
| [lifecycle-marketing-campaigns](skills/lifecycle-marketing-campaigns) | Create lifecycle marketing campaign flows for SaaS, digital products, and service businesses |
| [marketing-product-ideas](skills/marketing-product-ideas) | Generate marketing and product ideas grounded in behavioral principles and proven PLG experiments |
| [n8n-automation](skills/n8n-automation) | Design, build, debug, and document n8n workflows and AI agent automations |
| [openclaw](skills/openclaw) | Design, build, debug, and document OpenClaw workflows and AI assistant configurations |
| [performance-marketing](skills/performance-marketing) | Plan, review, and optimize paid campaigns across Google, Meta, LinkedIn, TikTok, YouTube, Reddit, X, Snapchat |
| [press-release](skills/press-release) | Create complete press release packages with newsworthiness evaluation and multiple headlines |
| [product-launch-gtm](skills/product-launch-gtm) | Guide end-to-end product and feature launch planning with launch sizing, GTM strategy, and success measurement |
| [product-messaging](skills/product-messaging) | Create complete messaging frameworks including value propositions, taglines, and elevator pitches |
| [product-positioning](skills/product-positioning) | Create complete positioning frameworks with target customers, competitive differentiation, and market categories |
| [saas-landing-pages](skills/saas-landing-pages) | Generate complete SaaS landing page drafts using 7 framework templates for different page types |
| [vibe-coding](skills/vibe-coding) | Guide beginner-to-intermediate developers through web development, Claude skills creation, and AI-assisted coding |

---

## Installation

### For Claude Code Users

**Option 1: Download and Copy (Easiest)**

1. Click the green **Code** button above, then **Download ZIP**
2. Unzip the downloaded file
3. Open Finder and press `Cmd + Shift + G`, then paste: `~/.claude/skills/`
4. Copy the folders from the `skills` folder in the unzipped download into this location

**Option 2: Using Terminal**

Open Terminal (search "Terminal" in Spotlight) and paste these two lines:

```bash
git clone https://github.com/realjaymes/marketingagentskills.git ~/Downloads/marketingagentskills
cp -r ~/Downloads/marketingagentskills/skills/* ~/.claude/skills/
```

### For Developers

```bash
# Clone and install
git clone https://github.com/realjaymes/marketingagentskills.git
cp -r marketingagentskills/skills/* ~/.claude/skills/

# Or add as a git submodule
git submodule add https://github.com/realjaymes/marketingagentskills.git .claude/marketingagentskills
```

### For Claude Web & Desktop App

Claude Code skills can also be used in the web app (claude.ai) and desktop app:

1. Go to **Settings → Capabilities → Skills**
2. Upload your skills in one of two formats:
   - **Single skill**: Upload the `SKILL.md` file directly
   - **Multiple skills**: Zip the `skills` folder and upload the `.zip` file

To get the skills, either download this repo or locate your installed skills at `~/.claude/skills/`

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
`product-positioning` `product-messaging` `product-launch-gtm`

### Content & Copy
`landing-page` `saas-landing-pages` `press-release` `copy-anatomy` `ai-humanizer`

### Research & Segmentation
`icp-persona` `customer-segments` `case-study-builder`

### Growth & Experimentation
`experimentation` `marketing-product-ideas` `performance-marketing` `lifecycle-marketing-campaigns`

### Automation & Technical
`n8n-automation` `openclaw` `clay-gtm-outbound` `vibe-coding`

### Meta Skills
`agent-skill-builder`

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
