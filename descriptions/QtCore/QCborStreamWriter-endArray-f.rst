.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 433e8f21c5b06f41cf554a572a2eb89b

Terminates the array started by either overload of :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startArray` and returns true if the correct number of elements was added to the array. This function must be called for every :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startArray` used.

A return of false indicates error in the application and an unrecoverable error in this stream. :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` also writes a warning using :sip:ref:`~PyQt6.QtCore.qWarning` if that happens.

Calling this function when the current container is not an array is also an error, though :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` cannot currently detect this condition.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startArray`, startArray(quint64), :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.endMap`.
