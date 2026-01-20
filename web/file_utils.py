import os
import tempfile

def process_file_safely(file_stream, processor_fn):
    with tempfile.NamedTemporaryFile(delete=True) as tmp:
        tmp.write(file_stream.read())
        tmp.flush()
        return processor_fn(tmp.name)

