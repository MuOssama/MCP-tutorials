"""
MCP Server — Mustapha Ossama's CV
Exposes tools to query skills, experience, projects, education,
certifications, and a resource to read/download the CV PDF.
"""

import base64
import json
import pathlib
from typing import Optional

try:
    from mcp.server.mcpserver import MCPServer as FastMCP
except (ImportError, ModuleNotFoundError):
    from mcp.server.fastmcp import FastMCP  # type: ignore

# path to CV PDF (same directory as this script)
CV_PDF_PATH = pathlib.Path(__file__).parent / "Mustapha_Ossama_3-Oct-26.pdf"

mcp = FastMCP(
    "mustapha-cv",
    instructions=(
        "This MCP server exposes Mustapha Ossama's CV data as queryable tools "
        "and a resource. Use the tools to look up skills, experience, projects, "
        "education, and certifications. Use the PDF resource to fetch the raw CV."
    ),
)

PROFILE = {
    "name": "Mustapha Ossama Abdelhalim",
    "title": "AI Software Engineer",
    "specializations": ["LLM Applications","Agentic AI","Document AI","Computer Vision"],
    "email": "mustaphaossamaplus@gmail.com",
    "phone": "01503808705",
    "location": "Sheikh Zayed, Giza, Egypt",
}

TECHNICAL_SKILLS = {
    "Web Scraping": ["Selenium","BeautifulSoup4 (BS4)","JavaScript DevTools","Requests","web data extraction"],
    "Agentic AI / Automation": ["LangChain","LangSmith","LangGraph","MCP","n8n","workflow orchestration","intelligent automation"],
    "AI / ML / DL": ["LLMs","VLMs","Classical ML","Deep Learning","fine-tuning","NLP","TensorFlow","Keras","Scikit-learn","YOLOv8"],
    "Computer Vision / ADAS": ["Object detection","image classification","image processing","LKAS","ACC","AEB","LDWS","drowsiness detection","LiDAR","Raspberry Pi 4","Embedded Linux"],
    "RAG": ["Splitting","semantic chunking","embeddings","vector search","hybrid retrieval","reranking","production-scale RAG"],
    "LLM Engineering": ["Local LLMs","LLM APIs","model hosting","instruction fine-tuning","performance-based optimization (PBO)","RLHF","DPO"],
    "Cloud / Deployment": ["AWS S3","EC2","Lambda","Docker","Kubernetes","API integration","production deployment"],
    "Coding / Scripting": ["Python","C","C++","Java","PHP","Linux","Bash","HTML","JavaScript","OOP","GUI development"],
    "Databases / Version Control": ["PostgreSQL","SQLite","Redis","Git","GitHub","data processing","validation","cleaning"],
}

EXPERIENCE = [
    {
        "role": "Software Automation Engineer",
        "company": "Zillion Parts",
        "location": "Cairo",
        "period": "Nov 2024 - Present",
        "highlights": [
            "AI-driven automation and data-processing workflows using Python, LLM APIs, LangGraph.",
            "AI web-scraping agent (LangGraph + DuckDuckGo) targeting 1M+ machine components.",
            "Machine-name identification, category identification, and classification apps.",
            "LLM-powered content creation and validation with automated quality checks.",
            "ML classifier for shipping-price determination.",
            "Deep-learning object removal and custom image classification.",
            "Desktop automation for repetitive data-entry workflows.",
        ],
    },
    {
        "role": "Mechatronics Engineer",
        "company": "YME 3D Engineering",
        "location": "Giza",
        "period": "Aug 2022 - Sep 2024",
        "highlights": [
            "Led end-to-end development of 30+ robotics and embedded systems.",
            "Bare-metal C/C++ firmware for Arduino and ESP32.",
            "Python applications on Raspberry Pi / Embedded Linux.",
            "Sensor/actuator integration, communication protocols, and control logic.",
        ],
    },
    {
        "role": "Embedded Systems Instructor",
        "company": "ITI",
        "location": "Smart Village, Giza",
        "period": "Jul 2023 - Aug 2024",
        "highlights": [
            "Delivered practical embedded-systems instruction.",
            "Guided learners through firmware and system-integration concepts.",
        ],
    },
    {
        "role": "Embedded Systems Intern",
        "company": "Siemens",
        "location": "Egypt",
        "period": "Jul 2022 - Oct 2022",
        "highlights": ["Exposure to OSEK, DevOps fundamentals, and functional safety."],
    },
]

