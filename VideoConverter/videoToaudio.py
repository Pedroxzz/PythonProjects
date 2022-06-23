# IMPORTANTE FAZER O PIP INSTALL MOVIEPY ANTES
import moviepy.editor

# Carrega o arquivo/URL do video
video = moviepy.editor.VideoFileClip("opa.mp4")

# Extrai o áudio do vídeo
audio_data = video.audio

# Salva o arquivo de áudio extraido
audio_data.write_audiofile("audio.mp4")