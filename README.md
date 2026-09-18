# Vastloom

Vastloom is an artist-directed procedural world-building extension for Blender.
Its long-term goal is to help artists construct and prepare large environments
while keeping creative decisions under their control.

> [!IMPORTANT]
> Vastloom is in very early development. It is not ready for production use,
> and its data structures and user interface may change frequently.

## Project goals

Vastloom is intended to grow into a modular toolkit for:

- Modular architecture and city construction
- Artist-directed terrain and vegetation
- Chunk-based world organization
- Camera-aware level-of-detail selection
- Procedural and render-to-texture distant horizons
- Offline animation preparation
- Versioned `.vloom` project and recovery data

The project follows a few core principles:

- World data is kept separate from generated Blender objects.
- Procedural results should be repeatable through deterministic seeds.
- Artists should be able to override automatic decisions.
- Systems should remain modular and understandable.
- Blender's native Python API, data blocks, Geometry Nodes, materials, and
  render systems are preferred.
- The procedural generation system does not require AI or machine learning.

## Current milestone

Stage 1 establishes the extension foundation:

- [x] Blender extension manifest
- [ ] Project settings
- [ ] Blender class registration
- [ ] Create Project operator
- [ ] Vastloom sidebar panel
- [ ] Installable extension package
- [ ] Blender installation and persistence tests

The first project settings are the project name, deterministic seed, and
initialization status. Terrain, buildings, vegetation, and horizon generation
are intentionally outside this milestone.

## Requirements

- Blender 5.2 LTS or newer compatible 5.x release
- Python 3.13 for the local development environment
- Git
- A Python editor such as Visual Studio Code

Blender includes its own Python runtime. The local virtual environment is used
for editor assistance and tests; it does not replace Blender's Python runtime.

## Development setup

Create and activate a Python 3.13 virtual environment:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
```

Install the Blender 5.2 API stubs for editor completion:

```bash
python -m pip install --upgrade pip
python -m pip install fake-bpy-module-5.2
```

The fake `bpy` package provides type information and autocomplete only. Actual
Blender operations must run inside Blender.

## Project structure

```text
vastloom/
├── blender_manifest.toml  # Blender extension metadata
├── __init__.py            # Extension registration entry point
├── properties.py          # Project settings stored by Blender
├── operators.py           # User-triggered actions
└── ui.py                  # Blender sidebar interface
```

The structure will expand gradually as each system is implemented and tested.

## Contributing

Vastloom is currently being built as a learning project. Issues and focused
contributions are welcome, but please discuss substantial architectural changes
before implementing them. Keep changes small, documented, and limited to one
concern whenever practical.

When reporting a Blender error, include:

- Blender version and operating system
- Steps required to reproduce the problem
- Expected and actual behavior
- The complete Python traceback

## Roadmap

Major planned stages include project persistence, asset registration, modular
building generation, city maps, terrain, vegetation, chunks, LODs, hybrid
horizons, preview rendering, animation preparation, caching, and recovery.

The roadmap may change as prototypes reveal better technical dependencies.

## License

Vastloom is intended to be distributed under the GNU General Public License
v3.0 or later (`GPL-3.0-or-later`), matching the license declared in the Blender
extension manifest. A complete `LICENSE` file should be included before the
first public release.
