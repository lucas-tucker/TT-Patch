import torch
import torch.nn.functional as F
import torchaudio
import io

def mp3_compression(audio_tensor, sample_rate):
    tmp_buffer = io.BytesIO()
    torchaudio.save(tmp_buffer, 
                    audio_tensor, 
                    sample_rate, 
                    format="mp3", 
                    encoding="MP3", 
                    bitrate="64k")
    tmp_buffer.seek(0)
    pcm, _ = torchaudio.load(tmp_buffer, format="mp3")
    return pcm
