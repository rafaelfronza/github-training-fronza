from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)  # Moved this line outside the function

output_directory = "webhook_data"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def create_app():
    @app.route('/webhook', methods=['POST'])
    def webhook_listener():
        if request.headers.get('X-GitHub-Event') == 'push':
            payload = request.json
            # Handle the GitHub push event here
            print("Received push event from GitHub:")
            print(payload)
            
            # Save the JSON data to a file
            filename = f"{output_directory}/{payload['repository']['name']}_{payload['after']}.json"
            with open(filename, 'w') as file:
                json.dump(payload, file, indent=4)

            return 'Webhook received and data saved', 200
        else:
            return 'Not a push event', 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
