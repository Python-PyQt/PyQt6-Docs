.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 8f45f61989d445c6f9162b1d3f25588e

Returns ``true`` if there is no more data to be read from the :sip:ref:`~PyQt6.QtCore.QTextStream`; otherwise returns ``false``. This is similar to, but not the same as calling :sip:ref:`~PyQt6.QtCore.QIODevice.atEnd`, as :sip:ref:`~PyQt6.QtCore.QTextStream` also takes into account its internal Unicode buffer.
