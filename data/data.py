import os

def split_csv_by_size(input_file, output_dir, max_chunk_size_mb=10, max_chunks=10):
    max_chunk_size = max_chunk_size_mb * 1024 * 1024  # Convert MB to bytes

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r', encoding='utf-8') as infile:
        header = infile.readline()
        chunk_index = 1
        output_path = os.path.join(output_dir, f'chunk_{chunk_index}.csv')
        outfile = open(output_path, 'w', encoding='utf-8')
        outfile.write(header)
        current_size = len(header.encode('utf-8'))

        for line in infile:
            encoded_line = line.encode('utf-8')
            line_size = len(encoded_line)
            if current_size + line_size > max_chunk_size and chunk_index < max_chunks:
                outfile.close()
                chunk_index += 1
                output_path = os.path.join(output_dir, f'chunk_{chunk_index}.csv')
                outfile = open(output_path, 'w', encoding='utf-8')
                outfile.write(header)
                current_size = len(header.encode('utf-8'))

            outfile.write(line)
            current_size += line_size

        outfile.close()

# Example usage:
split_csv_by_size('/Users/luna/Desktop/PhishingAwarenessTrainingRAG/data/CEAS_08.csv', 'output_chunks', max_chunk_size_mb=10)