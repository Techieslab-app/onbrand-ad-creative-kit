# Imagegen Prompt Template

Use the image generation model. Do not render final ad creatives as HTML, SVG, canvas, or code.

Create a `[BRAND]` ad creative in `[RATIO]`, exactly `[WIDTH] x [HEIGHT]` px.

Use these input files:

- Logo reference: `[LOGO_PATH]`
- Brand system: `[BRAND_MD_PATH]`
- Design rules: `[RULES_MD_PATH]`
- Reference image: `[REFERENCE_IMAGE_PATH]`

Brand constraints:

- Palette: `[PALETTE]`
- Type direction: `[TYPE_DIRECTION]`
- Voice: `[VOICE]`
- Visual feel: `[VISUAL_FEEL]`
- Hard avoids: `[AVOIDS]`

Copy:

- Headline, spelled exactly: `[HEADLINE]`
- Support, spelled exactly: `[SUPPORT]`
- CTA, spelled exactly: `[CTA]`
- Mandatory details, if any: `[MANDATORY_DETAIL_LINE]`

Layout:

- Follow `[RATIO]` safe-zone rules from `[RULES_MD_PATH]`.
- Keep headline, support, CTA, and mandatory details grouped in the safe visual area.
- Keep the logo in the approved position.
- Preserve the same creative idea across ratios, but adapt composition to the canvas.
- Use the approved reference image as the visual base or primary inspiration.

Output filename:

`[OUTPUT_FILENAME]`
