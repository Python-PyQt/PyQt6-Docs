.. sip:class-description::
    :status: todo
    :brief: Convenient access to text-to-speech engines
    :digest: 32ed1109c77ef8e4b041101281a26f18

The :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech` class provides a convenient access to text-to-speech engines.

Use :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.say` to start reading text to the default audio device, and :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.stop`, :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.pause`, and :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.resume` to control the reading of the text.

.. literalinclude:: ../../../snippets/qtspeech-examples-speech-hello_speak-mainwindow.py
    :lines: 122-124

.. literalinclude:: ../../../snippets/qtspeech-examples-speech-hello_speak-mainwindow.py
    :lines: 127-129

.. literalinclude:: ../../../snippets/qtspeech-examples-speech-hello_speak-mainwindow.py
    :lines: 132-134

.. literalinclude:: ../../../snippets/qtspeech-examples-speech-hello_speak-mainwindow.py
    :lines: 137-137

To synthesize text into PCM data for further processing, use synthesize().

Use findVoices() to get a list of matching voices, or use :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.availableVoices` to get the list of voices that support the current locale. Change the :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.locale` property, using one of the :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.availableLocales` that is a good match for the language that the input text is in, and for the accent of the desired voice output. This will change the list of available voices on most platforms. Then use one of the available voices in a call to :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.setVoice`.

Not every engine supports all features. Use the :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.engineCapabilities` function to test which features are available, and adjust the usage of the class accordingly.

**Note:** Which locales and voices the engine supports depends usually on the Operating System configuration. E.g. on macOS, end users can install voices through the *Accessibility* panel in *System Preferences*.
