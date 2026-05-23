from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
text="""class Student:
# 📘 Project Name: Smart Student Tracker

A simple Python-based project to manage and track student data,

---

## 🔍 Features

- Add new students with relevant info
- View student details
- Check if a student is passing
- Easily extendable class-based design

---

## ❌ Tech Stack

- Python 3.10+
- No external dependencies"""

spilitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=200,
    chunk_overlap=0)

chunks = spilitter.split_text(text)
print(len(chunks))
print(chunks[2])


 