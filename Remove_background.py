import shutil
import pathlib
from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter

path = list(pathlib.Path.cwd().parents)[1].joinpath('c/sound_detect')

#delete_path = path.joinpath('audio_spleeter_out')
#try:
    #shutil.rmtree(delete_path)
#except OSError as e:
    #print(e)
#else:
    #print("The directory is deleted successfully")

print(path)
mp3_path = path.joinpath('music/紳士.mp3')
out_path = path.joinpath('audio_spleeter_out')
print(mp3_path)
print(out_path)
separator = Separator('spleeter:2stems')
default_adapter = AudioAdapter.default()
separator.separate_to_file(str(mp3_path),out_path,audio_adapter=default_adapter,synchronous=False)
