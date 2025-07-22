# import csv
#
# input_csv = 'dblp-sparql-logs-2025-05-13.csv'  # Name of CSV file
# sparql_col = 'query'                 # Change to your actual column name
# max_lines = 1000
# unique_trigrams = set()
# distinct_rows = []
# nohash_rows = []
import csv
from collections import Counter
from datasketch import MinHash, MinHashLSH
import pandas as pd
import re

def diversify_queries(
    input_csv: str,
    output_csv: str,
    query_col: str = "query",
    threshold: float = 0.3
):
    """
    Reads input_csv with columns ['id', 'question', 'query', ...],
    skips rows where the query contains '+',
    and writes a diversified subset to output_csv using MinHash (Jaccard) LSH.
    Only one representative per near-duplicate group is kept.
    """
    df = pd.read_csv(input_csv)
    # Filter out queries containing '+'
    df = df[df[query_col].apply(lambda x: '+' not in str(x) if pd.notnull(x) else False)]
    df = df.dropna(subset=[query_col])  # remove rows without a query

    queries = df[query_col].astype(str).tolist()

    def tokenize(text):
        text = re.sub(r'[^\w\s]', '', text.lower())
        return set(text.split())

    minhashes = []
    for q in queries:
        tokens = tokenize(q)
        m = MinHash(num_perm=128)
        for token in tokens:
            m.update(token.encode('utf8'))
        minhashes.append(m)

    lsh = MinHashLSH(threshold=threshold, num_perm=128)
    for i, mh in enumerate(minhashes):
        lsh.insert(f"q{i}", mh)

    seen = set()
    representative_indices = []

    for i, q in enumerate(queries):
        if i in seen:
            continue
        mh = minhashes[i]
        similar = lsh.query(mh)
        indices = [int(s[1:]) for s in similar]
        seen.update(indices)
        representative_indices.append(i)

    print(f"Total queries: {len(queries)}")
    print(f"Diversified queries: {len(representative_indices)}")

    diverse_df = df.iloc[representative_indices]
    diverse_df.to_csv(output_csv, index=False)
    print(f"Diversified queries written to {output_csv}")


def preview_csv(file_path, num_lines=3):
    """
    Print the first `num_lines` lines (including header) of a CSV file.
    """
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            print(row)
            if i + 1 >= num_lines:
                break

def get_trigram_after_hash(line):
    """
    If the line starts with #, return the first 3 words after leading hashes.
    Otherwise, return None.
    """
    line = line.lstrip()
    if line.startswith('#'):
        idx = 0
        while idx < len(line) and line[idx] == '#':
            idx += 1
        s = line[idx:].lstrip()
        words = s.split()
        return tuple(words[:3]) if words else None
    return None

