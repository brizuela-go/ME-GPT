from elevenlabslib import ElevenLabsUser
from dotenv import load_dotenv
import gradio as gr
import openai
# import winsound
from elevenlabslib import *
from pydub import AudioSegment
from pydub.playback import play
import io
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
api_key = os.getenv("ELEVENLABS_API_KEY")
user = ElevenLabsUser(api_key)

messages = [
    "You're name is Juan Eduardo Brizuela. You're 23 years old. You can speak multiple languages. "]

preamble = "You're name is Juan Eduardo Brizuela. You're 23 years old. You can speak multiple languages."


def transcribe(audio):
    global messages

    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    messages.append(f"\n{transcript['text']}")

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{preamble}{messages[-1]}",
        max_tokens=80,
        n=1,
        stop=None,
        temperature=0.5,
    )

    system_message = response["choices"][0]["text"]
    messages.append(f"{system_message}")

    voice = user.get_voices_by_name("Brizuela")[0]
    audio = voice.generate_audio_bytes(system_message)

    audio = AudioSegment.from_file(io.BytesIO(audio), format="mp3")
    audio.export("output.wav", format="wav")

    # winsound.PlaySound("output.wav", winsound.SND_FILENAME)

    # Replace winsound with pydub playback
    play(AudioSegment.from_wav("output.wav"))

    chat_transcript = "\n".join(messages)
    return chat_transcript


iface = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(source="microphone", type="filepath",
                    placeholder="Please, start speaking. Remember to stop the recording once you're done..."),
    outputs="text",
    title="🤖 ME GPT 🤖",
    description="🌟 Please ask me your question and I will respond both verbally and in text to you...",
)

iface.launch()
