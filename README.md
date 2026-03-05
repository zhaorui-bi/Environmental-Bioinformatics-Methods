# PKU EMBL | Environmental Bioinformatics Methods

A CS224n-style course repository for environmental bioinformatics: clear schedule, structured assignments, milestone-based project workflow, and a standalone course website on Read the Docs.

## Course Hub

- Course docs (Read the Docs): <https://environmental-bioinformatics-methods.readthedocs.io/>
- Course syllabus: [docs/syllabus.md](docs/syllabus.md)
- Weekly schedule: [docs/schedule.md](docs/schedule.md)
- Assignments: [assignments/README.md](assignments/README.md)
- Final project: [project/README.md](project/README.md)

## Repository Structure

```text
.
├── assignments/          # Homework specs, grading rubric, submission templates
├── docs/                 # Sphinx + MyST source for Read the Docs site
├── lecture/              # Lecture slides (PDF)
├── project/              # Final project track and templates
├── LICENSE
├── README.md
└── TOOL.md               # Suggested standards for bioinformatics tools
```

## Lectures

1. Lecture 1: [生物学基础](lecture/第一讲_生物学基础.pdf)
2. Lecture 2: [生物信息学资源](lecture/第二讲_生物信息学资源.pdf)
3. Lecture 3: [基础BLAST分析实例](lecture/第三讲_基础BLAST分析实例.pdf)
4. Lecture 4: [宏基因组分析概况及序列组装](lecture/第四讲_宏基因组分析概况及序列组装.pdf)
5. Lecture 5: [宏基因组分析设计及组装(1)](lecture/第五-六讲_宏基因组分析设计及组装.pdf)
6. Lecture 6: [宏基因组分析设计及组装(2)](lecture/第五-六讲_宏基因组分析设计及组装.pdf)
7. Lecture 7: [宏基因组分箱分析及实操](lecture/第七讲_宏基因组分箱分析及实操.pdf)
8. Lecture 8: [封箱、基因组质量检测及进化树的构建](lecture/第八讲_封箱、基因组质量检测及进化树的构建.pdf)
9. Lecture 9: [宏基因组丰度计算、功能注释及转录组分析基础](lecture/第九讲_宏基因组丰度计算、功能注释及转录组分析基础.pdf)
10. Lecture 10: [生态学理论及初步扩增子分析](lecture/第十讲_生态学理论及初步扩增子分析.pdf)

## Build Docs Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` in browser after build succeeds.

## Deploy to Read the Docs

1. Push this repository to GitHub.
2. Import the repository at <https://app.readthedocs.org/>.
3. Read the Docs will auto-detect `.readthedocs.yaml` and build the docs.
4. Optional: set custom domain in RTD project settings.

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
