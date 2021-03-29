.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: 46f8174b31e39216ee2d64f1a420526e

Saves the state of the splitter's layout.

Typically this is used in conjunction with :sip:ref:`~PyQt6.QtCore.QSettings` to remember the size for a future session. A version number is stored as part of the data. Here is an example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-splitter-splitter.py
    :lines: 76-77

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitter.restoreState`.
