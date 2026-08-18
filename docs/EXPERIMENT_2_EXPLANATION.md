# Experiment 2: Text Cleaning Using Python and Regular Expressions

## 1. Objective / Aim
To clean, normalize, and preprocess raw, noisy Terms & Conditions / Privacy Policy text extracted from HTML sources using regular expressions (`re`) and `BeautifulSoup`, demonstrating the critical difference between **generic aggressive cleaning** and **legal-aware cleaning**.

---

## 2. What We Did (Step-by-Step Explanation)

### Step 1: Ingesting Raw Web-Scraped HTML
- **What:** Ingested `dirty_tc_sample.html`, a mock scraped contract containing HTML tags (`<h2>`, `<p>`, `<a>`), metadata, hyperlinks, contact emails, helpline phone numbers, and formatting boilerplate.

### Step 2: Modular Cleaning with `re` and `BeautifulSoup`
- **What:** Built isolated, reusable cleaning functions:
  1. **HTML Stripping:** `BeautifulSoup(text, "html.parser").get_text(" ")` to strip all HTML tags cleanly without merging adjacent words.
  2. **URL Removal:** `re.sub(r"https?://\S+|www\.\S+", " ", text)` to strip web links.
  3. **Email Address Removal:** `re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", " ", text)` to remove contact emails.
  4. **Phone Number Removal:** Regex to remove international and standard helpline numbers.
  5. **Whitespace Normalization:** `re.sub(r"\s+", " ", text).strip()` to collapse tabs, newlines, and multi-spaces into single spaces.

### Step 3: Generic Over-Cleaning vs. Domain-Specific Legal Cleaning
- **What:** Tested and compared two cleaning strategies on a high-risk liability clause:
  - Clause: `UNDER NO CIRCUMSTANCE SHALL THE COMPANY BE LIABLE FOR ANY AMOUNT EXCEEDING $500.00 USD OR 100% OF FEES PAID. We do NOT warrant error-free operation.`
  - **Aggressive Cleaner (Over-cleaning):** Stripped all digits (`\d+`), punctuation (`[^a-z\s]`), and lowercase everything.
    - *Problem:* Completely lost the monetary limit (`$500`), percentage (`100%`), and legal emphasis.
  - **Legal-Aware Cleaner:** Stripped HTML/URLs/boilerplate symbols (`©`, `®`, `•`) while **preserving monetary caps, percentages, section numbering (`Section 3.1(b)`), and negation words (`NOT`, `NO`, `WITHOUT`)**.

### Step 4: Batch Dataset Cleaning with Pandas
- **What:** Applied the legal-aware cleaner across all clauses in `tc_clauses.csv`.
- **How:** Calculated initial character length vs cleaned character length and computed the **Noise Reduction Percentage** across the dataset (average noise reduction ~3.5% to 5% without data loss).

### Step 5: Extension Activity (Legal Pattern Extractor via Regex)
- **What:** Created regular expression patterns to automatically flag high-risk contractual clauses:
  1. **Termination Triggers:** `(?:terminate|suspend|ban|cancel accounts?)\b`
  2. **Liability Disclaimers:** `(?:AS IS|NO LIABILITY|DISCLAIMS? ALL WARRANTIES|NOT BE LIABLE)\b`
  3. **Monetary Limits & Caps:** `\$\d+(?:,\d+)*(?:\.\d+)?|\b\d+%(?:\s+OF\s+[A-Z]+)?`
  4. **Arbitration & Jurisdictions:** `(?:arbitration|jury trial|dispute resolution|jurisdiction)\b`

---

## 3. How to Answer When Asked (Viva / Exam Points)
- **Why is regex preferred over `str.replace()`?** `str.replace()` only matches fixed literal substrings, whereas regex (`re.sub()`) matches flexible patterns (e.g. any email, any URL, any currency pattern).
- **What is the Danger of Over-Cleaning in Legal/Financial NLP?** Over-cleaning destroys critical semantic signals: removing numbers erases financial liability caps (`$500`), removing negation alters the entire legal meaning (`"liable"` vs `"NOT liable"`).
- **Why use `BeautifulSoup` instead of Regex for HTML?** HTML can have nested tags, broken formatting, and script blocks. A parser like `BeautifulSoup` accurately parses the DOM tree.
