<div align="center">

# 🌌 Vastloom
### *An Artist-Directed Procedural World-Building Engine for Blender*

[![Blender](https://img.shields.io/badge/Blender-5.2%20LTS-orange?logo=blender&logoColor=white)](https://www.blender.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Built with AI](https://img.shields.io/badge/Co--Engineered%20with-Gemini%203.8%20Flash-8E75B2?logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![Vibe Coded](https://img.shields.io/badge/Built%20by-An%20Artist-FF6B6B)](#-from-an-artists-brush-to-code)

<p align="center">
  <b>Designed for animators and game developers who want to paint living, cinematic worlds.</b><br>
  <i>Tailored for both painterly stylised aesthetics (Arcane / Fortiche style) and grounded realism.</i>
</p>

---

</div>

## 🎨 From an Artist's Brush to Code

> *"I am an artist, not a programmer. I have stories to tell and worlds to build, but manual world-building can take months of repetitive labor. That's why I teamed up with AI — **Gemini 3.8 Flash** — to turn creative vision directly into code.*
> 
> *Vastloom is proof of what happens when artistic direction meets modern AI co-engineering: a tool built by an artist, designed with empathy for creators, crafted to empower everyone to build massive, breathtaking 3D environments without getting bogged down in the technical grind."*

---

## ✨ Features at a Glance

<table>
  <tr>
    <td width="50%">
      <h3>🏙️ Procedural Urban Layouts</h3>
      <ul>
        <li><b>Orthogonal Manhattan Grids:</b> Clean, dense city blocks.</li>
        <li><b>Angled Diagonal Streets:</b> Tilted avenues at custom degree angles.</li>
        <li><b>Radial & Concentric Curves:</b> Circular European / fantasy ring roads with radiating avenues.</li>
      </ul>
    </td>
    <td width="50%">
      <h3>🏢 Dynamic Skyline Variations</h3>
      <ul>
        <li><b>Multi-Story Buildings:</b> Realistic floor distribution.</li>
        <li><b>Deterministic Random Seeds:</b> Re-roll the city skyline with a single click.</li>
        <li><b>Front-Facing Architecture:</b> Doors and entrances automatically align tangent to the adjacent street.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h3>⚡ High-Performance Linked Instancing</h3>
      <ul>
        <li><b>Blender <code>Option + D</code> Architecture:</b> All buildings and roads reference shared mesh data in memory.</li>
        <li><b>Zero Viewport Lag:</b> Thousands of buildings render at smooth 60+ FPS with minimal RAM usage.</li>
      </ul>
    </td>
    <td width="50%">
      <h3>📁 Clean Artist-Friendly Hierarchy</h3>
      <ul>
        <li><b>Structured Outliner:</b> Generates dedicated sub-collections (<code>House_1</code>, <code>House_2</code>, etc.) grouping bodies, roofs, and doors neatly.</li>
        <li><b>One-Click Cleanup:</b> Rebuilding automatically clears previous iterations cleanly.</li>
      </ul>
    </td>
  </tr>
</table>

---

## 🗺️ Vision & Roadmap

- [x] **Phase 0:** Modular multi-package architecture (`core`, `bridge`, `operators`, `ui`, `properties`).
- [x] **Phase 1 (Streets & Blocks):** Grid, angled, and curved concentric city generation with multi-floor skyline variations.
- [x] **Performance Engine:** `Option + D` shared mesh instancing.
- [ ] **Continuous Smooth Roads:** Polygon road meshes with chamfered junctions and curb fillets.
- [ ] **2D Map Image Parser:** Draw a top-down street map in Photoshop / Krita / Affinity, or take a screenshot from Google Maps, and watch Vastloom turn it into a 3D city automatically!
- [ ] **Terrain & Natural Mountains:** Multi-octave procedural heightmaps with hydraulic water and wind erosion simulations.
- [ ] **Stylized Shader Pipeline:** Hand-painted painterly textures, sharp rim edges, and stylized NPR shading.
- [ ] **One-Click Game Engine Bridge:** Direct export to Unreal Engine and Unity with pre-configured LODs and collision hulls.

---

## 🏛️ Architecture: Pure Logic Meets 3D

Vastloom is built with a strictly decoupled multi-package design:

```text
vastloom/
├── core/                  # Pure math & geometry algorithms (ZERO Blender dependencies)
│   ├── roads.py           # Straight, angled, and radial curved street math
│   └── buildings.py       # Parcel subdivision & lot placement logic
│
├── bridge/                # The 3D craftsman (converts math into Blender meshes)
│   ├── collections.py     # Option+D linked instancing & clean hierarchy
│   ├── roads.py           # 3D road surface generation
│   └── buildings.py       # Modular building construction
│
├── ui/                    # Immediate-mode N-panel sidebar interface
│   ├── main_panel.py      # Main control deck & environment switcher
│   └── city_panel.py      # Urban sliders, skyline seeds & street controls
│
├── operators/             # Blender event triggers & coordinator
│   └── city_ops.py        # City generation execution logic
│
├── properties/            # Persistent scene data notebook
│   └── properties.py      # Scene-level parameters & settings
│
├── blender_manifest.toml  # Blender 5.x extension manifest
└── __init__.py            # Main entry point and class registration
```

---

## 🚀 Getting Started

### Requirements
- **Blender:** 5.2 LTS or newer
- **OS:** macOS (Apple Silicon optimized), Windows, Linux

### Installation
1. Download or clone this repository:
   ```bash
   git clone git@github.com:Niraj7-svg/VastLoom.git
   ```
2. Open Blender 5.2 LTS.
3. In the 3D Viewport, press **`N`** on your keyboard to reveal the right sidebar.
4. Click on the **Vastloom** tab.
5. Choose your layout style, adjust your blocks and skyline sliders, and hit **Generate City**!

---

## 💖 Community & Contributing

Vastloom is being actively crafted in public. If you are an artist with ideas for stylized procedural shapes, or a developer wanting to contribute to the core math:
- Feel free to open an **Issue** or submit a **Pull Request**.
- Star ⭐ the repository if you want to follow the journey!

---

<div align="center">
  <sub>Crafted with passion by an artist • Powered by Gemini 3.8 Flash • Licensed under GPL-3.0</sub>
</div>
