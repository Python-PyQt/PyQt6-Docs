.. sip:class-description::
    :status: todo
    :brief: Interface for receiving audio data from an audio input device
    :digest: 67e057a80502f5f13c85e6b63a95f881

The :sip:ref:`~PyQt6.QtMultimedia.QAudioSource` class provides an interface for receiving audio data from an audio input device.

You can construct an audio input with the system's default audio input device. It is also possible to create :sip:ref:`~PyQt6.QtMultimedia.QAudioSource` with a specific :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice`. When you create the audio input, you should also send in the :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat` to be used for the recording (see the :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat` class description for details).

To record to a file:

:sip:ref:`~PyQt6.QtMultimedia.QAudioSource` lets you record audio with an audio input device. The default constructor of this class will use the systems default audio device, but you can also specify a :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice` for a specific device. You also need to pass in the :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat` in which you wish to record.

Starting up the :sip:ref:`~PyQt6.QtMultimedia.QAudioSource` is simply a matter of calling :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.start` with a :sip:ref:`~PyQt6.QtCore.QIODevice` opened for writing. For instance, to record to a file, you can:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py
    :lines: 68-69

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py
    :lines: 76-97

This will start recording if the format specified is supported by the input device (you can check this with :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice.isFormatSupported`. In case there are any snags, use the :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.error` function to check what went wrong. We stop recording in the ``stopRecording()`` slot.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py
    :lines: 101-106

At any point in time, :sip:ref:`~PyQt6.QtMultimedia.QAudioSource` will be in one of four states: active, suspended, stopped, or idle. These states are specified by the :sip:ref:`~PyQt6.QtMultimedia.QAudio.State` enum. You can request a state change directly through :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.suspend`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.resume`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.stop`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.reset`, and :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.start`. The current state is reported by :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.state`. :sip:ref:`~PyQt6.QtMultimedia.QAudioSink` will also signal you when the state changes (\ :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.stateChanged`).

:sip:ref:`~PyQt6.QtMultimedia.QAudioSource` provides several ways of measuring the time that has passed since the :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.start` of the recording. The ``processedUSecs()`` function returns the length of the stream in microseconds written, i.e., it leaves out the times the audio input was suspended or idle. The :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.elapsedUSecs` function returns the time elapsed since :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.start` was called regardless of which states the :sip:ref:`~PyQt6.QtMultimedia.QAudioSource` has been in.

If an error should occur, you can fetch its reason with :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.error`. The possible error reasons are described by the :sip:ref:`~PyQt6.QtMultimedia.QAudio.Error` enum. The :sip:ref:`~PyQt6.QtMultimedia.QAudioSource` will enter the :sip:ref:`~PyQt6.QtMultimedia.QAudio.State.StoppedState` when an error is encountered. Connect to the :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.stateChanged` signal to handle the error:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py
    :lines: 110-129

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioSink`, :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice`.
