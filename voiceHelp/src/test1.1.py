import os
from pocketsphinx import LiveSpeech, get_model_path, Decoder, DefaultConfig, Jsgf
from datetime import datetime

model_path = get_model_path()

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'zero_ru.cd_cont_4000'),
    lm=os.path.join(model_path, 'ru.lm'),
    dic=os.path.join(model_path, 'ru.dic')
)

print("Say something!")
config = Decoder.default_config()
config.set_string('-hmm', 'zero_ru.cd_cont_4000')
config.set_string('-lm', 'ru.lm')
config.set_string('-dict', 'ru.dic')
decoder = Decoder(config)

# fsg.writefile('goforward.fsg')

# jsgf = Jsgf('goforward.gram')
# rule = jsgf.get_rule('goforward.move2')
# fsg = jsgf.build_fsg(rule, decoder.get_logmath(), 7.5)
# fsg.writefile('goforward.fsg')
#
# decoder.set_fsg("goforward", fsg)
# decoder.set_search("goforward")
#
# jsgf_file.jsgf = 'with-neighbors.jsgf'
jsgf_file = 'jsgf_file.jsgf'
decoder.set_jsgf_file('grammar', jsgf_file)
# decoder.set_jsgf('grammar', jsgf_file.jsgf)
decoder.set_search('grammar')

print("go!")


while True:
    decoder.start_utt()
    time_1 = datetime.now()
    print("time_1", time_1)
    stream = open('goforward3.raw', 'rb')
    while True:
        buf = stream.read(1024)
        if buf:
             decoder.process_raw(buf, False, False)
        else:
             break
    time_2 = datetime.now()
    print("time_2", time_2)
    print("t1-t2", time_2 - time_1)
    decoder.end_utt()
    print('Decoding with "goforward" grammar:', decoder.hyp().hypstr)

# for phrase in speech:
#     print(phrase)