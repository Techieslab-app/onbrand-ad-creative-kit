# Input Contract

## `brand.md`

Should explain:

- brand name and offer
- target audience
- positioning
- voice and tone
- visual feeling
- logo rules
- typography direction
- image style
- hard avoids

## `tokens.json`

Recommended fields:

```json
{
  "brand": {
    "name": "Brand Name",
    "tagline": "Optional tagline"
  },
  "colors": {
    "primary": "#000000",
    "text_on_dark": "#ffffff",
    "accent": "#ff3366",
    "secondary": "#999999"
  },
  "typography": {
    "display": "Geometric sans",
    "body": "Inter",
    "rules": ["No condensed poster fonts", "No negative letter spacing"]
  },
  "logo": {
    "primary": "inputs/media/logo.svg",
    "safe_position": "top-left"
  },
  "cta": {
    "style": "rounded pill",
    "default_text": "Apply now"
  }
}
```

## `rules.md`

Should define:

- safe zones
- logo placement
- headline/support/CTA placement
- image selection rules
- image styles to avoid
- ratio-specific layout requirements
- whether generated imagery is allowed or only reference-library imagery

## `hooks.csv`

Required columns:

```csv
id,persona,angle,headline,support,cta,offer_notes
```

Optional columns:

```csv
language,reference_image,layout_hint,priority,status
```

## `ad-batch.yaml`

Recommended fields:

```yaml
campaign:
  name: campaign-name
  offer: short offer
ratios:
  - id: 1x1
    size: 1080x1080
  - id: 4x5
    size: 1080x1350
  - id: 9x16
    size: 1080x1920
outputs:
  folder: outputs
  naming: "{campaign}-{hook_id}-{slug}-{ratio}.png"
```
