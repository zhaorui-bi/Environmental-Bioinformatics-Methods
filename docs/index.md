# 环境生物信息学方法

Methodologies of Environmental Bioinformatics

```{admonition} Course Positioning
:class: note
本课程采用结构化课程组织方式：明确教学进度、分阶段作业与案例训练、项目化结课。
```

::::{grid} 1 2 2 2
:::{grid-item-card} 课程大纲
课程定位、修读对象、参考书和考核方式。
+++
[查看 Syllabus](syllabus.md)
:::

:::{grid-item-card} 教学进度
16 讲完整教学安排与内容要点。
+++
[查看 Schedule](schedule.md)
:::

:::{grid-item-card} 作业与案例
平时作业、案例 I/II/III 与评分标准。
+++
[查看 Assignments](assignments.md)
:::

:::{grid-item-card} 课程项目
第 15-16 讲项目设计与小组汇报要求。
+++
[查看 Project](project.md)
:::
::::

## 快速信息

- 修读对象：硕士/博士研究生
- 任课教师：余珂
- 学时：48 学时（16 讲 x 3 学时）
- 课程形式：讲授 + 上机 + 案例 + 项目

## 文档本地构建

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
