.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: a61c31053eb375132ed36d32f13543a9

Starts speaking the *text*.

This function starts sythesizing the speech asynchronously, and reads the text to the default audio output device.

.. literalinclude:: ../../../snippets/qtspeech-examples-speech-hello_speak-mainwindow.py
    :lines: 122-124

**Note:** All in-progress readings are stopped before beginning to read the recently synthesized text.

The current state is available using the :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.state` property, and is set to :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.State.Speaking` once the reading starts. When the reading is done, :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.state` will be set to :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.State.Ready`.

.. seealso:: :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.enqueue`, :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.stop`, :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.pause`, :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.resume`, synthesize().
