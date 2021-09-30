.. sip:method-description::
    :status: todo
    :pysig: 84c441882b1d3c5e4091f5738dde2a81
    :realsig: (float,QAudio::VolumeScale,QAudio::VolumeScale)
    :digest: e0efcd4a7305efcad083e919535b276d

Converts an audio *volume* *from* a volume scale *to* another, and returns the result.

Depending on the context, different scales are used to represent audio volume. All Qt Multimedia classes that have an audio volume use a linear scale, the reason is that the loudness of a speaker is controlled by modulating its voltage on a linear scale. The human ear on the other hand, perceives loudness in a logarithmic way. Using a logarithmic scale for volume controls is therefore appropriate in most applications. The decibel scale is logarithmic by nature and is commonly used to define sound levels, it is usually used for UI volume controls in professional audio applications. The cubic scale is a computationally cheap approximation of a logarithmic scale, it provides more control over lower volume levels.

The following example shows how to convert the volume value from a slider control before passing it to a :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer`. As a result, the perceived increase in volume is the same when increasing the volume slider from 20 to 30 as it is from 50 to 60:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-audio.py
    :lines: 246-255

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QAudio.VolumeScale.VolumeScale`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSink.setVolume`, :sip:ref:`~PyQt6.QtMultimedia.QAudioSource.setVolume`, :sip:ref:`~PyQt6.QtMultimedia.QSoundEffect.setVolume`.
