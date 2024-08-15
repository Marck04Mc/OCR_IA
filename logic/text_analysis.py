import spacy
from datetime import time, datetime
from connections.connection import connect_db

nlp = spacy.load("es_core_news_sm")

def analyze_text(text, publication_date, newspaper_name):
    doc = nlp(text)
    military_units = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    political_divisions = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "LOC"]]
    
    processing_time = time.time()
    
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO analyzed_texts (military_units, political_divisions, publication_date, newspaper_name, processing_time, processed_date) VALUES (%s, %s, %s, %s, %s, %s)",
                (', '.join(military_units), ', '.join(political_divisions), publication_date, newspaper_name, processing_time, datetime.now()))
    conn.commit()
    cur.close()
    conn.close()
    
    return military_units, political_divisions
