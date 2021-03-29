.. sip:method-description::
    :status: todo
    :pysig: 185bdabd93fcd409fe17d8923ea1a313
    :realsig: (const QObject*,const QMetaMethod&)
    :digest: 1f9fafd95fd5599cde4bfdb1be9214d2

Constructs a new :sip:ref:`~PyQt6.QtTest.QSignalSpy` that listens for emissions of the *signal* from the :sip:ref:`~PyQt6.QtCore.QObject` *obj*. If :sip:ref:`~PyQt6.QtTest.QSignalSpy` is not able to listen for a valid signal (for example, because *obj* is ``nullptr`` or *signal* does not denote a valid signal of *obj*), an explanatory warning message will be output using :sip:ref:`~PyQt6.QtCore.qWarning` and subsequent calls to ``isValid()`` will return false.

This constructor is convenient to use when Qt's meta-object system is heavily used in a test.

Basic usage example:

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-doc_src_qsignalspy.py
    :lines: 104-111

Imagine we need to check whether all properties of the :sip:ref:`~PyQt6.QtGui.QWindow` class that represent minimum and maximum dimensions are properly writable. The following example demonstrates one of the approaches:

.. literalinclude:: ../../../snippets/qtbase-src-testlib-doc-snippets-code-doc_src_qsignalspy.py
    :lines: 115-149
