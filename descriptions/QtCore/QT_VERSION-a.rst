.. sip:attribute-description::
    :status: todo
    :digest: 3cf0d70834a539fbbb1984e2d311be26

This macro expands a numeric value of the form 0xMMNNPP (MM = major, NN = minor, PP = patch) that specifies Qt's version number. For example, if you compile your application against Qt 4.1.2, the  macro will expand to 0x040102.

You can use  to use the latest Qt features where available.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 208-213

.. seealso:: :sip:ref:`~PyQt6.QtCore.QT_VERSION_STR`, :sip:ref:`~PyQt6.QtCore.qVersion`.
