.. sip:method-description::
    :status: todo
    :pysig: ae37ca4aff0e0113e02871bc3305e3b3
    :realsig: (const QElapsedTimer&) const
    :digest: 0ee05299f835c45c398f255628645707

Returns the number of seconds between this :sip:ref:`~PyQt6.QtCore.QElapsedTimer` and *other*. If *other* was started before this object, the returned value will be negative. If it was started later, the returned value will be positive.

Calling this function on or with a :sip:ref:`~PyQt6.QtCore.QElapsedTimer` that is invalid results in undefined behavior.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QElapsedTimer.msecsTo`, :sip:ref:`~PyQt6.QtCore.QElapsedTimer.elapsed`.
