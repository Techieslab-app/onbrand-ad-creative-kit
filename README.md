# OnBrand Ad Creative Kit

A standardized package for turning brand inputs into on-brand ad creative batches across multiple ratios.

The intended workflow is:

```text
brand system + design rules + hook list + reference images
-> ad creative recipe skill
-> 1:1, 4:5, 9:16, and optional 16:9 ad creatives
```

This repo is designed for Codex + an image generation model. It should not render final ad creatives with HTML, SVG, canvas, or code unless the user explicitly asks for a mockup. Final creative assets should be raster image outputs from an image generation model, then QA'd against the brand and layout rules.

## Inputs

Put campaign inputs in `inputs/` or copy from `templates/`:

- `inputs/brand/brand.md` — brand system, voice, positioning, logo usage, typography direction.
- `inputs/brand/tokens.json` — color, type, spacing, CTA, and logo token values.
- `inputs/design-rules/rules.md` — layout rules, safe zones, visual do/don't list, platform constraints.
- `inputs/hooks/hooks.csv` — personas, hooks, headlines, support copy, CTA, offer notes.
- `inputs/hooks/personas.md` — persona notes and angle strategy.
- `inputs/media/` — logos, approved image library, product shots, venue photos, brand references.
- `inputs/ad-batch.yaml` — batch settings: ratios, output count, naming, offer, required copy fields.

## Outputs

Generated files should be organized by ratio:

```text
outputs/
|-- 1x1/     1080 x 1080
|-- 4x5/     1080 x 1350
|-- 9x16/    1080 x 1920
`-- 16x9/   1920 x 1080, optional
```

The default package target is 3 ratios:

- square: `1:1`
- portrait feed: `4:5`
- vertical story/reel: `9:16`

Optional:

- horizontal: `16:9`

## How To Use

1. Fill the files in `inputs/`.
2. Ask Codex: `Use the ad-creative-recipe skill in this repo to generate a prompt plan for this batch.`
3. Generate the ads with an image generation model.
4. Save files under `outputs/<ratio>/`.
5. Run:

```bash
python3 scripts/validate_outputs.py outputs
```

6. Review with `templates/qa-checklist.md`.

## Package Design

The package standardizes three things:

- **Brand lock:** the generated creative follows the supplied brand system, logo, palette, typography, and voice.
- **Layout lock:** each ratio uses safe-zone-aware composition rules, so headlines, CTAs, and mandatory details do not get cropped or covered.
- **Angle lock:** hooks are generated from personas and campaign strategy, not random generic ad copy.

## Example

`examples/foundersvn/` contains a sample campaign based on the FoundersVN dinner ads system. It is a reference example, not a hard-coded requirement for other brands.

## Skill Install

To install the reusable Codex skill locally:

```bash
cp -R skill/ad-creative-recipe ~/.codex/skills/
```

Then invoke it in any project that follows this input contract.
