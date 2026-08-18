# Experiment 1: Working with Text Input and Python Data Structures

## 1. Objective / Aim
To read raw text from different input sources (`.txt`, `.csv`, `.json`, interactive string input) and represent/manipulate them using appropriate Python data structures (`str`, `list`, `tuple`, `dict`, `set`, `pd.DataFrame`) applied to **Terms & Conditions documents** (Amazon & Alibaba).

---

## 2. What We Did (Step-by-Step Explanation)

### Step 1: String Operations (`str`)
- **What:** Took a sample legal clause (`"Amazon reserves the right to refuse service, terminate accounts..."`) and performed string methods.
- **How:**
  - Length of text (`len(text)`), length without whitespace (`len(text.replace(" ", ""))`), and word count (`len(text.split())`).
  - Case normalisation (`text.lower()`, `text.upper()`).
  - Keyword lookup using Python's `in` operator (e.g. `'terminate' in text.lower()`).

### Step 2: Safe File Reading with UTF-8 (`.txt`)
- **What:** Ingested unstructured text files (`amazon.txt` & `alibaba.txt`).
- **How:** Used a safe reader function wrapped with `try-except` blocks handling `FileNotFoundError` and `UnicodeDecodeError` with explicit `utf-8` encoding.

### Step 3: Line-by-Line Clause Extraction (`list`, `tuple`, `set`)
- **What:** Extracted contract provisions and organized them into primitive collections.
- **How:**
  - **List:** Read lines sequentially, stripped leading/trailing spaces, and filtered out empty lines/headers.
  - **Tuple:** Created immutable pairs `(clause_index, word_count, clause_snippet)` for fixed structured records.
  - **Set:** Built unique legal vocabulary sets from Amazon and Alibaba clauses. Used `set.intersection()` to identify shared contractual terms (e.g., *services, accounts, dispute, arbitration, liability*).

### Step 4: Structured Data Ingestion (`.csv`) with Pandas DataFrame
- **What:** Loaded `tc_clauses.csv` (17 labeled legal clauses from Amazon and Alibaba).
- **How:**
  - Inspected dataset shape (`df.shape`), missing values (`df.isnull().sum()`), and class balance (`df['risk_level'].value_counts()`).
  - Engineered new feature columns: `word_count` and `char_count`.
  - Analyzed risk levels across categories using contingency tables (`pd.crosstab`).

### Step 5: Hierarchical JSON Parsing (`dict`)
- **What:** Ingested `tc_policies.json` containing company metadata, versions, sections, and sub-clauses.
- **How:** Built a fast lookup dictionary `{Company -> {Section_Name -> [Clauses]}}` to query clauses by section name (e.g., querying Alibaba's *"Limitation of Liability"* section).

### Step 6: Extension Activity
- **What:** Aggregated clause statistics across companies and risk levels.
- **How:** Grouped data by `['company', 'risk_level']` and computed mean/min/max word counts and character counts.

---

## 3. How to Answer When Asked (Viva / Exam Points)
- **Why use Tuples?** Tuples are immutable and memory-efficient; ideal for fixed records like `(clause_id, word_count)`.
- **Why use Sets?** Sets only store unique elements and provide $O(1)$ lookup time for vocabulary extraction and set operations (`intersection`, `difference`).
- **Why use Pandas DataFrames?** DataFrames provide tabular data structures with native support for filtering, missing-value handling, grouping, and batch feature engineering.
- **Why explicit UTF-8 encoding?** Prevents `UnicodeDecodeError` when reading legal text containing special quotation marks, copyright signs (`©`), or dashes.
