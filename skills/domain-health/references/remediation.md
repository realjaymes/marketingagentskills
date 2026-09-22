# Remediation by Failure Mode

## No SPF record

Add one TXT record at the apex. There must be exactly one SPF record on a domain. Two records is a PermError and SPF fails entirely, which is worse than having none.

Start permissive and tighten once the sender inventory is confirmed:

```
v=spf1 include:<provider> ~all
```

## SPF over the ten-lookup limit

Every `include`, `a`, `mx`, `exists`, `ptr` and `redirect` triggers a DNS lookup, and nested includes count too. Past ten, receivers return PermError and SPF fails for all mail.

Remove includes for services no longer in use, which the sender inventory surfaces. Where a provider offers a flattened or dedicated include, use it. Avoid SPF flattening services that rewrite the record on a schedule, since they fail silently when the provider changes IPs.

## SPF ends in ~all or ?all

`~all` is soft fail, `?all` is neutral and asserts nothing. Move to `-all` only after the sender inventory is confirmed and reports show no legitimate sender failing, because `-all` is what turns an unlisted sender into a delivery failure.

## No DKIM found

DKIM is per-provider. Each sending service publishes its own key and selector, so this is configured once per service, not once per domain.

**Google Workspace.** Admin console, Apps, Google Workspace, Gmail, Authenticate email. Generate, then publish the TXT record on selector `google`.

**Microsoft 365.** Defender portal, Email authentication settings, DKIM. Publishes two CNAMEs on `selector1` and `selector2`.

**Zoho.** Mail Admin console, Domains, the domain, Email Configuration, DKIM. Default selector is `zmail`.

**Brevo.** Senders and domains, Domains, Authenticate. Publishes a DKIM record plus its own SPF include. Verifying a domain in Brevo does **not** add it to SPF, which is the gap the sender inventory is built to catch.

**SendGrid.** Sender Authentication, Authenticate Your Domain. Publishes CNAMEs on `s1` and `s2`.

**Mailgun.** Sending, Domains, DNS records. Selector varies by account.

**Amazon SES.** Verified identities, DKIM. Uses three CNAMEs with per-account random selectors, which is why a selector sweep will never find SES.

**Mailchimp, Postmark, Klaviyo, HubSpot.** Each has an authentication or sending-domain section that emits the required records. Follow it rather than hand-writing anything.

## DMARC missing

Start at monitoring with reports pointed somewhere readable:

```
v=DMARC1; p=none; rua=mailto:<report-reader-address>
```

Do not start at quarantine or reject. See `dmarc-rollout.md`.

## DMARC reports going to a human mailbox

Aggregate reports are gzipped XML. Repoint `rua` at a report reader. This is the single highest-value change on most domains, because it converts an unread setting into actual information.

## sp=none with a stronger apex policy

Subdomains are a common spoofing target precisely because they are forgotten. Set `sp=` to match `p=`, or remove `sp=` entirely so subdomains inherit.

## Forwarding breaks SPF

SPF alignment does not survive forwarding, DKIM does. A domain relying on SPF alone will see forwarded mail fail DMARC. This is a strong argument for configuring DKIM on every sender rather than treating SPF as sufficient.

## Cloudflare Email Routing

This forwards inbound mail and does not send. A domain using it for receiving still needs a separate configured sender for outbound, and its SPF include covers forwarding only.