def process_sparql_csv(
    input_csv,
    output_distinct='log_data/distinct_sparqls.csv',
    output_nohash='log_data/nohash_sparqls.csv',
    sparql_col=None,
    max_lines=None
    ):
    """
    Process a CSV, find distinct SPARQLs by first 3 words after #, and save others.
    If sparql_col is None, will use the first column.
    """
    unique_trigrams = set()
    distinct_rows = []
    nohash_rows = []

    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        # Determine SPARQL column if not given
        if sparql_col is None:
            sparql_col = reader.fieldnames[0]
            print(f"Guessing SPARQL column is: '{sparql_col}'")
        else:
            if sparql_col not in reader.fieldnames:
                raise ValueError(f"Column '{sparql_col}' not found in CSV headers: {reader.fieldnames}")
        for i, row in enumerate(reader):
            if max_lines and i >= max_lines:
                break
            sparql = row[sparql_col].lstrip()
            if not sparql.startswith('#'):
                nohash_rows.append(row)
            else:
                trigram = get_trigram_after_hash(sparql)
                if trigram and trigram not in unique_trigrams:
                    distinct_rows.append(row)
                    unique_trigrams.add(trigram)

    # Write results
    with open(output_distinct, 'w', newline='', encoding='utf-8') as out1:
        writer = csv.DictWriter(out1, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(distinct_rows)

    with open(output_nohash, 'w', newline='', encoding='utf-8') as out2:
        writer = csv.DictWriter(out2, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(nohash_rows)

    print(f"Wrote {len(distinct_rows)} distinct rows to {output_distinct}")
    print(f"Wrote {len(nohash_rows)} #less rows to {output_nohash}")


def split_sparql_logs(input_file, desc_file, direct_file, other_file):
    """
    Splits a large SPARQL log CSV into three files:
    - desc_file: entries with description (## ...), extracting 'question' and trimming from 'query'
    - direct_file: entries starting directly with PREFIX or SELECT
    - other_file: everything else
    CSVs are written efficiently line by line.
    """
    with open(input_file, newline='', encoding='utf-8') as infile, \
         open(desc_file, 'w', newline='', encoding='utf-8') as desc_out, \
         open(direct_file, 'w', newline='', encoding='utf-8') as direct_out, \
         open(other_file, 'w', newline='', encoding='utf-8') as other_out:

        reader = csv.DictReader(infile)
        desc_fieldnames = ['id', 'datetime', 'question', 'query']
        desc_writer = csv.DictWriter(desc_out, fieldnames=desc_fieldnames)
        direct_writer = csv.DictWriter(direct_out, fieldnames=reader.fieldnames)
        other_writer = csv.DictWriter(other_out, fieldnames=reader.fieldnames)
        desc_writer.writeheader()
        direct_writer.writeheader()
        other_writer.writeheader()

        for row in reader:
            q = row['query']
            if isinstance(q, str):
                query_strip = q.lstrip()
                if query_strip.startswith('##'):
                    # Extract description as 'question'
                    after_hash = query_strip[2:].lstrip()
                    idx_prefix = after_hash.upper().find('PREFIX')
                    idx_select = after_hash.upper().find('SELECT')
                    if idx_prefix != -1 and (idx_select == -1 or idx_prefix < idx_select):
                        idx = idx_prefix
                        question = after_hash[:idx].strip()
                        query_rest = after_hash[idx:].strip()
                    elif idx_select != -1:
                        idx = idx_select
                        question = after_hash[:idx].strip()
                        query_rest = after_hash[idx:].strip()
                    else:
                        question = after_hash.strip()
                        query_rest = ''
                    desc_writer.writerow({
                        'id': row['id'],
                        'datetime': row['datetime'],
                        'question': question,
                        'query': query_rest
                    })
                elif query_strip.lstrip('#').lstrip().upper().startswith('PREFIX') or \
                     query_strip.lstrip('#').lstrip().upper().startswith('SELECT'):
                    direct_writer.writerow(row)
                else:
                    other_writer.writerow(row)
            else:
                other_writer.writerow(row)


def collect__unique_queries(desc_file, out_file=None):
    """
    From desc_file (description_queries.csv), collect rows with unique 'question' values.
    If out_file is given, also write these unique rows to out_file as CSV with same columns.
    """
    with open(desc_file, newline='', encoding='utf-8') as infile:
        rows = list(csv.DictReader(infile))
    q_counts = Counter(row['question'] for row in rows)
    unique_rows = [row for row in rows if q_counts[row['question']] == 1]

    if out_file and unique_rows:
        with open(out_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=unique_rows[0].keys())
            writer.writeheader()
            writer.writerows(unique_rows)
    # return unique_rows


def jaccard_similarity(str1, str2):
    set1 = set(str1.lower().split())
    set2 = set(str2.lower().split())
    if not set1 or not set2:
        return 0.0
    return len(set1 & set2) / len(set1 | set2)

def filter_unique_questions_jaccard(input_file, output_file, threshold=0.8):
    """
    Writes only unique questions based on Jaccard similarity threshold.
    """
    unique_rows = []
    unique_questions = []

    with open(input_file, newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:

        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            question = row['question']
            if question.__contains__('+'):
                continue
            is_similar = False
            for existing in unique_questions:
                if jaccard_similarity(question, existing) >= threshold:
                    is_similar = True
                    break
            if not is_similar:
                unique_rows.append(row)
                unique_questions.append(question)
                writer.writerow(row)


def save_unique_trigram_queries(input_csv: str, output_csv: str, query_col: str = "question"):
    """
    Reads a CSV file and writes rows such that only the first row for each unique
    (case-insensitive) first three words ("trigram") in the `query` column is kept,
    and any queries containing a '+' character are skipped.

    All columns are preserved in the output.
    """
    df = pd.read_csv(input_csv)
    df = df.dropna(subset=[query_col])

    seen_prefixes = set()
    unique_rows = []

    def get_first_three_words(query):
        return ' '.join(str(query).strip().lower().split()[:3])

    for _, row in df.iterrows():
        query_val = str(row[query_col])
        if '+' in query_val:
            continue  # skip queries with '+'
        prefix = get_first_three_words(query_val)
        if prefix not in seen_prefixes:
            seen_prefixes.add(prefix)
            unique_rows.append(row)

    unique_df = pd.DataFrame(unique_rows)
    unique_df.to_csv(output_csv, index=False)
    print(f"Original queries: {len(df)}")
    print(f"Queries with unique first 3 words (and no '+'): {len(unique_rows)}")
    print(f"Written to: {output_csv}")


def filter_queries_by_jaccard(
    input_csv: str,
    output_csv: str,
    query_col: str = "question",
    threshold: float = 0.4
   ):
    """
    Reads input_csv, filters for diverse queries by Jaccard similarity.
    - Skips queries containing '+'
    - Only keeps a query if it's not too similar to any previously selected query
    - All columns are preserved
    """
    df = pd.read_csv(input_csv).dropna(subset=[query_col])
    seen_sets = []
    unique_rows = []

    def tokenize(query):
        query = re.sub(r'[^\w\s]', '', query.lower())
        return set(query.split())

    def jaccard(set1, set2):
        inter = len(set1 & set2)
        union = len(set1 | set2)
        return inter / union if union else 0

    for _, row in df.iterrows():
        q = str(row[query_col])
        if '+' in q:
            continue
        tokens = tokenize(q)
        if all(jaccard(tokens, s) < threshold for s in seen_sets):
            seen_sets.append(tokens)
            unique_rows.append(row)

    pd.DataFrame(unique_rows).to_csv(output_csv, index=False)
    print(f"Original queries: {len(df)}")
    print(f"Filtered (diverse) queries: {len(unique_rows)}")
    print(f"Written to: {output_csv}")


if __name__ == "__main__":
    #preview_csv('your_large_sparqls.csv')
    # process_sparql_csv('log_data/dblp-sparql-logs-2025-05-13.csv', max_lines=1000, sparql_col='query')
    # split_sparql_logs('log_data/dblp-sparql-logs-2025-05-13.csv', 'log_data/description_queries.csv', 'log_data/direct_queries.csv', 'log_data/other_rows.csv')
    # collect__unique_queries('log_data/description_queries.csv','log_data/unique_queries.csv')
    # filter_unique_questions_jaccard('log_data/unique_queries.csv', 'log_data/unique_queries_by_jacard_similarity.csv')
    # diversify_queries(
    #     'log_data/unique_queries.csv',
    #     'log_data/diverse_queries.csv',
    #     query_col='question',  # or your column name if different
    #     threshold=0.3  # set as desired for your level of diversification
    # )
    # save_unique_trigram_queries('log_data/description_queries.csv',"log_data/questions_with_distinct_trigram.csv")
    filter_queries_by_jaccard('log_data/description_queries.csv', 'log_data/filter_queries_by_jaccard_2.csv')
