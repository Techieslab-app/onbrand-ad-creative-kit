# Lovable Public Brand Test Creative Plan

Source of truth:

- `inputs/brand/brand.md`
- `inputs/brand/tokens.json`
- `inputs/design-rules/rules.md`
- `inputs/hooks/hooks.csv`
- `inputs/media/lovable-opengraph.png`

Public references:

- Lovable press/brand page: https://lovable.dev/brand
- Lovable public brand profile: https://brandfetch.com/lovable.dev

## Row L01 / 1x1

- Output: `outputs/1x1/lovable-public-brand-test-l01-build-your-app-by-chatting-with-ai-1x1.png`
- Size: `1080x1080`
- Persona: Founder
- Angle: Idea to shipped product
- Headline: `Build your app by chatting with AI`
- Support: `Go from rough idea to working product without waiting on a dev team`
- CTA: `Start building`
- Layout: product-led split
- Logo: top-left
- Palette: `#FCFBF8`, `#272725`, `#1E52F1`, `#F3702F`, `#EA8AAB`, `#FFFFFF`

Prompt used:

```text
Use case: ads-marketing
Asset type: 1:1 social ad creative, 1080x1080 square
Primary request: Create a polished Lovable brand ad for founders, using the supplied Lovable reference image only as brand/logo/style reference. The creative should look like a real product-led ad, not a generic AI poster.
Scene/backdrop: warm light background (#FCFBF8), clean modern software workspace, a crisp chat prompt transforming into a working app/web interface mockup.
Subject: Lovable product experience: chat on the left or upper-left, generated app preview on the right/lower-right, clear sense of idea-to-product.
Style/medium: high-craft raster marketing creative, clean SaaS product visual, rounded UI surfaces, subtle shadows, bright and calm.
Composition/framing: square 1080x1080, keep all important text inside a 96px safe margin. Lovable logo/wordmark top-left with generous clearspace. Headline upper-left/center-left, support below, CTA below support. Product UI mockup on right or lower half.
Lighting/mood: bright neutral daylight, optimistic, capable, approachable.
Color palette: use Lovable colors #FCFBF8 background, #272725 text, #1E52F1 primary blue, #F3702F coral accent, #EA8AAB pink accent, #FFFFFF surfaces.
Typography: friendly rounded geometric sans similar to Lovable/Camera Plain, 0 letter spacing, bold but not heavy headline.
Text (verbatim): headline "Build your app by chatting with AI" support "Go from rough idea to working product without waiting on a dev team" CTA "Start building"
Constraints: preserve the Lovable wordmark/logo appearance from the reference as accurately as possible; do not invent another logo; no robots, no dark cyberpunk, no stock people, no crypto motifs, no fake code rain, no watermark. Exact spelling is important.
```

QA notes:

- Pass: final PNG dimensions are `1080x1080` after resize.
- Pass: palette, background, primary blue CTA, and warm light software style are close to Lovable.
- Pass: logo is recognizable and placed top-left with adequate clearspace.
- Pass: headline, support copy, and CTA are readable and match the approved hook.
- Pass: product-led composition avoids generic AI tropes.
- Watch: generated UI content is invented (`Feedback Hub`) rather than sourced from approved Lovable product screenshots.
- Watch: the image generation tool initially returned `1254x1254`; post-processing was required before validator passed.

## Row L01 / 4x5

- Output: `outputs/4x5/lovable-public-brand-test-l01-build-your-app-by-chatting-with-ai-4x5.png`
- Size: `1080x1350`
- Persona: Founder
- Angle: Idea to shipped product
- Headline: `Build your app by chatting with AI`
- Support: `Go from rough idea to working product without waiting on a dev team`
- CTA: `Start building`

QA notes:

- Pass: final PNG dimensions are `1080x1350` after resize.
- Pass: logo, palette, CTA color, typography direction, and warm light background stay consistent with the 1x1 creative.
- Pass: text is more stable than the 1x1 output; headline, support, and CTA match the approved hook.
- Pass: layout adapts well to portrait feed instead of stretching the square design.
- Watch: generated product UI is invented (`Habit Tracker`) rather than sourced from approved Lovable product screenshots.

