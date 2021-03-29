.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: efc06df33b7034f65b9a6d03df36cc4f

Returns ``true`` if the URL is relative; otherwise returns ``false``. A URL is relative reference if its scheme is undefined; this function is therefore equivalent to calling :sip:ref:`~PyQt6.QtCore.QUrl.scheme`.\ :sip:ref:`~PyQt6.QtCore.QUrl.isEmpty`.

Relative references are defined in RFC 3986 section 4.2.

.. seealso:: :ref:`qurl-relative-urls-vs-relative-paths`.
