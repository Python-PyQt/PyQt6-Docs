.. sip:attribute-description::
    :status: todo
    :digest: c0a92342343f4641db55be338799db5e

This macro expands to a numeric value of the same form as QT_VERSION_CHECK() constructs, that specifies the version of Qt with which code using it is compiled. For example, if you compile your application with Qt 6.1.2, the  macro will expand to ``0x060102``, the same as ``QT_VERSION_CHECK(6, 1, 2)``. Note that this need not agree with the version the application will find itself using at *runtime*.

You can use  to select the latest Qt features where available while falling back to older implementations otherwise. Using QT_VERSION_CHECK() for the value to compare with is recommended.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 208-213

.. seealso:: :sip:ref:`~PyQt6.QtCore.QT_VERSION_STR`, QT_VERSION_CHECK(), :sip:ref:`~PyQt6.QtCore.qVersion`.
