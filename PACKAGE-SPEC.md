# Package Spec

## Purpose

This package lets a team provide brand/campaign inputs and receive consistent multi-ratio ad creatives from one standardized workflow.

## Required Inputs

| File | Purpose |
|---|---|
| `inputs/brand/brand.md` | Brand narrative, voice, audience, typography, logo rules, visual world |
| `inputs/brand/tokens.json` | Machine-readable colors, typography, CTA, logo, spacing and ratio tokens |
| `inputs/design-rules/rules.md` | Creative constraints, safe zones, composition rules, image rules |
| `inputs/hooks/hooks.csv` | Persona, angle, headline, support, CTA and offer rows |
| `inputs/ad-batch.yaml` | Batch settings and requested ratios |
| `inputs/media/` | Logo files, reference images, product shots, approved campaign imagery |

## Standard Outputs

| Ratio | Size | Folder |
|---|---:|---|
| `1x1` | `1080x1080` | `outputs/1x1/` |
| `4x5` | `1080x1350` | `outputs/4x5/` |
| `9x16` | `1080x1920` | `outputs/9x16/` |
| `16x9` | `1920x1080` | `outputs/16x9/` |

## Batch Formula

```text
personas x hooks per persona x ratios = total creatives
```

Example:

```text
5 personas x 10 hooks x 3 ratios = 150 creatives
```

## Invariants

- Logos come from the approved input files.
- Colors come from `tokens.json`.
- Layout follows `rules.md`.
- Image references come from `inputs/media/`.
- Headlines and CTAs stay inside safe zones.
- Every ratio keeps the same creative concept but adapts the layout to the canvas.
