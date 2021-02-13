.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: c84456ea6cbf96641b4b2759344dc6ef

Interrupts or re-enables JavaScript execution.

If *interrupted* is ``true``, any JavaScript executed by this engine immediately aborts and returns an error object until this function is called again with a value of ``false`` for *interrupted*.

This function is thread safe. You may call it from a different thread in order to interrupt, for example, an infinite loop in JavaScript.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSEngine.isInterrupted`.
