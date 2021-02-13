.. sip:method-description::
    :status: todo
    :pysig: a8f391c4169bdf9b8c5cd82cf6f14fb7
    :realsig: (const QObject*,const char*)
    :digest: 34ab171c9d6b2405ec9a7f300feece10

Constructs a new :sip:ref:`~PyQt6.QtTest.QSignalSpy` that listens for emissions of the *signal* from the :sip:ref:`~PyQt6.QtCore.QObject` *object*. If :sip:ref:`~PyQt6.QtTest.QSignalSpy` is not able to listen for a valid signal (for example, because *object* is ``nullptr`` or *signal* does not denote a valid signal of *object*), an explanatory warning message will be output using :sip:ref:`~PyQt6.QtCore.qWarning` and subsequent calls to ``isValid()`` will return false.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-doc_src_qsignalspy.py
    :lines: 92-92
