# dudulabs site — DESIGN.md

Based on the Apple web design language (VoltAgent/awesome-design-md `apple`), adapted for a one-person app studio.
This file is the only design reference for this site. Change this file first if the site needs to look different.

## Idea
The apps are the product. Like a gallery: the wall disappears, the app screens take over.
Each app gets a full-width section with its name, one line, two links and a real screenshot.

## Not allowed (things that make it look AI-generated)
- Emoji icons, feature trios ("3 columns: icon + title + sentence"), "How we build" value grids
- Gradients, glow, glassmorphism, neon, decorative blobs
- Shadows on cards, buttons or text
- Grey rounded "cards" everywhere; badges on every card
- Slogans that say nothing ("Creative ideas, elegant solutions", "작고 정직한…")
- A second accent colour

## Colours
| token | hex | use |
|---|---|---|
| ink | #1d1d1f | all text on light |
| canvas | #ffffff | default section |
| parchment | #f5f5f7 | alternate section, footer |
| tile-dark | #000000 / #272729 | dark section (Muscle Memory, its app is dark) |
| muted | #6e6e73 | secondary text |
| hairline | #d2d2d7 | 1px dividers |
| action | #0066cc | every link and button on light |
| action-on-dark | #2997ff | links on dark sections |

## Type
System font (SF Pro on Apple devices): `-apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", system-ui`.
| role | size / weight / line-height / tracking |
|---|---|
| section headline | 48px (mobile 36) / 600 / 1.08 / -0.02em |
| tagline | 24px (mobile 21) / 400 / 1.25 |
| body | 17px / 400 / 1.47 / -0.01em |
| caption | 14px / 400 |
| nav | 12–13px / 400 |
Weights: 400 and 600 only.

## Layout
- Sections are full-bleed, edge-to-edge, no gap. The colour change is the divider.
- Section padding: 80px top (mobile 56), screenshots bleed into the bottom edge.
- Text centred above screenshots on the home page.
- Max text width 680px; documents (privacy) 680px, left aligned.

## Components
- **Global nav**: 44px, black, white 12–13px links, wordmark left, language toggle right. Under 480px only wordmark + language.
- **Screenshots on mobile**: at most 2 side by side.
- **Links pair**: primary = blue pill (#0066cc, white text, 980px radius, 8×18px padding); secondary = text link "Learn more ›".
- **Screenshot**: real simulator capture, iPhone rounded corners, one soft shadow `0 20px 60px rgba(0,0,0,.18)` (the only shadow allowed).
- **FAQ**: hairline list, no boxes.
- **Footer**: parchment, 12px muted text, links separated by hairlines.

## Copy
- Short and concrete. Say what the app does, not how we feel.
- EN + KO on every page; language follows the device, toggle in nav.
- Never say "Coming soon" more than once per app (use one small line under the links).
