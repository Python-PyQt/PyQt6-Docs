.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qsizetype)
    :digest: 04794c08d7617661f51fffc8945fc5a4

This signal gets emitted just before the engine starts to synthesize the speech audio for *id*. The *id* is the value returned by a call to :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.enqueue`, Applications can use this signal to make last-minute changes to :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.voice` attributes, or to track the process of text enqueued via :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.enqueue`.

.. seealso:: :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.enqueue`, synthesize(), :sip:ref:`~PyQt6.QtTextToSpeech.QTextToSpeech.voice`.
