.. sip:class-description::
    :status: todo
    :brief: Exception-safe wrapper around QObject::blockSignals()
    :digest: b840cd72ce0a01fb03c0b2a2d3a4cf7f

Exception-safe wrapper around :sip:ref:`~PyQt6.QtCore.QObject.blockSignals`.

:sip:ref:`~PyQt6.QtCore.QSignalBlocker` can be used wherever you would otherwise use a pair of calls to :sip:ref:`~PyQt6.QtCore.QObject.blockSignals`. It blocks signals in its constructor and in the destructor it resets the state to what it was before the constructor ran.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 553-556

is thus equivalent to

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 560-562

except the code using :sip:ref:`~PyQt6.QtCore.QSignalBlocker` is safe in the face of exceptions.

.. seealso:: QMutexLocker, :sip:ref:`~PyQt6.QtCore.QEventLoopLocker`.