PROJECTS = [
    {"name": "Bbox Inpainter", "stack": ["Python","Deep Learning","Computer Vision"], "description": "Deep-learning image inpainting system for removing selected objects from images.", "github": True},
    {"name": "Zillion Parts AI Web Scraping & Datasheet Agent", "stack": ["Python","LangGraph","LLM APIs","Web Scraping"], "description": "Agentic pipeline for supplier search, datasheet discovery, PDF retrieval, document verification, adaptive query rewriting, and usage/cost tracking.", "github": False},
    {"name": "Zillion Parts Machine Name & Category Classification", "stack": ["Python","LLMs","NLP","Classification"], "description": "AI apps for machine-name identification, category identification, and classification across industrial product data.", "github": False},
    {"name": "Zillion Parts LLM Content Creation & Validation", "stack": ["Python","LLM APIs","NLP"], "description": "LLM-powered apps for structured content creation, content validation, and automated quality checks.", "github": False},
    {"name": "Zillion Parts Shipping Price ML Classifier", "stack": ["Python","Scikit-learn","Machine Learning"], "description": "ML classifier for shipping prices within product and order automation workflows.", "github": False},
    {"name": "Zillion Parts Custom Image Classifier", "stack": ["Python","Deep Learning","Computer Vision"], "description": "Custom image classification for certificates, datasheet-like images, and numeric tables.", "github": False},
    {"name": "Background Remover using DINO + SAM", "stack": ["Python","Computer Vision","DINO","SAM"], "description": "Pipeline combining Grounding DINO-style detection with SAM segmentation for background/object isolation.", "github": True},
    {"name": "YOLOv8 Custom Drowsiness Detection", "stack": ["Python","YOLOv8","Deep Learning"], "description": "YOLOv8 model fine-tuned on a custom dataset for drowsiness detection.", "github": True},
    {"name": "ADAS Graduation Project", "stack": ["Python","C/C++","Deep Learning","Computer Vision","Embedded Linux","Raspberry Pi 4","LiDAR"], "description": "Integrated ACC, AEB, LKAS, LDWS, and drowsiness detection on a real vehicle platform.", "github": False},
    {"name": "MuBank", "stack": ["Python","Raspberry Pi","Embedded Linux"], "description": "Raspberry Pi-based ATM application demonstrating Embedded Linux and software/system integration.", "github": True},
    {"name": "RTOS Smart Home", "stack": ["C","AVR","RTOS"], "description": "AVR-based smart-home project built around real-time embedded software.", "github": True},
    {"name": "Medical Assistance Robot", "stack": ["Robotics","Embedded Systems"], "description": "Large-scale robotics project integrating mechanics, electronics, sensing, and control.", "github": True},
]

EDUCATION = [
    {"degree": "MSc, Electronics and Communication", "institution": "Cairo University", "period": "Oct 2024 - Present", "gpa": None},
    {"degree": "B.E., Mechatronics Engineering", "institution": "October 6 University", "period": "Jul 2019 - Jul 2024", "gpa": "3.48"},
    {"degree": "Diploma, Embedded Linux", "institution": "IMT", "period": "Oct 2022 - Mar 2023", "gpa": None},
    {"degree": "Diploma, Embedded Systems AVR", "institution": "IMT, Giza", "period": "Jul 2021 - Mar 2022", "gpa": None},
]

CERTIFICATIONS = [
    "Minesweeper ARC - Alamein Robotics Championship: Qualified to Finals (2023)",
    "16th Undergraduate Research Forum (UGRF), Nile University (2023)",
    "Introduction to Electronics, Georgia Institute of Technology (2022)",
    "Python Classes and Inheritance, University of Michigan (2022)",
]


@mcp.tool()
def get_profile() -> str:
    """Return Mustapha Ossama professional profile: name, title, specializations, and contact details."""
    lines = [
        f"Name : {PROFILE['name']}",
        f"Title: {PROFILE['title']}",
        f"Specializations: {', '.join(PROFILE['specializations'])}",
        f"Email: {PROFILE['email']}",
        f"Phone: {PROFILE['phone']}",
        f"Location: {PROFILE['location']}",
    ]
    return "\n".join(lines)


@mcp.tool()
def list_skill_categories() -> str:
    """List all high-level technical skill categories on the CV."""
    return "Skill categories:\n" + "\n".join(f"  - {c}" for c in TECHNICAL_SKILLS)


@mcp.tool()
def get_skills(category: Optional[str] = None) -> str:
    """
    Return technical skills from the CV.

    Args:
        category: Optional skill category name e.g. 'AI / ML / DL'.
                  If omitted, returns ALL skills grouped by category.
    """
    if category:
        key = next((k for k in TECHNICAL_SKILLS if k.lower() == category.lower()), None)
        if key is None:
            return f"Category '{category}' not found. Available: {', '.join(TECHNICAL_SKILLS)}"
        return f"{key}:\n" + "\n".join(f"  - {s}" for s in TECHNICAL_SKILLS[key])
    parts = []
    for cat, skills in TECHNICAL_SKILLS.items():
        parts.append(f"{cat}:\n" + "\n".join(f"  - {s}" for s in skills))
    return "\n\n".join(parts)


