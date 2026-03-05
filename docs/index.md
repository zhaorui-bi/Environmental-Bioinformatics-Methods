# Environmental Bioinformatics Methods

```{admonition} Course Positioning
:class: note
This course is organized in a CS224n-style workflow: clear weekly roadmap, assignment-driven learning, and milestone-based final project.
```

::::{grid} 1 2 2 2
:::{grid-item-card} Syllabus
Understand goals, prerequisites, learning outcomes, and grading.
+++
[Open Syllabus](syllabus.md)
:::

:::{grid-item-card} Weekly Schedule
Lecture-by-lecture reading and practice plan.
+++
[Open Schedule](schedule.md)
:::

:::{grid-item-card} Assignments
Homework tracks, submission standards, and rubric.
+++
[Open Assignments](assignments.md)
:::

:::{grid-item-card} Final Project
Project milestones from proposal to final report.
+++
[Open Project Guide](project.md)
:::
::::

## Teaching Philosophy

- Learn from real environmental datasets rather than toy examples.
- Keep every analysis reproducible: environment, commands, data version, and outputs.
- Value engineering quality in addition to biological interpretation.

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
```

```{toctree}
:maxdepth: 2
:caption: Course Navigation

syllabus
schedule
assignments
project
policies
resources
faq
```
