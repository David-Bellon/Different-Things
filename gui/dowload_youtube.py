from pytube import YouTube


def dowload(url, audio_path):
    try:
        video = YouTube(url)
        best_audio = video.streams.filter(only_audio=True, file_extension="mp4")[0]
        for i, stream in enumerate(video.streams.filter(only_audio=True, file_extension="mp4")):
            if stream.abr > best_audio.abr:
                best_audio = stream

        best_audio.download(audio_path)
        return f"Dowload Complete. Audio place in {audio_path}"
    except:
        return "Error during Dowload. Check the url is a valid one"