## Row L01 / 9x16

- Output: `outputs/9x16/lovable-public-brand-test-l01-build-your-app-by-chatting-with-ai-9x16.png`
- Size: `1080x1920`
- Persona: Founder
- Angle: Idea to shipped product
- Headline: `Build your app by chatting with AI`
- Support: `Go from rough idea to working product without waiting on a dev team`
- CTA: `Start building`

QA notes:

- Pass: final PNG dimensions are `1080x1920` after resize.
- Pass: brand shell is stable: logo, palette, CTA, headline hierarchy, and bright Lovable-like product aesthetic are consistent.
- Pass: story layout uses the extra height intentionally and keeps primary copy in safe zones.
- Watch: product UI drift is stronger than the feed outputs; the model invented a named app (`Trackly`) and several UI claims.
- Watch: this ratio would need approved product screenshots or stricter product-screen prompts before production use.

## Bundle Stability Verdict

- Stable: logo recognition, logo placement, background, palette, CTA treatment, headline, support copy, and overall Lovable-like SaaS polish.
- Moderately stable: layout adaptation across square, portrait feed, and story ratios.
- Not stable enough for production: generated in-product UI content. The model keeps inventing plausible sample apps and dashboard copy.
- Workflow issue: image generation outputs did not arrive at the exact target dimensions, so a resize/post-processing step is required before package validation.
- Recommendation: for production bundles, require approved product screenshots or UI references in `inputs/media/` and treat generated UI mockups as draft-only.

## Additional 1x1 Samples

### L02 / Product Manager

- Output: `outputs/1x1/lovable-public-brand-test-l02-turn-specs-into-working-tools-1x1.png`
- Headline: `Turn specs into working tools`
- Support: `Describe the workflow and let Lovable build the first version`
- CTA: `Start building`

QA notes:

- Pass: logo, headline, support, CTA, and palette are stable.
- Pass: product-led workflow/dashboard visual supports the PM angle.
- Watch: the dark prompt card feels heavier than Lovable's mostly light public brand shell.
- Watch: internal app content is invented and should be replaced with approved screenshots for production.

### L03 / Marketer

- Output: `outputs/1x1/lovable-public-brand-test-l03-launch-pages-without-the-wait-1x1.png`
- Headline: `Launch pages without the wait`
- Support: `Chat through the brief and get a polished page ready to test`
- CTA: `Start building`

QA notes:

- Pass: visually polished and recognizably aligned with the Lovable palette.
- Pass: marketing landing-page concept is clear.
- Watch: the outer rounded border makes it feel more like a framed mockup than a native social creative.
- Watch: generated UI includes fictional `Acme` content and unrelated customer logos.

### L04 / Founder

- Output: `outputs/1x1/lovable-public-brand-test-l04-your-idea-can-be-an-app-today-1x1.png`
- Headline: `Your idea can be an app today`
- Support: `Prompt, refine, and ship from one Lovable workspace`
- CTA: `Start building`

QA notes:

- Pass: strongest additional sample overall; brand shell, product transformation, and copy all hold together.
- Pass: clean Lovable-like composition without the heavy outer frame.
- Watch: still uses fictional product UI (`Launchpad`) rather than approved Lovable screenshots.

## Expanded Sample Verdict

- Stronger after more samples: the kit can produce multiple credible first-draft Lovable-style ads from lightweight public inputs.
- Stable across samples: logo usage, palette, CTA styling, large rounded headline typography, clean product-led SaaS aesthetic.
- Main drift pattern: the model invents app names, dashboard data, customer names, and UI details unless supplied screenshots are treated as mandatory.
- Production recommendation: add a `product_ui_mode` or similar field to the input contract with values like `approved_screenshot_only`, `stylized_reference`, and `invented_mockup_ok`.
