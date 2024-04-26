.. sip:method-description::
    :status: todo
    :pysig: 03569a4c2e2fbf5278fd93ad0e7cd975
    :realsig: (QTextToSpeech::BoundaryHint)
    :digest: 442e33bbf9e55769e86d6494eba91626

Stops the current reading at *boundaryHint*, and clears the queue of pending texts.

The reading cannot be resumed. Whether the *boundaryHint* is respected depends on the engine.

.. seealso:: :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.say`, :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.enqueue`, :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.pause`.
