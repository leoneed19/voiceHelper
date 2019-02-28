import os
from pocketsphinx import AudioFile, get_model_path, get_data_path

model_path = get_model_path()
data_path = get_data_path()

config = {
    'verbose': False,
    'audio_file': os.path.join(data_path, 't.wav'),
    'buffer_size': 2048,
    'no_search': False,
    'full_utt': False,
    'hmm': os.path.join(model_path, 'zero_ru.cd_cont_4000'),
    'lm': os.path.join(model_path, 'ru.lm'),
    'dict': os.path.join(model_path, 'ru.dic')
}

audio = AudioFile(**config)

for phrase in audio:
    print(phrase)