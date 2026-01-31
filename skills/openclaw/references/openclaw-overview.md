# OpenClaw

**James Praise | Marketing In Action**

## What is OpenClaw?
OpenClaw is a free, open-source, privacy-first personal AI assistant that runs locally on your computer.
It keeps all data on your machine and integrates with chat platforms like WhatsApp, Telegram, Discord, Slack, Signal, and iMessage.

Created by **Peter Steinberger**.

## Key Features
- Runs 100% locally for privacy
- Multi-platform chat access
- Persistent memory
- Browser and system automation
- 50+ integrations
- Extensible skill system
- Supports Claude, GPT, and local models

## Prerequisites
- Node.js v22+
- macOS, Linux, or Windows (WSL2 recommended)
- Anthropic API key or Claude Pro/Max subscription
- Optional: Brave Search API key

## Installation

### Quick Install (Recommended)
macOS / Linux:
```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

Windows (PowerShell):
```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

### NPM Install
```bash
npm install -g openclaw@latest
```

## Initial Setup
Run the onboarding wizard:
```bash
openclaw onboard --install-daemon
```

This configures:
- Gateway
- AI model authentication
- Chat channels
- Background daemon

## Security Warnings
- OpenClaw can read files and run commands
- Use pairing, allowlists, and sandboxing
- Keep secrets out of reachable filesystems
- Run regular security audits

```bash
openclaw security audit --deep
```

## Connecting Chat Platforms
Supported platforms:
- WhatsApp
- Telegram
- Discord
- Slack

Pairing approval is required for new users.

## Basic Usage
```bash
openclaw agent --message "Plan my week"
```

Supports higher reasoning modes:
```bash
openclaw agent --message "Summarize my emails" --thinking high
```

## Configuration
Main config file:
```json
~/.openclaw/openclaw.json
```

Example:
```json
{
  "agent": {
    "model": "anthropic/claude-opus-4-5"
  }
}
```

## OpenClaw Skills
Skills extend OpenClaw capabilities using `SKILL.md` files with YAML frontmatter.

### Skill Loading Order
1. `<workspace>/skills`
2. `~/.openclaw/skills`
3. Bundled skills

### Skill Requirements
- Required binaries
- Environment variables
- Config paths
- OS restrictions

## ClawdHub
ClawdHub is the public skill registry.

Key commands:
```bash
clawdhub search "spotify"
clawdhub install spotify-controller
clawdhub publish ./my-skill
```

## Best Practices
- Treat third-party skills as trusted code
- Inject secrets via environment variables
- Use sandboxing for untrusted inputs

## Troubleshooting
- Gateway issues: `openclaw gateway --verbose`
- Auth errors: rerun onboarding
- Dashboard: ensure gateway is running

## Quick Start (5 Minutes)
1. Install OpenClaw
2. Run onboarding
3. Connect a chat platform
4. Open dashboard
5. Install ClawdHub
6. Install a skill
7. Restart gateway
8. Start chatting