@mcp.tool()
def search_skills(keyword: str) -> str:
    """
    Search for a keyword across all skill categories.

    Args:
        keyword: A technology or concept to search for e.g. 'Docker', 'RAG', 'YOLOv8'.
    """
    results = []
    kw = keyword.lower()
    for cat, skills in TECHNICAL_SKILLS.items():
        matched = [s for s in skills if kw in s.lower()]
        if matched:
            results.append(f"{cat}: {', '.join(matched)}")
    if not results:
        return f"No skills matching '{keyword}' found."
    return f"Skills matching '{keyword}':\n" + "\n".join(f"  - {r}" for r in results)


@mcp.tool()
def get_experience(company: Optional[str] = None) -> str:
    """
    Return professional work experience.

    Args:
        company: Optional company name to filter by e.g. 'Zillion Parts'.
                 If omitted, returns the full experience history.
    """
    jobs = EXPERIENCE
    if company:
        jobs = [j for j in EXPERIENCE if company.lower() in j["company"].lower()]
        if not jobs:
            return f"No experience at '{company}'. Known companies: {', '.join(j['company'] for j in EXPERIENCE)}"
    parts = []
    for j in jobs:
        header = f"{j['role']} @ {j['company']}, {j['location']} ({j['period']})"
        bullets = "\n".join(f"  - {h}" for h in j["highlights"])
        parts.append(f"{header}\n{bullets}")
    return "\n\n".join(parts)


@mcp.tool()
def get_projects(stack_filter: Optional[str] = None) -> str:
    """
    Return selected AI and software/embedded projects from the CV.

    Args:
        stack_filter: Optional technology to filter by e.g. 'LangGraph', 'YOLOv8', 'C++'.
                      If omitted, all projects are returned.
    """
    projects = PROJECTS
    if stack_filter:
        sf = stack_filter.lower()
        projects = [p for p in PROJECTS if any(sf in t.lower() for t in p["stack"])]
        if not projects:
            return f"No projects found using '{stack_filter}'."
    parts = []
    for p in projects:
        tag = " [GitHub]" if p["github"] else ""
        parts.append(
            f"{p['name']}{tag}\n"
            f"  Stack: {', '.join(p['stack'])}\n"
            f"  {p['description']}"
        )
    return "\n\n".join(parts)


@mcp.tool()
def get_education() -> str:
    """Return educational background and qualifications."""
    parts = []
    for e in EDUCATION:
        gpa = f" | GPA: {e['gpa']}" if e["gpa"] else ""
        parts.append(f"{e['degree']} - {e['institution']} ({e['period']}){gpa}")
    return "Education:\n" + "\n".join(f"  - {p}" for p in parts)


@mcp.tool()
def get_certifications() -> str:
    """Return certifications and notable achievements."""
    return "Certifications & Achievements:\n" + "\n".join(f"  - {c}" for c in CERTIFICATIONS)


@mcp.tool()
def full_cv_summary() -> str:
    """Return a complete structured summary of the entire CV in one call."""
    return "\n".join([
        get_profile(),
        "\n--- SKILLS ---",
        get_skills(),
        "\n--- EXPERIENCE ---",
        get_experience(),
        "\n--- PROJECTS ---",
        get_projects(),
        "\n--- EDUCATION ---",
        get_education(),
        "\n--- CERTIFICATIONS ---",
        get_certifications(),
    ])


@mcp.resource("cv://pdf/base64")
def cv_pdf_base64() -> str:
    """
    Return the raw CV PDF encoded as a Base64 string.
    Decode with base64.b64decode(response) to get the binary PDF bytes.
    """
    if not CV_PDF_PATH.exists():
        return f"ERROR: PDF not found at {CV_PDF_PATH}"
    return base64.b64encode(CV_PDF_PATH.read_bytes()).decode("ascii")


@mcp.resource("cv://pdf/info")
def cv_pdf_info() -> str:
    """Return metadata about the CV PDF file: filename, path, size."""
    exists = CV_PDF_PATH.exists()
    size = CV_PDF_PATH.stat().st_size if exists else 0
    return json.dumps({
        "filename": CV_PDF_PATH.name,
        "path": str(CV_PDF_PATH),
        "exists": exists,
        "size_bytes": size,
        "size_kb": round(size / 1024, 1),
    }, indent=2)


@mcp.resource("cv://skills/{category}")
def skills_by_category(category: str) -> str:
    """Templated resource: returns skills for a specific category. Example URI: cv://skills/RAG"""
    return get_skills(category)


if __name__ == "__main__":
    mcp.run(transport="stdio")
