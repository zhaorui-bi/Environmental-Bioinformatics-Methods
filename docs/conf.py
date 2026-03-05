from datetime import datetime

project = "Environmental Bioinformatics Methods"
author = "PKU EMBL"
release = "2026"
copyright = f"{datetime.now().year}, {author}"

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = {
    ".md": "markdown",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "attrs_block",
    "attrs_inline",
]

html_theme = "sphinx_book_theme"
html_title = "Environmental Bioinformatics Methods"
html_static_path = ["_static"]
html_css_files = ["course.css"]

html_theme_options = {
    "repository_url": "https://github.com/PKU-EMBL/Environmental-Bioinformatics-Methods",
    "use_repository_button": True,
    "use_issues_button": True,
    "show_toc_level": 2,
    "home_page_in_toc": True,
    "path_to_docs": "docs",
}
