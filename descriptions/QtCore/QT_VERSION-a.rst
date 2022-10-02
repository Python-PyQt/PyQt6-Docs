.. sip:attribute-description::
    :status: todo
    :digest: 604078026537287e335936014b9479f8

This macro expands to a numeric value of the same form as QT_VERSION_CHECK() constructs, that specifies the version of Qt with which code using it is compiled. For example, if you compile your application with Qt 6.1.2, the QT_VERSION macro will expand to ``0x060102``, the same as ``QT_VERSION_CHECK(6, 1, 2)``. Note that this need not agree with the version the application will find itself using at *runtime*.

You can use QT_VERSION to select the latest Qt features where available while falling back to older implementations otherwise. Using QT_VERSION_CHECK() for the value to compare with is recommended.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 208-213

.. seealso:: :sip:ref:`~PyQt6.QtCore.QT_VERSION_STR`, QT_VERSION_CHECK(), :sip:ref:`~PyQt6.QtCore.qVersion`.
