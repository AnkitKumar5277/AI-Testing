### 🤖 Agent Skill kya hoti hai?

Simple language mein:

**Skill = AI agent ko kisi specific kaam ko consistently karne ke liye diye gaye instructions.**

Example:
Agar tumne AI ko baar-baar samjhaya hai:

> “Bug report hamesha Summary → Steps → Expected → Actual → Environment format mein banana.”

Toh ye ek **Skill** banane ke liye perfect candidate hai.

Course ka simple rule hai:

**Jo cheez tumne 3 baar explain kar di → usko Skill banane ke baare mein socho.** 

---

## 📁 Skill ka structure

Ek skill basically ek folder hota hai:

```text
.claude/
└── skills/
    └── flaky-triage/
        └── SKILL.md
```

`SKILL.md` ke 2 main parts hote hain:

1. **Frontmatter** → Skill **kab activate hogi**
2. **Body** → Skill activate hone ke baad **kya karna hai** 

Yaad rakho:

> **Frontmatter = WHEN**
> **Body = WHAT/HOW**

---

# 🧠 Sabse important concept: Context

Claude startup par skill ka **poora content load nahi karta**.

Initially sirf:

```text
Skill name
+
Skill description
```

context mein hota hai.

Jab user ki request description se match karti hai, tab **poora SKILL.md load hota hai**. 

### Example

Skill:

```yaml
description: Diagnose flaky tests. Use when tests
fail intermittently or pass locally but fail in CI.
```

User:

> "Ye test locally pass ho raha hai but CI mein randomly fail ho raha hai."

AI description ko match karega → **flaky-triage skill activate**.

### 🔥 Interview point

**Skill trigger hone ke decision ke time AI ne body nahi padhi hoti.**

Isliye:

> **Description is the trigger.**

Agar description weak hai, chahe `SKILL.md` ke andar 500 lines ki amazing information ho, skill automatically trigger nahi hogi. 

---

# ✍️ Description kaise likhein?

❌ Weak:

```yaml
description: Helps with testing.
```

AI ko pata hi nahi chalega kab use karna hai.

✅ Better:

```yaml
description: Writes pull request descriptions in the team format.
Use when creating a PR, writing a PR, summarising changes
on a branch, or when asked what changed since main.
```

Matlab description mein 2 cheezein honi chahiye:

**1. Skill kya karti hai?**
**2. Kis situation mein use karni hai?** 

---

# 📍 Skills kahan rakhi ja sakti hain?

4 main levels:

| Level      | Location            | Scope                    |
| ---------- | ------------------- | ------------------------ |
| Enterprise | Managed settings    | Puri organisation        |
| Personal   | `~/.claude/skills/` | Tumhare all projects     |
| Project    | `.claude/skills/`   | Current repository       |
| Plugin     | Plugin ke andar     | Jahan plugin enabled hai |

Priority:

**Enterprise > Personal > Project**

Plugin skills namespace use karti hain, jaise:

```text
plugin-name:skill-name
```

isliye normal skills ke saath name collision nahi karti. 

---

# 📝 Frontmatter

Portable **Agent Skills specification** ke according:

### Required:

```yaml
name:
description:
```

`name`:

* 1–64 characters
* lowercase
* numbers allowed
* hyphens allowed
* parent folder ke naam se match hona chahiye

`description`:

* 1–1024 characters

Optional fields:

```yaml
license:
compatibility:
metadata:
allowed-tools:
```



### ⚠️ Important difference

**Agent Skills specification** mein `name` aur `description` required hain.

Lekin **Claude Code** mein frontmatter fields optional hain; `description` recommended hai aur `name` directory name se default ho sakta hai. 

---

# 🚨 `allowed-tools` ka important correction

Ye exam/interview ke liye important hai.

❌ Galat understanding:

> `allowed-tools` = Claude ko sirf in tools tak restrict karta hai.

Actually:

> **`allowed-tools` listed tools ko permission prompt ke bina pre-approve karta hai.**

Agar tools ko restrict karna hai:

```yaml
disallowed-tools:
```

use karo. 

---

# 📚 Progressive Disclosure

Agar `SKILL.md` bahut bada ho gaya, maan lo:

```text
2000 lines
```

toh problem hogi.

Better structure:

```text
flaky-triage/
│
├── SKILL.md
├── scripts/
│   └── rerun.sh
├── references/
│   └── retry-patterns.md
└── assets/
    └── template.json
```

### Meaning:

**SKILL.md**
→ main instructions + pointers

