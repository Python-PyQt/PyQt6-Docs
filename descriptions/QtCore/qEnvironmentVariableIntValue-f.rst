.. sip:method-description::
    :status: todo
    :pysig: 01a14469e152a0ff2a4996affe14e914
    :realsig: (const char*,bool*)
    :digest: 0184728ff94887752b19371e7d9cd9a6

Returns the numerical value of the environment variable *varName*. If *ok* is not null, sets ``\*ok`` to ``true`` or ``false`` depending on the success of the conversion.

Equivalent to

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 737-737

except that it's much faster, and can't throw exceptions.

**Note:** there's a limit on the length of the value, which is sufficient for all valid values of int, not counting leading zeroes or spaces. Values that are too long will either be truncated or this function will set *ok* to ``false``.

.. seealso:: qgetenv(), :sip:ref:`~PyQt6.QtCore.qEnvironmentVariable`, :sip:ref:`~PyQt6.QtCore.qEnvironmentVariableIsSet`.
