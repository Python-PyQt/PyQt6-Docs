.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const char*)
    :digest: 85fcb3687fb8f93b6d462787b8f7d7b3

Returns whether the environment variable *varName* is set.

Equivalent to

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 741-741

except that it's potentially much faster, and can't throw exceptions.

.. seealso:: qgetenv(), :sip:ref:`~PyQt6.QtCore.qEnvironmentVariable`, :sip:ref:`~PyQt6.QtCore.qEnvironmentVariableIsEmpty`.
