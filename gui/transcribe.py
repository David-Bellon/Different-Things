import subprocess
import whisper
import torch

def main_transcribe(input, model, device):
    #input = "audio.mp4"
    #output = "ouput.wav"
    #cuda = torch.device("cuda")
    model = "models\\" + model + ".pt"
    model = whisper.load_model(model, device=device)
    #subprocess.run(["ffmpeg", "-i", input, "-vn", "-acodec", "pcm_s16le", "-ar", "44100", "-ac", "2", output])
    out = model.transcribe(input, verbose=False)
    return out