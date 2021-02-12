.. sip:method-description::
    :status: todo
    :pysig: 9785bedab2880ecc1650a8a706cb4984
    :realsig: (double,double)
    :digest: f3ea18b5f1bbda75a140cb450c64e9c8

Compares the floating point value *p1* and *p2* and returns ``true`` if they are considered equal, otherwise ``false``.

Note that comparing values where either *p1* or *p2* is 0.0 will not work, nor does comparing values where one of the values is NaN or infinity. If one of the values is always 0.0, use qFuzzyIsNull instead. If one of the values is likely to be 0.0, one solution is to add 1.0 to both values.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qglobal.py
    :lines: 623-626

The two numbers are compared in a relative way, where the exactness is stronger the smaller the numbers are.
