import os
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import text

# Mapping of ISO language codes to language names
ISO_LANGUAGE_NAMES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "nl": "Dutch",
    "ru": "Russian",
    "zh": "Chinese",
    "ar": "Arabic",
    "ja": "Japanese",
    "ko": "Korean",
    "hi": "Hindi",
    "tr": "Turkish",
    "pl": "Polish",
    "sv": "Swedish",
    "fi": "Finnish",
    "da": "Danish",
    "no": "Norwegian",
    "el": "Greek",
    "he": "Hebrew",
    "th": "Thai"
}

# Path to the folder containing text files
FOLDER_PATH = "./"  # Change this to the folder where your files are stored

# Initialize the language detector
base_options = mp_python.BaseOptions(model_asset_path="language_detector.tflite")
options = text.LanguageDetectorOptions(base_options=base_options)
detector = text.LanguageDetector.create_from_options(options)

# Get all .txt files in the folder
txt_files = [f for f in os.listdir(FOLDER_PATH) if f.endswith(".txt")]
txt_files.sort()  # Sort files alphabetically

if not txt_files:
    print("❌ No text files found in the folder.")
    exit()

# Process each text file in order
for file_name in txt_files:
    file_path = os.path.join(FOLDER_PATH, file_name)
    print(f"\n📂 Processing: {file_name}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            input_text = file.read().strip()

        if not input_text:
            print("⚠️ Skipping empty file.")
            continue

        detection_result = detector.detect(input_text)

        if detection_result.detections:
            print("📝 Detected Languages:")
            for detection in detection_result.detections:
                language_name = ISO_LANGUAGE_NAMES.get(detection.language_code, "Unknown Language")
                print(f"  - {detection.language_code} ({language_name}): ({detection.probability:.2f})")
        else:
            print("⚠️ No language detected.")

    except Exception as e:
        print(f"❌ Error processing {file_name}: {e}")

print("\n✅ All files processed.")
