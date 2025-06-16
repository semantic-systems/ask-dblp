# import csv
#
# input_csv = 'dblp-sparql-logs-2025-05-13.csv'  # Name of CSV file
# sparql_col = 'query'                 # Change to your actual column name
# max_lines = 1000
# unique_trigrams = set()
# distinct_rows = []
# nohash_rows = []
import csv

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


if __name__ == "__main__":
    #preview_csv('your_large_sparqls.csv')
    process_sparql_csv('log_data/dblp-sparql-logs-2025-05-13.csv', max_lines=1000, sparql_col='query')