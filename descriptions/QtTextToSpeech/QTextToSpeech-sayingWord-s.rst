.. sip:signal-description::
    :status: todo
    :pysig: 6e9bd0af09692292ea2d4e29fd37a92e
    :realsig: (const QString&, qsizetype, qsizetype, qsizetype)
    :digest: 542c5695c65dfd434ae954f42838e35c

This signal is emitted when the *word*, which is the slice of text indicated by *start* and *length* in the utterance *id*, gets played to the audio device.

**Note:** This signal requires that the engine has the :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.Capability.WordByWordProgress` capability.

.. seealso:: :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.Capability.Capability`, :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.say`.
