# Project Context: Veiled Privacy Protocol (Robinhood Chain & Pons Family)

> **Purpose**: This file provides complete orientation for any AI agent or developer continuing work on this project in a new conversation.

---

## 1. Project Overview & Identity

* **Project Name**: Veiled Privacy Protocol (`$VEILED`)
* **Brand Wordmark**: **`V E I L E D`** (tracked uppercase editorial serif, inspired by [noumen.xyz](https://www.noumen.xyz/))
* **Official Domain**: **`https://veiled.space/`**
* **Contact Email**: `contact@veiled.space`
* **X / Twitter**: `@veiledprivacy` (`https://x.com/veiledprivacy`)
* **Brand Logo Glyph**: **Chiseled Veiled Monogram (`V`)** with delicate sheer veil drapery contours and central glowing zero-knowledge focal star.
* **Target Network**: Robinhood Chain (EVM · Chain ID: `4663` · Native Asset: `ETH`)
* **Launchpad**: Pons Family Launchpad (`https://ponsfamily.com/launchpad`)
* **Block Explorer**: Blockscout (`https://robinhoodchain.blockscout.com`)
* **Core Value Proposition**: An EVM-native, zero-knowledge state shield allowing users on Robinhood Chain to shield native ETH and USDG into a Poseidon Merkle accumulator, break on-chain heuristics, and withdraw clean funds to unlinked recipient wallets via decentralized relayers.
* **Aesthetic & Style**: Atmospheric, cinematic, minimalist noir with obsidian dark background (`#030405`), glowing celestial indigo accents (`#A5B4FC`), living HTML5 particle canvas physics, and dynamic typography.
* **Typography System**:
  - **Brand Wordmark & Display**: **Instrument Serif** uppercase with wide tracking (`letter-spacing: 0.28em - 0.35em`, styled as `V E I L E D` like Noumen's `N O U M E N`).
  - **Headings & Editorial Statements**: **Instrument Serif** (the exact editorial typeface used on [noumen.xyz](https://www.noumen.xyz/)), with tight leading (`1.02`), `-0.02em` tracking, and delicate flowing italic cursive for emphasis words (`<em>shadow.</em>`).
  - **Body Text**: **Geist** (`ui-sans-serif`).
  - **Code & Metadata**: **Geist Mono** (`ui-monospace`).
* **Mascots & Cryptographic Iconography**:
  - **The Veiled Marble Sentinel ("The Veiled Sovereign")**: Classical draped marble bust in 1-bit stipple pointillism with interactive fluid physics in the Hero section, enlarged and right-aligned (`hcx = hw * 0.72`) to complement the left-aligned editorial headline typography.
  - **Justitia Velata with Balance Scales**: Neoclassical half-figure holding antique balance scales by the fulcrum in the Glass Ledger Scroll Accumulator, scaled up to 460px width, demonstrating state conservation ($\sum \text{In} = \sum \text{Out}$).
  - **The Council of Five Veiled Sentinels ("The Silent Custodians")**: 5 miniature classical Carrara marble busts (`assets/veiled_bust_node.png`) of the Veiled Sentinel resting on classical plinths in The Shuffling Veil Game, executing the shroud-lift transition sequence.
* **Tagline**: *"Silence on the ledger. Leave no shadow."*

---

## 2. Robinhood Chain Network Configurations

Use the following official configurations when developing, deploying, or testing:

### Robinhood Chain (Mainnet)
* **Chain ID**: `4663`
* **Currency Symbol**: `ETH`
* **Default RPC URL**: `https://rpc.mainnet.chain.robinhood.com/`
* **Block Explorer**: `robinhoodchain.blockscout.com` (https://robinhoodchain.blockscout.com)

### Robinhood Chain Testnet
* **Chain ID**: `46630`
* **Currency Symbol**: `ETH`
* **Default RPC URL**: `https://rpc.testnet.chain.robinhood.com/`
* **Block Explorer**: `explorer.testnet.chain.robinhood.com` (https://explorer.testnet.chain.robinhood.com)

---

## 3. Directory Structure & File Map

```
d:\project\Q4 Dev Arc\
├── .agents/                 # Preserved agent rules and configurations
├── index.html               # Main production landing page (self-contained HTML5, EVM-ready)
├── favicon.svg              # Brand vector icon with Chiseled Veiled Monogram 'V'
├── favicon.ico              # Standard icon fallback
├── PROJECT_CONTEXT.md       # Master project context (this file)
├── WALKTHROUGH.md           # Deep technical architecture & component breakdown
├── TWITTER_FLOW.md          # 10-tweet launch thread, teaser flow, daily CT roadmap
├── generate_site.py         # Standalone Python script to adjust brand/contract variables
└── assets/                  # Local runtime assets (no external CDN dependencies required)
    ├── hosts-Dhq3J-lZ.js     # Subdomain router & origin host resolver
    ├── hosts-DyUKjrHR.css    # Host utility styling
    ├── loader-LzncGZh9.css   # Preloader animations
    ├── site-nav-CgcRjVws.css # Navigation glassmorphic blur styles
    ├── site-nav-CTcSYDIB.js  # Sticky navigation, mobile menu & scrollspy observer
    ├── instrument-serif-normal.woff2 # Instrument Serif Regular 400 (Local)
    ├── instrument-serif-italic.woff2 # Instrument Serif Italic 400 (Local)
    ├── veiled_sentinel.jpg   # Master high-res 1-bit dithered Veiled Sentinel artwork
    ├── veiled_scales_cropped.jpg # Concept B: Justitia Velata holding balance scales
    └── veiled_bust_node.png  # Concept A: Veiled Sentinel marble bust for #game nodes
```

---

## 4. Running & Testing Locally

The project is served with Python's built-in HTTP server:

```powershell
python -m http.server 3000
```

* **Local Browser URL**: `http://localhost:3000/`
* **Default Document**: `index.html`

---

## 5. Key Interactive Components in `index.html`

1. **Preloader Animation (`#loader`)**: Plays once per browser tab session (`sessionStorage`). Shows the Chiseled Veiled Monogram `V` drawn in animated vector strokes with progress bar and reveals the page when ready.
2. **Hero Atmospheric Editorial Composition (`#heroCanvas`)**:
   * Samples ~5,400 dither points from `assets/veiled_sentinel.jpg` using an offscreen canvas.
   * Right-aligned on desktop (`hcx = hw * 0.72`) and enlarged up to 880px max, forming a balanced editorial composition alongside the left-aligned headline typography (`Silence on the ledger. Leave no shadow.`).
   * Illuminated by the ambient celestial indigo halo (`.halo`) positioned behind the sculpture (`left: 72%`).
   * Ultra-clean pre-launch layout: unlaunched contract address card removed in favor of pure negative space and clear pre-launch action pathways (`[Explore Protocol ↓]` and `[Follow Announcements ↗]`).
   * **Fluid Physics & Particle Engine**:
     - Spring pull: `p.vx += (tx - p.x) * 0.08`, `p.vy += (ty - p.y) * 0.08`.
     - Fluid mouse repulsion: $R = 105\text{px}$, force multiplier $= 6.5$.
     - Damping: $0.82$.
     - Ambient breathing float: $\sin(1.3 t + \phi) \cdot 1.8\text{px}$.
     - Ballistic sparks & shockwave ripple: Clicking anywhere within the hero section bursts luminous sparks toward the Veiled Sentinel, triggering an expanding shockwave ripple through the stipple matrix.
3. **Glass Ledger Scroll Accumulator (`#storyCanvas`)**:
   * Pinned viewport stage scrubbing through 4 protocol phases based on scroll depth ($p \in [0.0, 1.0]$).
   * **Justitia Velata with Interactive Balance Scales**: Neoclassical half-figure holding balance scales by the central fulcrum (`fx, fy`), scaled to a commanding `sW = 460px` with clear 230px+ clearance to Wallet A and Wallet B cards.
   * **Scale Tilt & Physics**:
     - *Phase 01*: Tilts down on left pan (`tilt = -0.052 rad`) under the heavy weight of 14.20 ETH on Wallet A.
     - *Phase 02*: Returns toward horizontal as funds stream into the left pan and climb to the fulcrum.
     - *Phase 03*: Gentle harmonic equilibrium balance (`sin(2.4t) · 0.012`) visually demonstrating $\sum \text{In} = \sum \text{Out}$ surrounded by 3D Merkle orbital rings and Poseidon hash nodes.
     - *Phase 04*: Tilts slightly down on right pan (`+0.036 rad`) as clean unlinked tokens pour out into fresh Wallet B (`0x4663…04AB`), with on-chain lineage severed below (`✕ NO LINK`).
4. **The Shuffling Veil Game (`#game`)**:
   * Interactive 5-node game simulating cryptographic mixing with **native 0.1 ETH coins (Ethereum diamond vector glyphs)**.
   * Nodes are rendered as **The Council of Five Veiled Sentinels** (`assets/veiled_bust_node.png`) resting upon classical carved plinths.
   * **Full Transition Animation Sequence**:
     - *Idle*: The 0.1 ETH coin hovers high above the center Sentinel (`translateY(-210px)`) under the spotlight cone.
     - *Drop*: Upon initiating shuffle, the coin slides smoothly down (`translateY(0)`), disappearing behind the custodian's veil into the plinth (`"Into the veil it goes…"`).
     - *Shuffle*: The spotlight dims into cryptographic blindness; the 5 identical Veiled Custodians glide and hop across the floor grid through 14 randomized swaps with real-time HUD swap tracking.
     - *Pick*: Hovering elevates any custodian slightly (`translateY(-8px) scale(1.02)`) with a glowing hover aura. The chosen custodian is enveloped in a radiant golden chiaroscuro rim glow (`.picked`).
     - *Reveal*: All 5 Veiled Custodians **lift up into the air (`translateY(-115px)`)**, ascending like ethereal apparitions as the spotlight floods the stage, unveiling the glowing `0.1 ETH` coins spinning on their plinths below ($5\text{ in }5$ anonymity set proof).
5. **Flashlight Wordmark (`#enter`)**:
   * Radial gradient mask follows the cursor via `--cx` and `--cy` CSS variables to illuminate the `V E I L E D` wordmark.
6. **Smooth Header Navigation**:
   * Header bounce animation disabled (`.nav.scrolled { animation: none !important; transform: none !important; }`), ensuring perfectly smooth, stationary glassmorphic navbar throughout scrolling.

---

## 6. How to Update Parameters via `generate_site.py`

To rebrand or customize parameters (e.g. changing the token name, ticker, EVM contract address, or Twitter handle):

```powershell
python generate_site.py "BrandName" "$TICKER"
```
