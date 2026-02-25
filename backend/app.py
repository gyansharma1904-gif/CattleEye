from flask import Flask, request, jsonify
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder automatically if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/predict", methods=["POST"])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    file = request.files['image']
    
    # Generate unique filename
    unique_filename = str(uuid.uuid4()) + "_" + file.filename
    
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], unique_filename)
    
    file.save(file_path)

    return jsonify({
        "message": "Image saved successfully",
        "stored_as": unique_filename,
        "path": file_path
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/predict", methods=["POST"])
# def predict():
#     if 'image' not in request.files:
#         return jsonify({"error": "No image uploaded"}), 400
    
#     file = request.files['image']
    
#     return jsonify({
#         "message": "API working",
#         "filename": file.filename
#     })
    
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)