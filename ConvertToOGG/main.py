import os
from pydub import AudioSegment

input_folder = '../ConvertToOGG/input'
output_folder = '../ConvertToOGG/output'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(('.mp3', '.wav', '.flac', '.aac', '.m4a')):
        file_path = os.path.join(input_folder, filename)
        audio = AudioSegment.from_file(file_path)

        audio = audio.set_frame_rate(48000).set_channels(1)

        output_file_path = os.path.join(output_folder, f'{os.path.splitext(filename)[0]}.ogg')
        audio.export(output_file_path, format='ogg')

        print(f'변환 완료 {output_file_path}')