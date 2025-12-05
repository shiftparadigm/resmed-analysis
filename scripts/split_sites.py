#!/usr/bin/env python3
"""Split sites into chunks for parallel agent analysis."""
import csv
import json
from pathlib import Path

def split_sites_into_chunks(input_csv: str, output_dir: str, num_chunks: int = 4):
    """Split sites CSV into N chunks for parallel processing."""

    # Read sites
    sites = []
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        sites = list(reader)

    # Remove empty rows
    sites = [s for s in sites if s.get('url')]

    print(f"Total sites: {len(sites)}")

    # Calculate chunk size
    chunk_size = (len(sites) + num_chunks - 1) // num_chunks

    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Split into chunks
    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = min((i + 1) * chunk_size, len(sites))
        chunk = sites[start_idx:end_idx]

        # Write CSV chunk
        csv_file = output_path / f"chunk_{i+1}_sites.csv"
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            if chunk:
                writer = csv.DictWriter(f, fieldnames=chunk[0].keys())
                writer.writeheader()
                writer.writerows(chunk)

        # Write JSON with just URLs for easier consumption
        json_file = output_path / f"chunk_{i+1}_urls.json"
        urls = [s['url'] for s in chunk]
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump({"chunk": i+1, "total_chunks": num_chunks, "sites": urls}, f, indent=2)

        print(f"Chunk {i+1}: {len(chunk)} sites ({start_idx+1}-{end_idx})")
        print(f"  Written to: {csv_file.name} and {json_file.name}")

    print(f"\nChunks written to: {output_path}")

if __name__ == "__main__":
    split_sites_into_chunks(
        input_csv="data/resmed_sites.csv",
        output_dir="data/chunks",
        num_chunks=4
    )
