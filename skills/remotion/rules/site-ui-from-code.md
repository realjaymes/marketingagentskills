---
name: site-ui-from-code
description: Show a real website's UI in a video, built from the site's own HTML and CSS, with real outputs
metadata:
  tags: product-demo, screen, website, tool, calculator, playwright, iframe, capture
---

# Real site UI from the site's own code

Use this when a video shows a product, tool, calculator, quiz or page from one of our sites. The UI on screen must match the live site exactly, and every result shown must be one the live tool produced. Never redraw a site's UI by hand in JSX, and never invent a result.

## Pick the route

| The product is built in... | Route |
| --- | --- |
| React (or another component library Remotion can import) | Import the real components into the Remotion project with the product's own stylesheet, and drive their props from `useCurrentFrame()`. Feed them real data captured from the live product |
| Plain HTML, CSS and JavaScript (a static marketing site or tool) | **Capture and rebuild** with the site motion kit, below |
| Anything, when the real behaviour itself is the point (a live search, a loading state) | **Screen recording**: the kit's capture job with `"record": true` writes a real recording, and Remotion adds motion on top with `<OffthreadVideo>` |

## The site motion kit

The kit is a small Remotion project plus a Playwright capture script. The parts below are what to build.

1. **Run the site locally.** Its server and port are listed in `sites.json`. Add a site there first if it is new: `repo`, `base`, `locale`, `timezone` and the selectors to `hide`.
2. **Write a capture job** in `jobs/<name>.json`, listing the page path, the phone viewport, a fixed `now` for date-based tools, the states with their steps (`fill`, `select`, `click`, `type`, `check`, `scroll`, `wait`, `eval`) and the `rects` to measure.
3. **Capture it:** `node scripts/capture.mjs jobs/<name>.json`. A headless browser runs the steps on the live page and saves each state's real HTML to `src/captures/<name>.json`. It copies the exact CSS, fonts and images into `public/sites/<site>/`. It also writes a screenshot per state to `captures/<name>/`, and a recording if asked. Analytics and ad pixels are blocked, scripts are stripped from the saved HTML, and form values are written into the HTML.
4. **Build the video** in `src/videos/`. Wrap the page in `<Phone>` and `<SitePage capture state scrollY apply>`:
   - `<SitePage>` renders the captured HTML in an iframe with the site's own stylesheets, so the site's CSS applies exactly as on the live site and never leaks into the video's own text.
   - It switches off the page's CSS transitions and animations, because time-based motion renders unpredictably frame by frame.
   - `apply(doc, frame)` changes the page for each frame: set an input's value, swap in a result with `fragmentFrom(capture, 'result', '#res')`, or set an inline opacity or transform. It must depend only on `frame`.
   - `boxOf(capture, state, selector)` gives element positions for scroll targets and `<Tap>` markers.
   - To change many numbers at once, stack two `<SitePage>` states and crossfade them.
5. **Check it:** render stills with `npx remotion still`, and compare them with the capture screenshots. Then render the video.

## Rules

- Every value on screen comes from a capture of the live tool. If the inputs change, recapture.
- Set the job's `locale` to the audience's (for example `en-GB`). A date input shows the browser's own locale format, so replace it with a text input showing the audience's format.
- Recapture after any site change to the page, so the video never shows an old UI.
- Captions, titles and end cards are drawn outside the iframe in the brand fonts, loaded with `loadFontCss`.
- Two patterns cover most videos: one captured state with frame-driven changes (a date typed, a result revealed), or two captured states crossfaded (a calculator before and after a new input).
