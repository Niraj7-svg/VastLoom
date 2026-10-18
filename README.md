# Vastloom

Vastloom is an artist-directed procedural world-building suite for Blender and game developers, designed for stylised (Arcane / Fortiche aesthetic) and realistic environments.

> [!NOTE]
> 🚀 **Vibe Coded with Gemini 3.8 Flash**  
> This entire project, its architecture, procedural math, and Blender integration are being iteratively vibe coded and co-engineered with **Gemini 3.8 Flash** in real-time.

> [!IMPORTANT]
> Vastloom is in early active development for **Blender 5.2 LTS**. Data structures and user interfaces are evolving rapidly.

---

## 🌟 What is Vastloom?

Vastloom is an all-in-one procedural environment powerhouse that generates production-ready, optimized 3D worlds with a single click:

- **Procedural Cities & Streets:** Orthogonal Manhattan grids, angled diagonal avenues, and concentric curved/radial ring roads.
- **Dynamic Skyline Variations:** Multi-floor buildings with randomized heights, roof variations, and deterministic seeds.
- **High-Performance Linked Duplication:** Built using Blender's `Option + D` data-sharing model (`bpy.data.objects.new` referencing shared `bmesh` cubes), allowing thousands of buildings to render smoothly at 60+ FPS with minimal RAM usage.
- **Strictly Decoupled Architecture:** Pure Python math in `core/` (zero `bpy` imports), completely isolated from the Blender mesh-building `bridge/` layer.
- **Continuous Road Networks & Map Parsing (In Progress):** Generating smooth continuous street corridors and converting black-and-white 2D map sketches/Google Maps screenshots into 3D cities.
- **Terrain & Erosion (Upcoming):** Multi-octave heightmaps, hydraulic and thermal erosion simulations.
- **Game Engine Bridges (Upcoming):** One-click import into Unreal Engine and Unity with pre-configured LODs and collision setups.

---

## 🏗️ Project Architecture

```text
vastloom/
├── core/                  # Pure Python math, vector & geometry algorithms (ZERO bpy imports)
│   ├── roads.py           # Straight, angled, and radial street math
│   └── buildings.py       # Parcel subdivision & building placement logic
│
├── bridge/                # Blender 3D construction layer (uses bpy & bmesh)
│   ├── collections.py     # Shared mesh instancing (Option+D) & collection hierarchy
│   ├── roads.py           # 3D road slab instantiation
│   └── buildings.py       # Modular house builder (body, roof, doors)
│
├── operators/             # Blender event handlers and operator actions
│   └── city_ops.py        # City generation and scene management operators
│
├── ui/                    # Immediate-mode dynamic sidebar panel (N-Panel)
│   ├── main_panel.py      # Main sidebar layout & environment switcher
│   └── city_panel.py      # Urban layout controls, skyline variations & road settings
│
├── properties/            # Persistent scene state & PropertyGroups
│   └── properties.py      # Scene-level data definitions
│
├── blender_manifest.toml  # Blender extension metadata
└── __init__.py            # Extension registration entry point
```

---

## ⚙️ Requirements

- **Blender:** 5.2 LTS or newer compatible 5.x release
- **Python:** 3.13 / 3.14 for local IDE development
- **VS Code Extension:** Blender Development (for instant interactive hot-reloading)

---

## 🛠️ Development Setup

1. Clone the repository:
   ```bash
   git clone git@github.com:Niraj7-svg/VastLoom.git
   cd VastLoom
   ```

2. Create a virtual environment and install typing stubs for autocomplete:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -U fake-bpy-module-latest
   ```

3. Open in VS Code, run `Blender: Start`, and press **N** in the 3D Viewport to open the **Vastloom** panel.

---

## 📄 License

Distributed under the GNU General Public License v3.0 or later (`GPL-3.0-or-later`), matching the Blender extension ecosystem.

Distributed under the GNU General Public License v3.0 or later (`GPL-3.0-or-later`), matching the Blender extension ecosystem.

