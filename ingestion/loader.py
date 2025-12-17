from pathlib import Path
from typing import List, Dict
from pypdf import PdfReader
import re


def load_pdf(file_path: Path) -> List[Dict]:
    reader = PdfReader(str(file_path))
    documents = []

    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text:
            continue

        documents.append(
            {
                "content": text.strip(),
                "metadata": {
                    "source": file_path.name,
                    "page": i,
                },
            }
        )

    return documents


def load_markdown(file_path: Path) -> List[Dict]:
    text = file_path.read_text(encoding="utf-8")

    return [
        {
            "content": text.strip(),
            "metadata": {
                "source": file_path.name,
            },
        }
    ]


def load_documents(data_dir: Path) -> List[Dict]:
    documents = []

    for file_path in data_dir.iterdir():
        if file_path.suffix == ".pdf":
            documents.extend(load_pdf(file_path))
        elif file_path.suffix == ".md":
            documents.extend(load_markdown(file_path))

    return documents

def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()