.. sip:method-description::
    :status: todo
    :pysig: 0754bfb51e695db3eb6df0f89fe4dbf0
    :realsig: (int)
    :digest: 3f55db313ad26b2df505d494d1cbdd1d

Returns a default channel configuration for *channelCount*.

Default configurations are defined for up to 8 channels, and correspond to standard Mono, Stereo and Surround configurations. For higher channel counts, this simply uses the first *channelCount* audio channels defined in :sip:ref:`~PyQt6.QtMultimedia.QAudioFormat.AudioChannelPosition`.
