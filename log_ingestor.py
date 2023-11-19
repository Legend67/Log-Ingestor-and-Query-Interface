from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
logs = []


@app.route('/')
def hello_world():
    return 'Logs Ingesting Machine Try'


@app.route('/ingest', methods=['POST'])
def ingest_log():
    try:
        log_data = request.get_json(force=True)
        log_data['timestamp'] = log_data.get(
            'timestamp', datetime.utcnow().isoformat())
        logs.append(log_data)
        return jsonify({'status': 'success'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/query', methods=['GET'])
def query_logs():
    try:
        query_params = request.args.to_dict()
        filtered_logs = filter_logs(logs, query_params)
        return jsonify({'logs': filtered_logs})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


def filter_logs(logs, filters):
    filtered_logs = logs
    for key, value in filters.items():
        filtered_logs = [log for log in filtered_logs if str(
            log.get(key)) == str(value)]
    return filtered_logs


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=3000)