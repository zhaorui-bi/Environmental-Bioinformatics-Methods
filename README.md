# 环境生物信息学方法 | Methodologies of Environmental Bioinformatics

面向研究生的环境生物信息学课程仓库与文档网站。  
A graduate-level course repository and documentation site for environmental bioinformatics.

## 课程基本信息 | Course Information

- 修读对象：硕士/博士研究生。  
  Target students: Master's and PhD students.
- 任课教师：余珂。  
  Instructor: Ke Yu.
- 总学时：48 学时（16 讲 x 3 学时）。  
  Contact hours: 48 hours (16 lectures x 3 hours).
- 课程网站（Read the Docs）：<https://environmental-bioinformatics-methods.readthedocs.io/>  
  Course website (Read the Docs): <https://environmental-bioinformatics-methods.readthedocs.io/>

## 课程入口 | Course Navigation

- 课程大纲：`docs/syllabus.md`  
  Syllabus: `docs/syllabus.md`
- 教学进度：`docs/schedule.md`  
  Schedule: `docs/schedule.md`
- 作业与案例：`docs/assignments.md`  
  Assignments and case studies: `docs/assignments.md`
- 课程项目：`docs/project.md`  
  Final project: `docs/project.md`
- 课程要求与规范：`docs/policies.md`  
  Policies: `docs/policies.md`

## 课程考核 | Assessment

- 平时作业与上机练习：25%。  
  Regular homework and lab practice: 25%.
- 研究案例 I/II/III：30%。  
  Case studies I/II/III: 30%.
- 课程项目设计（第 15 讲）：10%。  
  Project proposal/design (Lecture 15): 10%.
- 期末小组报告（第 16 讲）：25%。  
  Final team report and presentation (Lecture 16): 25%.
- 课堂参与与出勤：10%。  
  Class participation and attendance: 10%.

## 参考书 | References

1. Rodriguez-Ezpeleta, Hackenberg, and Aransay. *Bioinformatics of High Throughput Sequencing*. 978-1-4614-0781-2, 2012.
2. Hodgman, French, and Westhead. *Bioinformatics*.

## 仓库结构 | Repository Structure

```text
.
├── assignments/          # 作业与案例模板 / Assignment and case templates
├── docs/                 # Sphinx + MyST 文档源文件 / Sphinx + MyST docs source
├── lecture/              # 课程讲义 PDF / Lecture slides (PDF)
├── project/              # 课程项目模板 / Final project templates
├── LICENSE
├── README.md
└── TOOL.md               # 生信工具开发建议 / Bioinformatics tool-quality guidance
```

## 本地构建文档 | Build Docs Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
```

构建成功后打开 `docs/_build/html/index.html`。  
Open `docs/_build/html/index.html` after build succeeds.

## 部署到 Read the Docs | Deploy to Read the Docs

1. Push this repository to GitHub.
2. Import the repository at <https://app.readthedocs.org/>.
3. Read the Docs auto-detects `.readthedocs.yaml` and builds docs.

## Citation

```bibtex
@misc{PKU-EMBL_EnvBioinfoMethods,
  author       = {{PKU-EMBL}},
  title        = {Environmental Bioinformatics Methods},
  year         = {2026},
  publisher    = {GitHub},
  journal      = {GitHub repository},
  howpublished = {\url{https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods}},
  note         = {Accessed: 2026-03-05}
}
```
