.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: be17f0250ed22f964bca846c4f88c20e

Terminates the map started by either overload of :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startMap` and returns true if the correct number of elements was added to the array. This function must be called for every :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startMap` used.

A return of false indicates error in the application and an unrecoverable error in this stream. :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` also writes a warning using :sip:ref:`~PyQt6.QtCore.qWarning` if that happens.

Calling this function when the current container is not a map is also an error, though :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` cannot currently detect this condition.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startMap`, startMap(quint64), :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.endArray`.
