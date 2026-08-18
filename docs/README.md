# Terms and Conditions Summarizer — NLP Practical Journal (Exp 1 - 3)

This directory contains detailed, step-by-step explanations and viva/interview cheat sheets for the first 3 NLP practical experiments applied to the **Terms & Conditions Summarizer** domain (using Amazon and Alibaba Terms of Use).

---

## Quick Index of Experiment Documents

| Experiment | Title | Document Link | Key Concepts & Tools |
| :--- | :--- | :--- | :--- |
| **Experiment 1** | Working with Text Input & Python Data Structures | [EXPERIMENT_1_EXPLANATION.md](file:///c:/Users/Saloni/OneDrive/Documents/AntiG/BE/nlp/docs/EXPERIMENT_1_EXPLANATION.md) | File I/O (`utf-8`), `str`, `list`, `tuple`, `set` (vocabulary), `dict` (JSON parsing), `pd.DataFrame` |
| **Experiment 2** | Text Cleaning Using Python & Regular Expressions | [EXPERIMENT_2_EXPLANATION.md](file:///c:/Users/Saloni/OneDrive/Documents/AntiG/BE/nlp/docs/EXPERIMENT_2_EXPLANATION.md) | `BeautifulSoup` (HTML), `re.sub` (URLs, emails, phones), Over-cleaning vs Legal-Aware Cleaning, Legal Regex Scanner |
| **Experiment 3** | Sentence and Word Tokenisation | [EXPERIMENT_3_EXPLANATION.md](file:///c:/Users/Saloni/OneDrive/Documents/AntiG/BE/nlp/docs/EXPERIMENT_3_EXPLANATION.md) | NLTK (`sent_tokenize`, `word_tokenize`), spaCy (`en_core_web_sm`), Contractions, Abbreviations, Complexity Ranker |

---

## 💡 Quick 2-Minute Summary for Viva / Project Presentation

### 1. What is the Project Topic?
**Terms & Conditions Summarizer**: Developing foundational NLP pipelines to ingest, clean, tokenize, and analyze long and complex legal agreements (such as Amazon Conditions of Use and Alibaba Membership Agreements) to make them easily readable and summarizable.

### 2. What was accomplished across Experiments 1 to 3?
1. **Experiment 1 (Data Ingestion & Structures):**
   - Ingested raw contract text (`.txt`), labeled clauses (`.csv`), and hierarchical policies (`.json`).
   - Organized legal data into immutable tuples, extracted shared legal vocabulary using Python `set`s, and created feature columns (`word_count`, `char_count`) in Pandas.
2. **Experiment 2 (Domain-Specific Cleaning):**
   - Stripped web boilerplate, HTML tags, URLs, and emails.
   - Preserved domain-critical legal tokens that generic cleaning removes: monetary caps (`$500`), percentages (`100%`), section numbers (`Section 3.1(b)`), and legal negation (`NOT`, `NO`, `WITHOUT`).
   - Built regex pattern matchers to detect *Termination triggers*, *Disclaimers*, and *Arbitration venues*.
3. **Experiment 3 (Tokenisation & Segmentation):**
   - Segmented multi-clause paragraphs into discrete sentences and tokens using **NLTK** and **spaCy**.
   - Benchmarked token handling on legal abbreviations (`Sec.`, `e.g.`) and contractions (`isn't`).
   - Built a complexity ranker to flag excessively dense legal clauses for downstream summarization.
