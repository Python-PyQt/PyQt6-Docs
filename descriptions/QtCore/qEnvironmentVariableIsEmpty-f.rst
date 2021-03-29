.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const char*)
    :digest: 1535c65d98b2a0ba9a2c0ee69c31e9a7

Returns whether the environment variable *varName* is empty.

Equivalent to

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 733-733

except that it's potentially much faster, and can't throw exceptions.

.. seealso:: qgetenv(), :sip:ref:`~PyQt6.QtCore.qEnvironmentVariable`, :sip:ref:`~PyQt6.QtCore.qEnvironmentVariableIsSet`.
