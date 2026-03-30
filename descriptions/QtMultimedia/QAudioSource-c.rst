.. sip:class-description::
    :status: todo
    :brief: Interface for receiving audio data from an audio input device
    :digest: 60962b8256420941f6d94d02a60e7664

The :sip:ref:`~PyQt6.QtMultimedia.QAudioSource` class provides an interface for receiving audio data from an audio input device.

You can construct an audio input with the system's default audio input device. It is also possible to create :sip:ref:`~PyQt6.QtMultimedia.QAudioSource` with a specific :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice`. When you create the audio input, you should also send in the :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat` to be used for the recording (see the :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat` class description for details).

:sip:ref:`~PyQt6.QtMultimedia.QAudioSink` can be used in two different modes:

* Using a :sip:ref:`~PyQt6.QtCore.QIODevice` from an application thread

* Using a callback-based interface from the audio thread

.. _qaudiosource-qiodevice-interface:

QIODevice interface
-------------------

:sip:ref:`~PyQt6.QtMultimedia.QAudioSource` lets you record audio with an audio input device. The default constructor of this class will use the systems default audio device, but you can also specify a :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice` for a specific device. You also need to pass in the :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat` in which you wish to record.

Starting up the :sip:ref:`~PyQt6.QtMultimedia.QAudioSource` is simply a matter of calling :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.start` with a :sip:ref:`~PyQt6.QtCore.QIODevice` opened for writing. For instance, to record to a file, you can:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py
    :lines: 68-69

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py
    :lines: 76-97

This will start recording if the format specified is supported by the input device (you can check this with :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice.isFormatSupported`. In case there are any snags, use the :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.error` function to check what went wrong. We stop recording in the ``stopRecording()`` slot.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py
    :lines: 101-106

At any point in time, :sip:ref:`~PyQt6.QtMultimedia.QAudioSource` will be in one of four states: active, suspended, stopped, or idle. These states are specified by the QtAudio::State enum.

:sip:ref:`~PyQt6.QtMultimedia.QAudioSource` provides several ways of measuring the time that has passed since the :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.start` of the recording. The ``processedUSecs()`` function returns the length of the stream in microseconds written, i.e., it leaves out the times the audio input was suspended or idle. The :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.elapsedUSecs` function returns the time elapsed since :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.start` was called regardless of which states the :sip:ref:`~PyQt6.QtMultimedia.QAudioSource` has been in.

.. _qaudiosource-threading-model-and-buffering:

Threading model and buffering
.............................

The :sip:ref:`~PyQt6.QtCore.QIODevice` interface is designed to be used from the application thread. A wait-free ringbuffer is used to communicate to the audio thread. The size of this ringbuffer can be configured with :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.setBufferSize` and defaults to 250ms. The state of this buffer can be queried with bytesFree(). If the ringbuffer is full because the application does not read from the :sip:ref:`~PyQt6.QtCore.QIODevice` in time, the state will change to QtAudio::IdleState and resume to QtAudio::ActiveState once the application has read data from the :sip:ref:`~PyQt6.QtCore.QIODevice`. Note that this state change will drop audio data, so you should always read from the :sip:ref:`~PyQt6.QtCore.QIODevice` as fast as possible to avoid dropouts.

.. _qaudiosource-callback-interface:

Callback interface
------------------

The preferred way to achieve low audio latencies is to use the callback based interface. It allows you to read audio data directly from the audio device without having to go through a :sip:ref:`~PyQt6.QtCore.QIODevice`. This is done by calling :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.start` with a callback function that will be called from the audio thread. This callback function will be called with a QSpan<const SampleType> whenever the audio backend produces data.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py

Unlike the :sip:ref:`~PyQt6.QtCore.QIODevice`-based interface, the :sip:ref:`~PyQt6.QtMultimedia.QAudioSource` can only be in the states active, suspendend and stopped. The :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.setBufferSize` API is not available when using the callback, the size of the callback argument is determined by the audio backend.

**Note:** This API is only available on platforms that support the callback API: Apple's CoreAudio (macOS, iOS, etc), Windows, Linux (using the PulseAudio or PipeWire backend) and Android.

**Note:** The callback will be called on a soft-realtime audio thread. It is important to ensure that the callback does not block, as this can cause audio glitches or dropouts. This includes performing blocking IO, locking mutexes, allocating memories or any other operations that may block. For best practices consult Ross Bencina's article `Real-time audio programming 101: time waits for nothing <https://doc.qt.io/qt-6/http://www.rossbencina.com/code/real-time-audio-programming-101-time-waits-for-nothing>`_. Also consider using clang's `Realtime sanitizer <https://doc.qt.io/qt-6/https://clang.llvm.org/docs/RealtimeSanitizer.html>`_ to validate the audio callback.

.. _qaudiosource-state-and-error-handling:

State and error handling
------------------------

State changes are reported through the :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.stateChanged` signal. You can request a state change directly through :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.suspend`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.resume`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.stop`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.reset`, and :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.start`.

The :sip:ref:`~PyQt6.QtMultimedia.QAudioSource` will enter the StoppedState when an error is encountered. The error type can be retrieved :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.error` function. Please see the QtAudio::Error enum for a description of the possible errors that are reported. Calling :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.stop` or :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.reset` will reset the error state to NoError.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py
    :lines: 110-129

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioSink`, :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice`.