**references/**
→ detailed documentation

**scripts/**
→ executable code

**assets/**
→ templates/data



### 500-line rule

`SKILL.md` ko roughly **500 lines se neeche** rakhna recommended hai.

Aur important trick:

> Script ko **read** karne ke bajaye **run** karo.

Script ka code context mein load nahi hota; uska **output** context mein aata hai. Isse tokens save hote hain. 

---

# ⚔️ Skill vs CLAUDE.md vs Hook vs Subagent vs MCP

Ye bahut important table hai:

| Mechanism     | Simple meaning                       |
| ------------- | ------------------------------------ |
| **CLAUDE.md** | Always-on instructions               |
| **Skill**     | Task-specific expertise              |
| **Hook**      | Event hone par automatically execute |
| **Subagent**  | Separate/isolated context mein kaam  |
| **MCP**       | External systems/tools se connect    |

Example QA project:

```text
CLAUDE.md
→ fixtures/golden ko edit mat karo

Skill
→ Accessibility testing checklist

Hook
→ Har save par linter run karo

Subagent
→ Large refactor investigate karo

MCP
→ Jira ticket fetch karo
```



### Ek line mein yaad karo:

**CLAUDE.md = Always**

**Skill = Sometimes**

**Hook = Event**

**Subagent = Isolation**

**MCP = External system**

---

# 🤖 Skills + Subagents

Sabse important trap:

> **Subagents tumhari skills automatically inherit nahi karte.**

Agar tum main conversation mein skill use kar rahe ho aur phir task ko subagent ko delegate kar diya, subagent ke paas woh skill automatically nahi hogi. 

Custom subagent mein explicitly:

```yaml
skills:
  - accessibility-audit
  - performance-check
```

dene par skills startup par **full inject** hoti hain. 

### `context: fork`

Ye opposite direction hai.

```yaml
context: fork
```

ka matlab skill khud **subagent context** mein run ho sakti hai. 

Yaad rakho:

> **skills field → skills ko subagent mein laata hai**
> **context: fork → skill ko subagent mein bhejta hai**

---

# 👥 Team mein Skill share karna

3 main methods:

### 1. Git

```text
.claude/skills/
```

repo mein commit karo.

Jo repo clone karega, skill mil jayegi.

### 2. Plugin

Skill ko plugin ke andar package karo.

Dusri teams install kar sakti hain.

### 3. Enterprise Managed Settings

Organisation-wide mandatory rules ke liye.

Priority sabse high:

**Enterprise > Personal > Project** 

---

# 🐛 Troubleshooting

Agar skill kaam nahi kar rahi:

| Problem                       | Pehle kya check karein   |
| ----------------------------- | ------------------------ |
| Skill fire nahi hoti          | `description`            |
| Skill list mein nahi hai      | Folder/`SKILL.md`/YAML   |
| Wrong skill fire hoti hai     | Overlapping descriptions |
| Tumhari skill ignore hoti hai | Priority                 |
| Plugin skill missing          | Plugin structure/cache   |
| Skill crash hoti hai          | Runtime/dependency       |



Validator:

```bash
claude plugin validate ~/.claude/skills
```

ya:

```bash
claude plugin validate .claude/skills
```

Portable skills ke liye:

```bash
skills-ref validate ./my-skill
```



---

# 🧪 QA Engineer ke liye real Skill example

Suppose tumhare project mein flaky tests hain.

```text
.claude/
└── skills/
    └── flaky-triage/
        └── SKILL.md
```

Frontmatter:

```yaml
---
name: flaky-triage
description: Diagnose and classify a flaky test. Use when a test
passes locally but fails in CI, when a test fails intermittently,
or when someone says a test is flaky.
---
```

AI ko instructions:

```text
1. Test ko 20 times isolated run karo.
2. Full suite mein 20 times run karo.
3. Passing aur failing traces compare karo.
4. Root cause classify karo:
   - timing
   - ordering
   - shared data
   - environment
5. Smallest fix propose karo.
6. Blind retry ya timeout increase mat suggest karo.
```

Ye exactly wahi type ka **repeatable QA workflow** hai jo Skill mein convert karna useful hai. 

---

# 🎯 Interview ke liye 10-second revision

Agar interviewer puche **"Agent Skill kya hai?"**

> **Agent Skill ek reusable set of instructions hai jo AI agent ko specific task ke liye expertise provide karta hai. Skill ka description decide karta hai ki skill kab trigger hogi, aur SKILL.md ka body batata hai ki activate hone ke baad kya karna hai.**

### Aur ye 8 points yaad rakho:

1. **Skill = reusable expertise**
2. **`SKILL.md` = main file**
3. **Description = trigger**
4. **Body = instructions**
5. **Names + descriptions initially context mein**
6. **Progressive disclosure = detail only when needed**
7. **Skill ≠ Hook ≠ Subagent ≠ MCP**
8. **Subagents skills automatically inherit nahi karte** 
