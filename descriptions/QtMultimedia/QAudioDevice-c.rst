.. sip:class-description::
    :status: todo
    :brief: Information about audio devices and their functionality
    :digest: 263de5a25805239a9c450b89046afa64

The :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice` class provides an information about audio devices and their functionality.

:sip:ref:`~PyQt6.QtMultimedia.QAudioDevice` describes an audio device available in the system, either for input or for playback.

A :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice` is used by Qt to construct classes that communicate with the device – such as :sip:ref:`~PyQt6.QtMultimedia.QAudioSource`, and :sip:ref:`~PyQt6.QtMultimedia.QAudioSink`. It is also used to determine the input or output device to use in a capture session or during media playback.

The :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice` instance retains its properties throughout its lifetime, even if the corresponding physical device is disconnected or its settings are modified. To keep track of updated properties, the user should load new instances of :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice` from :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` when the relevant signals are fired.

You can also query each device for the formats it supports. A format in this context is a set consisting of a channel count, sample rate, and sample type. A format is represented by the :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat` class.

The values supported by the device for each of these parameters can be fetched with :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice.minimumChannelCount`, :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice.maximumChannelCount`, :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice.minimumSampleRate`, :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice.maximumSampleRate` and :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice.supportedSampleFormats`. The combinations supported are dependent on the audio device capabilities. If you need a specific format, you can check if the device supports it with :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice.isFormatSupported`. For instance:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py
    :lines: 151-170

The set of available devices can be retrieved from the :sip:ref:`~PyQt6.QtMultimedia.QMediaDevices` class.

For instance:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py
    :lines: 208-210

In this code sample, we loop through all devices that are able to output sound, i.e., play an audio stream in a supported format. For each device we find, we simply print the deviceName().

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudioSink`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSource`, :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat`.
