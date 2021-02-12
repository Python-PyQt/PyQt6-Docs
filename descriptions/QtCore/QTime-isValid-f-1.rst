.. sip:method-description::
    :status: todo
    :pysig: 55bb8d9b829998213fb20e956458ec3d
    :realsig: (int,int,int,int)
    :digest: 47efe3a1713e09ea4efaab826a98327c

This is an overloaded function.

Returns ``true`` if the specified time is valid; otherwise returns false.

The time is valid if *h* is in the range 0 to 23, *m* and *s* are in the range 0 to 59, and *ms* is in the range 0 to 999.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_time_qdatetime.py
    :lines: 118-119
