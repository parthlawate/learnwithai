# 🎓 learnwithai

> **Simple Tools, LLM-Ready Educational Content & HTML5 AI Games to empower parents and teachers helping kids learn, excel at homework, and ace exam prep.**

---

## 🌟 Vision & Purpose

Parents and teachers often face hurdles when helping young children learn in regional and vernacular mediums:
1. **Unusable Legacy PDFs**: Textbooks are often encoded with non-Unicode 8-bit fonts (e.g., Shree-Lipi, WinAnsi), rendering them unreadable by modern AI assistants, search engines, and screen readers.
2. **Lack of Assistive AI Tools for Regional Languages**: LLMs have immense potential to be patient, interactive 24/7 tutors, but they require clean, structured, high-fidelity source material.
3. **Engaging Gamified Learning**: Learning shouldn't just be rote memorization. Combining clean curriculum data with interactive HTML5 AI games creates an immersive, joyful study experience.

`learnwithai` bridges this gap by providing:
- **Clean, structured, full-Unicode curriculum data** across grades and mediums.
- **Ready-to-use LLM prompts, RAG datasets, and study agent workflows**.
- **Interactive HTML5 AI games & assistive tools** designed for parents, teachers, and students.

---

## 📂 Repository Catalog & Assets

```
learnwithai/
├── README.md
└── medium/
    └── marathi/
        ├── extract_marathi_textbook.py                 # Automated Balbharati PDF Unicode extraction script
        └── grade3/
            └── marathi/
                ├── Grade_3_Marathi_Balbharati.html     # Standalone interactive HTML reader app
                ├── Grade_3_Marathi_Balbharati_Complete.md # Complete 100-page Unicode textbook (22 lessons)
                ├── part_1.md                           # भाग १: धडे १ ते ६ (पृष्ठ १ ते २३)
                ├── part_2.md                           # भाग २: धडे ७ ते ११ (पृष्ठ २४ ते ४२)
                ├── part_3.md                           # भाग ३: धडे १२ ते १७ (पृष्ठ ४३ ते ६७)
                ├── part_4.md                           # भाग ४: धडे १८ ते २२ + संतवाणी (पृष्ठ ६८ ते ९०)
                └── README.md                           # Grade 3 Marathi overview and chapter index
```

---

## 🤖 How to Use with LLMs & AI Agents

The Markdown files in this repository are structured specifically for LLMs (Gemini, Claude, GPT-4, Llama 3). Here are primary use cases with ready-to-use prompt recipes:

### 1. 📖 24/7 AI Homework & Doubt Solver (RAG Context)
Feed the relevant lesson Markdown file into any LLM with the following prompt:
```text
System Prompt: You are a friendly, encouraging 3rd-grade Marathi school tutor.
Context: [Paste chapter markdown, e.g., part_1.md]
Task: Answer the student's question using simple Marathi, suitable for an 8-year-old child. Provide examples and encourage critical thinking.
```

### 2. 📝 Automated Exam Worksheet & Practice Paper Generator
Generate customized test papers based on the Maharashtra State Board pattern:
```text
Context: [Paste part_2.md / part_3.md]
Prompt: Based on the provided Marathi lessons, create a 20-mark practice test for a 3rd grader with:
1. रिकाम्या जागा भरा (Fill in the blanks) - 4 Marks
2. योग्य जोड्या लावा (Match the following) - 4 Marks
3. एका वाक्यात उत्तरे लिहा (One-sentence answers) - 4 Marks
4. व्याकरण: समानार्थी / विरुद्धार्थी शब्द व लिंग बदला - 4 Marks
5. दोन-तीन वाक्यांत उत्तरे लिहा - 4 Marks
Provide the answer key at the end for parents.
```

### 3. 📇 Flashcard & Vocabulary Generator (Anki / Quizlet)
Extract vocabulary and grammar drills into spreadsheet/Anki-compatible format:
```text
Context: [Paste Grade_3_Marathi_Balbharati_Complete.md]
Prompt: Extract all entries from "नवीन शब्द शिकू या" (Vocabulary) and "खेळू या शब्दांशी" across all chapters into a clean CSV table with columns: [शब्द (Word), अर्थ (Meaning), वाक्यात उपयोग (Example Sentence), धडा (Chapter)].
```

### 4. 🌐 Bilingual Bridge for Parents (Marathi ↔ English/Hindi)
For parents who want to understand what their child is learning in Marathi medium:
```text
Context: [Paste poem/story text]
Prompt: Explain this Marathi poem line-by-line in simple English, highlighting the poetic meaning, cultural context, and key Marathi vocabulary words to teach my 3rd grader.
```

### 5. 🗣️ Speech Synthesis & Pronunciation Practice (TTS)
Because the text is 100% standard Unicode Devanagari, it integrates seamlessly with Text-to-Speech (TTS) models (e.g. Google Cloud TTS Marathi, ElevenLabs) to read out poems with rhythm and stories with natural expression.

---

## 🎮 Upcoming Roadmap: HTML5 AI Games & Assistive Tools

We are building a suite of lightweight, browser-based HTML5 educational games and AI tools:

### 🕹️ Interactive Learning Games
- **🧩 शब्दकोडे (Marathi Crosswords & Word Hunt)**: Interactive grid puzzles generated dynamically from textbook vocabulary.
- **⚔️ व्याकरण चॅम्पियन (Grammar Quest)**: Fast-paced drag-and-drop game for *लिंग (Gender)*, *वचन (Singular/Plural)*, and *विरामचिन्हे (Punctuation)*.
- **🎤 कविता गाऊ या (Poem Karaoke & Rhyme Matcher)**: Audio-assisted poem recitation and rhyming word matching.
- **🎭 पात्र संवाद (Roleplay with Story Characters)**: Talk to characters like *तेनालीराम (Tenalirama)* or *हिरकणी (Hirakani)* powered by Gemini / LLM backend.

### 🛠️ Parent & Teacher Assistive Tools
- **📄 1-Click Printable Worksheet Maker**: Generate printable PDF revision sheets with answer keys.
- **📊 Concept & Weak-Area Diagnostic**: Interactive quiz assessing comprehension and identifying areas needing practice.
- **🎙️ Reading Fluency Coach**: Voice-enabled web widget that listens to child reading Marathi text and gives encouraging pronunciation feedback.

---

## 🤝 Contributing & Community

Contributions are welcome! You can help by:
- Adding clean Unicode transcriptions for other grades (Grade 1 to 10) and subjects (गणित, परिसर अभ्यास, इंग्रजी, विज्ञान).
- Contributing HTML5 AI game templates.
- Sharing effective prompt templates and homework assistance workflows.

---

## 📄 License & Attribution

- **Textbook Content**: Source material belongs to the *Maharashtra State Bureau of Textbook Production & Curriculum Research (Balbharati), Pune*. Digitized and structured for educational, non-commercial, and assistive study purposes.
- **Code, Scripts & Tools**: Released under the [MIT License](LICENSE).
