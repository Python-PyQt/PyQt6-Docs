.. sip:method-description::
    :status: todo
    :pysig: b9bc79a70cead5893ff4ccaf27c0cf7e
    :realsig: (const QByteArray&)
    :digest: 66a58db50f10bbe68aa30a7603409017

Restores the splitter's layout to the *state* specified. Returns ``true`` if the state is restored; otherwise returns ``false``.

Typically this is used in conjunction with :sip:ref:`~PyQt6.QtCore.QSettings` to restore the size from a past session. Here is an example:

Restore the splitter's state:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-splitter-splitter.py
    :lines: 84-85

A failure to restore the splitter's layout may result from either invalid or out-of-date data in the supplied byte array.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitter.saveState`.
