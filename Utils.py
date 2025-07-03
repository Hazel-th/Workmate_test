import csv

class Utils():
    
    @staticmethod
    def read_csv_in_chunks(filepath):
        CHUNK_SIZE = 1000
        
        with open(filepath, newline="", encoding="utf-8") as f:
            
            reader = csv.reader(f)
            headers = next(reader)
            chunk = []
            for row in reader:
                chunk.append(row)
                if len(chunk) >= CHUNK_SIZE:
                    yield headers, chunk
                    chunk = []
            if chunk:
                yield headers, chunk