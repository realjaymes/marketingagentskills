# Account Safety & Ban Recovery (across ad platforms)

The **account-behaviour** layer of ad-policy survival — how you *run and structure the account*, distinct from the **creative/copy** layer (policy-compliant messaging, handled in-copy and in the platform playbooks). Most platforms suspend for account behaviour as readily as for creative; this is the discipline that prevents it and the protocol that recovers from it. Universal first, then platform notes where they differ.

## Universal prevention — account hygiene (all platforms)

- **Warm up new accounts.** Don't run aggressive conversion campaigns on a brand-new account / page / pixel / business. Build history first (organic activity, then a low-stakes engagement or traffic campaign), start spend low, and scale gradually (≈ ≤20–30% every 48–72h). A cold account taking sudden high spend is a near-universal risk signal — sharpest on Meta and TikTok.
- **Payment-method discipline.** One stable, verified method whose billing name matches the account/business. Don't rotate or stack methods; repeated failures or name mismatches flag risk. Google and Meta both tie account trust to billing stability.
- **One identity, kept consistent.** One business → one clean account structure; don't share or spin accounts across people or device-fingerprints. Platforms link by device/IP/browser/business entity. After a ban, never rebuild on the same fingerprint — it gets re-caught and compounds the flag.
- **Login + access hygiene.** Stable login geography (careful with VAs/VPNs hopping countries), 2FA on, and proper user roles via the platform's business layer (Meta Business Manager / Google MCC / TikTok Business Center) rather than password-sharing.
- **Asset & claim sourcing.** Use owned / licensed / AI assets; never lift a competitor's creative or copyrighted media. Keep claims substantiable — especially in the regulated "special categories" (health, finance/credit, employment, housing).
- **Declare special ad categories.** Housing, employment, credit, and (some platforms) social/political require the special-category declaration + restricted targeting. Mis-declaring to dodge the restriction is a fast suspension.

## Platform-specific notes

- **Meta (FB/IG)** — strictest on warm-up, spend pacing, and (for NG financial offers) the income classifier. Page quality *and* account quality both matter, and restrictions cascade across linked assets. Recover via **Account Quality → request review**.
- **Google Ads** — suspensions skew to **policy strikes** (a 3-strike system for some violations), **suspicious payment**, and **misrepresentation** (the hardest to lift — about business/destination transparency). Landing-page integrity and **advertiser identity verification** matter more here than on Meta.
- **TikTok** — slow, semi-human review; income / health / "get-rich" claims and the **≤89-char disclaimer** rule (handled in-copy) are the usual creative trips. New accounts must warm up; aggressive scaling forces re-review.
- **LinkedIn** — stricter B2B content standards and higher minimum spend; less behaviour-ban-happy, but rejects off-tone/consumer-style creative. Account issues are usually billing or identity.
- **Snapchat / X / Reddit / YouTube** — lighter behaviour policing; main risks are creative-policy + payment. YouTube inherits Google's policy stack and verification.

## Recovery — the universal protocol (any platform)

When an ad is rejected or an account is restricted:

1. **Read the actual reason** in the platform's policy/quality center — never guess.
2. **Diagnose the layer** — creative / copy / landing page (→ fix the message or destination per the platform playbook) **vs** account behaviour (→ this file: warm-up, payment, identity, fingerprint).
3. **Fix the cause, then resubmit ONCE.** Resubmitting an *unchanged* ad reads as circumventing enforcement and can escalate to an account-level flag. Change something real first.
4. **If still rejected, appeal / request review** with a short, factual explanation. Don't spam resubmissions.
5. **Log it** — what tripped, what fixed it — so the trigger doesn't recur (feeds the trigger-word / policy bank).

**Account suspended/disabled:** request review through the official flow **once**, calmly; don't open a new account on the same fingerprint while under review; resolve any payment / identity / business-verification mismatch **before** appealing. The hardest suspensions — Google "misrepresentation," Meta "circumventing systems" — are won with **transparency** (a real, verifiable business + a clear, honest destination), not with volume of appeals.

## Where this sits

Read **before scaling spend** and **at any rejection**, alongside the creative/policy compliance in `performance-marketing-playbook.md`. It complements — never replaces — message-level compliance.
