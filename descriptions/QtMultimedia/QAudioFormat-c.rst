.. sip:class-description::
    :status: todo
    :brief: Stores audio stream parameter information
    :digest: 28308193b3be28a1786a93efef341921

The :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat` class stores audio stream parameter information.

An audio format specifies how data in a raw audio stream is arranged. For example, how the stream is to be interpreted.

:sip:ref:`~PyQt6.QtMultimedia.QAudioFormat` contains parameters that specify how the audio sample data is arranged. These are the frequency, the number of channels, and the sample format. The following table describes these in more detail.

+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter          | Description                                                                                                                                                     |
+====================+=================================================================================================================================================================+
| Sample Rate        | Samples per second of audio data in Hertz.                                                                                                                      |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Number of channels | The number of audio channels (typically one for mono or two for stereo). These are the amount of consecutive samples that together form one frame in the stream |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Sample format      | The format of the audio samples in the stream                                                                                                                   |
+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

This class is used in conjunction with QAudioSource or QAudioSink to allow you to specify the parameters of the audio stream being read or written, or with QAudioBuffer when dealing with samples in memory.

You can obtain audio formats compatible with the audio device used through functions in QAudioDevice. This class also lets you query available parameter values for a device, so that you can set the parameters yourself. See the QAudioDevice class description for details. You need to know the format of the audio streams you wish to play or record.

Samples for all channels will be interleaved. One sample for each channel for the same instant in time is referred to as a frame in Qt Multimedia (and other places).
