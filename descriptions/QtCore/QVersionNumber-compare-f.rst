.. sip:method-description::
    :status: todo
    :pysig: ca53e2153b1dc5a23d59555893382fd8
    :realsig: (const QVersionNumber&,const QVersionNumber&)
    :digest: 91fa098307a3133d9b6818c80ba91d48

Compares *v1* with *v2* and returns an integer less than, equal to, or greater than zero, depending on whether *v1* is less than, equal to, or greater than *v2*, respectively.

Comparisons are performed by comparing the segments of *v1* and *v2* starting at index 0 and working towards the end of the longer list.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qversionnumber-main.py
    :lines: 76-78
