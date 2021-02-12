.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 692dd74c7687c0d4f297e9bd6808e0ff

Sets the :sip:ref:`~PyQt6.QtCore.QTemporaryFile` into auto-remove mode if *b* is ``true``.

Auto-remove is on by default.

If you set this property to ``false``, ensure the application provides a way to remove the file once it is no longer needed, including passing the responsibility on to another process. Always use the :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileName` function to obtain the name and never try to guess the name that :sip:ref:`~PyQt6.QtCore.QTemporaryFile` has generated.

On some systems, if :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileName` is not called before closing the file, the temporary file may be removed regardless of the state of this property. This behavior should not be relied upon, so application code should either call :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileName` or leave the auto removal functionality enabled.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.autoRemove`, remove().
