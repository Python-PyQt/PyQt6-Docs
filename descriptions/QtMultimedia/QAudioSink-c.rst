.. sip:class-description::
    :status: todo
    :brief: Interface for sending audio data to an audio output device
    :digest: d111de168f6c0012501ecf590bb6674c

The :sip:ref:`~PyQt6.QtMultimedia.QAudioSink` class provides an interface for sending audio data to an audio output device.

You can construct an audio output with the system's default audio output device. It is also possible to create :sip:ref:`~PyQt6.QtMultimedia.QAudioSink` with a specific :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice`. When you create the audio output, you should also send in the :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat` to be used for the playback (see the :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat` class description for details).

To play a file:

Starting to play an audio stream is simply a matter of calling :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.start` with a :sip:ref:`~PyQt6.QtCore.QIODevice`. :sip:ref:`~PyQt6.QtMultimedia.QAudioSink` will then fetch the data it needs from the io device. So playing back an audio file is as simple as:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py
    :lines: 143-144

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py
    :lines: 151-170

The file will start playing assuming that the audio system and output device support it. If you run out of luck, check what's up with the :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.error` function.

After the file has finished playing, we need to stop the device:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py

At any given time, the :sip:ref:`~PyQt6.QtMultimedia.QAudioSink` will be in one of four states: active, suspended, stopped, or idle. These states are described by the QtAudio::State enum. State changes are reported through the :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.stateChanged` signal. You can use this signal to, for instance, update the GUI of the application; the mundane example here being changing the state of a ``play/pause`` button. You request a state change directly with :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.suspend`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.stop`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.reset`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.resume`, and :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.start`.

If an error occurs, you can fetch the error type with the :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.error` function. Please see the QtAudio::Error enum for a description of the possible errors that are reported. The :sip:ref:`~PyQt6.QtMultimedia.QAudioSink` will enter the StoppedState when an error is encountered.

You can check for errors by connecting to the :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.stateChanged` signal:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py
    :lines: 174-195

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioSource`, :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice`.
