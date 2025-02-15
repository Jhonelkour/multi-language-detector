import os
import tkinter as tk
from tkinter import scrolledtext, ttk
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import text

# Mapping of ISO language codes to language names
ISO_LANGUAGE_NAMES = {
    "en": "English", "es": "Spanish", "fr": "French", "de": "German", "it": "Italian",
    "pt": "Portuguese", "nl": "Dutch", "ru": "Russian", "zh": "Chinese", "ar": "Arabic",
    "ja": "Japanese", "ko": "Korean", "hi": "Hindi", "tr": "Turkish", "pl": "Polish",
    "sv": "Swedish", "fi": "Finnish", "da": "Danish", "no": "Norwegian", "el": "Greek",
    "he": "Hebrew", "th": "Thai"
}

# Path to the folder containing text files
FOLDER_PATH = "./"  # Change as needed

# Initialize the language detector
base_options = mp_python.BaseOptions(model_asset_path="language_detector.tflite")
options = text.LanguageDetectorOptions(base_options=base_options)
detector = text.LanguageDetector.create_from_options(options)

# Function to process files and update GUI
def process_files():
    txt_files = [f for f in os.listdir(FOLDER_PATH) if f.endswith(".txt")]
    txt_files.sort()
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    
    if not txt_files:
        output_text.insert(tk.END, "❌ No text files found in the folder.\n")
        output_text.config(state=tk.DISABLED)
        return
    
    for file_name in txt_files:
        file_path = os.path.join(FOLDER_PATH, file_name)
        output_text.insert(tk.END, f"\n📂 Processing: {file_name}\n")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                input_text = file.read().strip()
            
            if not input_text:
                output_text.insert(tk.END, "⚠️ Skipping empty file.\n")
                continue
            
            detection_result = detector.detect(input_text)
            
            if detection_result.detections:
                output_text.insert(tk.END, "📝 Detected Languages:\n")
                for detection in detection_result.detections:
                    language_name = ISO_LANGUAGE_NAMES.get(detection.language_code, "Unknown Language")
                    output_text.insert(tk.END, f"  - {detection.language_code} ({language_name}): ({detection.probability:.2f})\n")
            else:
                output_text.insert(tk.END, "⚠️ No language detected.\n")
        except Exception as e:
            output_text.insert(tk.END, f"❌ Error processing {file_name}: {e}\n")
    
    output_text.config(state=tk.DISABLED)

# Create GUI window
root = tk.Tk()
root.title("Language Detector")
root.geometry("700x500")
root.configure(bg="#f0f0f0")

# Header label
header_label = ttk.Label(root, text="Language Detector", font=("Arial", 16, "bold"), background="#f0f0f0")
header_label.pack(pady=10)

# Create a frame for button
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=5)

# Create a button to trigger file processing
process_button = ttk.Button(button_frame, text="Process Files", command=process_files)
process_button.pack()

# Create a frame for the output text
txt_frame = tk.Frame(root, bg="#f0f0f0")
txt_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# Create a scrollable text widget for output
output_text = scrolledtext.ScrolledText(txt_frame, wrap=tk.WORD, height=20, width=80, font=("Arial", 12))
output_text.pack(fill=tk.BOTH, expand=True)
output_text.config(state=tk.DISABLED)

# Run the GUI
root.mainloop()
