# James Context Skill

Load James Praise's reference documents for positioning, messaging, and brand context.

---

## Invocation

- `/james-context` - Auto-detect relevant documents based on conversation context
- `/james-context all` - Load all reference documents
- `/james-context mia` - Load MIA positioning and messaging frameworks
- `/james-context services` - Load services positioning and messaging frameworks
- `/james-context personal` - Load personal story and press kit
- `/james-context press` - Load all press kits

---

## Document Mappings

| Argument | Documents |
|----------|-----------|
| `mia` | 2026 Positioning Framework _ MIA.pdf, 2026 Messaging Framework _ MIA.pdf, Marketing In Action (MIA) Press Kit.pdf, MIA Ecosystem Business Model.pdf |
| `services` | 2025 Positioning Framework _ James Product Marketing Services.pdf, 2025 Messaging Framework _ James Product Marketing Services.pdf, 2025 Positioning Framework _ James Praise x RealTalk.pdf |
| `personal` | James Praise (Personal Story).pdf, James Praise Press Kit.pdf |
| `press` | James Praise Press Kit.pdf, Marketing In Action (MIA) Press Kit.pdf |
| `voice` | Tweets _ Realjaymes.pdf |
| `business` | MIA Ecosystem Business Model.pdf |
| `all` | All documents listed above |

---

## Base Path

All documents are located at:
```
/Users/jamespraise/Documents/James Praise AI Context/
```

---

## Instructions

### Step 1: Determine Context Type

If an argument is provided, use it directly.

If no argument is provided, analyze the current conversation to determine relevance:

| Conversation Topic | Load |
|--------------------|------|
| Writing about MIA, Marketing In Action, the newsletter, academy, or resources | `mia` |
| Writing bios, about pages, speaker profiles, or press materials | `personal` + `press` |
| Writing about James's services, consulting, or client work | `services` |
| Matching voice, tone, or writing style | `voice` |
| MIA business model, revenue, pricing, or ecosystem strategy | `business` |
| Unclear or broad task requiring full context | `all` |

### Step 2: Read Documents

Read the PDF files that match the determined context type using the Read tool.

### Step 3: Summarize Loaded Context

After reading, provide a brief summary of what context is now available:

```
Loaded context:
- [Document name]: [1-line summary of key points]
- [Document name]: [1-line summary of key points]
```

### Step 4: Apply to Current Task

Use the loaded context to inform the response to the user's request. Reference specific positioning statements, messaging frameworks, or brand voice as appropriate.

---

## Full Document List

| File | Purpose |
|------|---------|
| 2026 Positioning Framework _ MIA.pdf | MIA's market position, differentiation, and strategic narrative |
| 2026 Messaging Framework _ MIA.pdf | MIA's key messages, value propositions, and proof points |
| MIA Ecosystem Business Model.pdf | MIA's business model, revenue streams, pricing, and ecosystem strategy |
| 2025 Positioning Framework _ James Product Marketing Services.pdf | James's services positioning and market differentiation |
| 2025 Messaging Framework _ James Product Marketing Services.pdf | Services messaging, value props, and client-facing language |
| 2025 Positioning Framework _ James Praise x RealTalk.pdf | RealTalk positioning framework |
| James Praise (Personal Story).pdf | James's background, journey, and personal narrative |
| James Praise Press Kit.pdf | Bio versions, headshots info, speaking topics, media contact |
| Marketing In Action (MIA) Press Kit.pdf | MIA brand info, press materials, media kit |
| Tweets _ Realjaymes.pdf | Examples of James's voice, tone, and writing style on social |

---

## Notes

- Always summarize what was loaded so the user knows what context is active
- For long documents, extract the most relevant sections rather than summarizing everything
- When writing copy, use the positioning and messaging frameworks as constraints, not just references
