.. sip:method-description::
    :status: todo
    :pysig: e067a21998652d1aaf9dc7a94f484b86
    :realsig: () const
    :digest: 65bfe62458a9150528fcca1605e34d08

Returns an equivalent version number but with all trailing zeros removed.

To check if two numbers are equivalent, use normalized() on both version numbers before performing the compare.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qversionnumber-main.py
    :lines: 113-118
