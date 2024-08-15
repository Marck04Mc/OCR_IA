from flask import Flask, jsonify, request
from logic.ocr_processing import producer_consumer
from logic.text_analysis import analyze_text
from connections.connection import connect_db

app = Flask(__name__)

@app.route('/procesar_ocr', methods=['POST'])
def procesar_ocr():
    data = request.json
    num_cores = data.get('num_cores', 1)
    pdf_files = data.get('pdf_files', [])
    
    texts = producer_consumer(pdf_files, num_cores)
    return jsonify({"message": "Procesamiento completado", "texts": texts})

@app.route('/procesar_texto', methods=['POST'])
def procesar_texto():
    data = request.json
    text = data.get('text', '')
    publication_date = data.get('publication_date', '')
    newspaper_name = data.get('newspaper_name', '')
    
    military_units, political_divisions = analyze_text(text, publication_date, newspaper_name)
    return jsonify({"message": "Análisis completado", "military_units": military_units, "political_divisions": political_divisions})

@app.route('/estadisticas', methods=['GET'])
def estadisticas():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*), AVG(processing_time) FROM processed_files")
    total_files, avg_processing_time = cur.fetchone()
    
    cur.execute("SELECT SUM(processing_time) FROM processed_files")
    total_processing_time = cur.fetchone()[0]
    
    cur.close()
    conn.close()
    
    return jsonify({
        "total_archivos_procesados": total_files,
        "tiempo_promedio_ocr": avg_processing_time,
        "tiempo_total_ocr": total_processing_time
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
