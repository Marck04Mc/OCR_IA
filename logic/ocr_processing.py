import os
import time
import pytesseract
import multiprocessing
from pdf2image import convert_from_path
from connections.connection import connect_db
from datetime import datetime

def process_pdf(file_path):
    images = convert_from_path(file_path)
    text = ""

    start_time = time.time()
    for image in images:
        text += pytesseract.image_to_string(image)
    
    processing_time = time.time() - start_time
    
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO processed_files (file_name, file_path, processing_time, processed_date) VALUES (%s, %s, %s, %s)",
                (os.path.basename(file_path), file_path, processing_time, datetime.now()))
    conn.commit()
    cur.close()
    conn.close()
    
    return text

def producer_consumer(pdf_files, num_cores):
    with multiprocessing.Pool(num_cores) as pool:
        results = pool.map(process_pdf, pdf_files)
        return results
    

