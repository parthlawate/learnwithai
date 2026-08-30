#!/usr/bin/env python3
"""
Balbharati Marathi Textbook Unicode Extractor & Formatter
Extracts legacy-font / non-Unicode Marathi PDF textbooks into high-fidelity Unicode Markdown and HTML.
"""

import os, sys, subprocess, argparse

def render_pages(pdf_path, output_dir, dpi=150):
    os.makedirs(output_dir, exist_ok=True)
    prefix = os.path.join(output_dir, "page")
    cmd = ["pdftoppm", "-png", "-r", str(dpi), pdf_path, prefix]
    print(f"[+] Rendering PDF pages using pdftoppm (DPI: {dpi})...")
    subprocess.run(cmd, check=True)
    png_files = sorted([f for f in os.listdir(output_dir) if f.endswith(".png")])
    print(f"[✓] Rendered {len(png_files)} pages to {output_dir}")
    return png_files

def main():
    parser = argparse.ArgumentParser(description="Extract Marathi PDF textbooks into structured Unicode documents.")
    parser.add_argument("pdf", help="Path to textbook PDF file")
    parser.add_argument("--outdir", default="./output", help="Output directory")
    parser.add_argument("--dpi", type=int, default=150, help="DPI for page rendering")
    args = parser.parse_args()

    if not os.path.exists(args.pdf):
        print(f"Error: {args.pdf} not found.")
        sys.exit(1)

    os.makedirs(args.outdir, exist_ok=True)
    pages_dir = os.path.join(args.outdir, "pages")
    render_pages(args.pdf, pages_dir, args.dpi)
    print("[+] Pages ready for vision OCR transcription.")

if __name__ == "__main__":
    main()
