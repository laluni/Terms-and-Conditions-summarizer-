# Experiment 3: Sentence and Word Tokenisation

## 1. Objective / Aim
To segment continuous legal contractual agreements into discrete sentences (clauses) and words (tokens) using **NLTK** and **spaCy**, and analyze how different tokenization strategies handle legal domain challenges (abbreviations, contractions, punctuation).

---

## 2. What We Did (Step-by-Step Explanation)

### Step 1: NLTK Tokenisation
- **What:** Applied NLTK's `sent_tokenize` and `word_tokenize` on long-form legal text.
- **How:**
  - `sent_tokenize`: Uses the Punkt tokenizer (an unsupervised algorithm trained to identify abbreviation periods vs sentence boundaries).
  - `word_tokenize`: Splits words, separates trailing periods and quotation marks into separate tokens.

### Step 2: spaCy Linguistic Tokenisation & Attribute Extraction
- **What:** Loaded spaCy's `en_core_web_sm` model and parsed the legal contract into a `Doc` object.
- **How:**
  - Extracted sentences using `doc.sents` (which uses dependency parse information to determine true clause boundaries).
  - Inspected token-level linguistic attributes using a DataFrame:
    - `token.is_alpha`: Whether token is purely alphabetic.
    - `token.is_punct`: Whether token is punctuation.
    - `token.is_stop`: Whether token is a standard stop word.
    - `token.like_num`: Whether token represents a numeric value or monetary figure.

### Step 3: Comparative Analysis (Python `split()` vs NLTK vs spaCy)
- **What:** Evaluated tokenization on a tricky legal sentence:  
  `"Alibaba.com isn't liable for user's $500 loss under Sec. 4.2(b), e.g., system outages."`
- **Key Findings:**
  1. **Python `split()` (Naïve):**
     - Keeps punctuation glued to words (e.g. `'outages.'`, `'$500'`).
     - Fails to split contractions (`"isn't"` remains one token).
     - Fails on abbreviations (`'Sec.'`, `'e.g.,'`).
  2. **NLTK `word_tokenize`:**
     - Separates contractions linguistically into verb and negation: `['is', "n't"]`.
     - Separates punctuation into individual tokens (`['$', '500']`).
  3. **spaCy Tokeniser:**
     - Non-destructive (preserves character offsets).
     - Correctly identifies `Sec.` and `e.g.` as abbreviations without falsely breaking sentences.
     - Grammatically splits contractions `['is', "n't"]` for downstream POS tagging and parsing.

### Step 4: Full Corpus Tokenisation Metrics (Amazon vs Alibaba)
- **What:** Processed the entire `amazon.txt` and `alibaba.txt` datasets through spaCy.
- **How:** Computed and tabulated corpus-level statistics:
  - Total Sentences
  - Total Tokens
  - Average Tokens per Sentence (~25-30 tokens/sentence, showing high syntactic complexity of legal language)
  - Punctuation count & Stop word counts.

### Step 5: Extension Activity (High-Complexity Legal Sentence Ranker)
- **What:** Designed an automated complexity ranker to identify the longest and most convoluted contractual clauses.
- **How:** Calculated token length and **Punctuation Density Percentage** (`(punct_count / total_tokens) * 100`). Filtered and ranked the top 5 longest clauses (prime candidates for text summarization).

---

## 3. How to Answer When Asked (Viva / Exam Points)
- **What is Tokenisation?** The process of breaking a continuous stream of text into smaller discrete linguistic units (sentences or words) for computational analysis.
- **Why is Python `split()` not sufficient?** `split()` only splits on whitespace. It cannot separate punctuation from words, cannot separate contractions (`don't` $\rightarrow$ `do` + `n't`), and cannot distinguish period in abbreviations (`e.g.`, `Inc.`, `Dr.`) from end-of-sentence periods.
- **Difference between NLTK and spaCy tokenization?**
  - NLTK uses rule-based and regular expression models (Punkt).
  - spaCy uses rule-based tokenization combined with statistical dependency parsing for sentence segmentation, making it more robust and industrial-grade.
- **Why is tokenisation critical for Summarization?** Summarization algorithms operate at the sentence level (extractive summarization) or sub-word/token level (abstractive models). Incorrect sentence boundaries lead to broken, incoherent summaries.
