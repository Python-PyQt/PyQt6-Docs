.. sip:method-description::
    :status: todo
    :pysig: 70ce07b225801abde2cb8f5bcae9bb3a
    :realsig: (const QString&)
    :digest: 9f5b2cc670eff42936ebd6ec96ad89fb

Adds *utterance* to the queue of texts to be spoken, and starts speaking. Returns the index of the text in the queue, or -1 in case of an error.

If the engine's :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.state` is currently ``Ready``, *utterance* will be spoken immediately. Otherwise, the engine will start to speak *utterance* once it has finished speaking the current text.

Each time the engine proceeds to the next text entry in the queue, the :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.aboutToSynthesize` signal gets emitted. This allows applications to keep track of the progress, and to make last-minute changes to voice attributes.

Calling :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.stop` clears the queue. To pause the engine at the end of a text, use the :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.BoundaryHint.Utterance` boundary hint.

.. seealso:: :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.say`, :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.stop`, :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.aboutToSynthesize`, synthesize().
