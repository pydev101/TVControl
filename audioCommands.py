import speech_recognition as sr


def handleCommand(text):
    print(text)


class Recog:
    active = True

    def __init__(self):
        self.recognizer = sr.Recognizer()
        print("ADJUSTING")
        m = sr.Microphone()
        with m as source:
            self.recognizer.adjust_for_ambient_noise(source)
        print("DONE ADJUST")

        # `stop_listening` is now a function that, when called, stops background listening
        self.stop_listening = self.recognizer.listen_in_background(m, self.callback)
        # calling this function requests that the background listener stop listening
        # stop_listening(wait_for_stop=False)

    def callback(self, rec, audio):
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            if self.active:
                handleCommand(rec.recognize_google(audio))
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            pass

