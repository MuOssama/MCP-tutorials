# gui.py -- Tkinter GUI for the ATS CV Reviewer
# Separated from agent logic for readability.
# Call build_gui(start_review_fn) to launch the window.

import tkinter as tk
from tkinter import filedialog, scrolledtext

# Color palette & fonts
BG       = "#1e1e2e"
CARD     = "#2a2a3d"
ACCENT   = "#7c6af7"
FG       = "#cdd6f4"
FG_DIM   = "#6c7086"
FONT     = ("Segoe UI", 10)
FONT_B   = ("Segoe UI", 10, "bold")
FONT_TTL = ("Segoe UI", 16, "bold")


def build_gui(start_review_fn):
    """
    Build and run the Tkinter GUI.

    Args:
        start_review_fn: callable(cv_path, job_desc, output_widget, btn, status_var)
                         called when the user clicks "Review CV".
    """
    root = tk.Tk()
    root.title("ATS CV Reviewer")
    root.geometry("780x640")
    root.resizable(True, True)
    root.configure(bg=BG)

    # Title
    tk.Label(root, text="ATS CV Reviewer", font=FONT_TTL,
             bg=BG, fg=ACCENT).pack(pady=(18, 2))
    tk.Label(root, text="Powered by Mistral:7b  |  LangGraph  |  MCP",
             font=("Segoe UI", 9), bg=BG, fg=FG_DIM).pack(pady=(0, 14))

    # CV path row
    frame_top = tk.Frame(root, bg=BG)
    frame_top.pack(fill="x", padx=24)

    tk.Label(frame_top, text="CV PDF", font=FONT_B, bg=BG, fg=FG).grid(
        row=0, column=0, sticky="w", pady=4)

    cv_var = tk.StringVar()
    tk.Entry(frame_top, textvariable=cv_var, font=FONT,
             bg=CARD, fg=FG, insertbackground=FG,
             relief="flat", bd=6, width=55).grid(
        row=1, column=0, sticky="ew", ipady=6)

    def browse():
        path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if path:
            cv_var.set(path)

    tk.Button(frame_top, text="Browse...", font=FONT, bg=ACCENT, fg="white",
              activebackground="#6455d6", relief="flat", bd=0, padx=12,
              command=browse).grid(row=1, column=1, padx=(8, 0), ipady=6)
    frame_top.columnconfigure(0, weight=1)

    # Job description
    tk.Label(root, text="Job Description", font=FONT_B, bg=BG, fg=FG).pack(
        anchor="w", padx=24, pady=(14, 4))
    jd_box = tk.Text(root, height=5, font=FONT, bg=CARD, fg=FG,
                     insertbackground=FG, relief="flat", bd=6,
                     wrap="word", padx=8, pady=8)
    jd_box.pack(fill="x", padx=24)
    jd_box.insert("1.0",
        "We are looking for a Python developer with FastAPI, SQL, Docker, REST APIs and Git.")

    # Review button
    status_var = tk.StringVar(value="Ready")
    btn = tk.Button(root, text="Review CV", font=FONT_B,
                    bg=ACCENT, fg="white", activebackground="#6455d6",
                    relief="flat", bd=0, padx=20, pady=10)
    btn.pack(pady=14)

    # Output box
    tk.Label(root, text="Report", font=FONT_B, bg=BG, fg=FG).pack(
        anchor="w", padx=24)
    output_box = scrolledtext.ScrolledText(
        root, font=("Consolas", 9), bg=CARD, fg=FG,
        insertbackground=FG, relief="flat", bd=6,
        wrap="word", padx=8, pady=8, state="disabled")
    output_box.pack(fill="both", expand=True, padx=24, pady=(4, 6))

    # Wire up the button now that output_box exists
    btn.config(command=lambda: start_review_fn(
        cv_var.get().strip(),
        jd_box.get("1.0", tk.END).strip(),
        output_box, btn, status_var,
    ))

    # Status bar
    tk.Label(root, textvariable=status_var, font=("Segoe UI", 9),
             bg=BG, fg=FG_DIM, anchor="w").pack(fill="x", padx=24, pady=(0, 10))

    root.mainloop()