.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 372c2d180890da74b6fb826eb82c63ee

Returns ``true`` if the rectangle is empty, otherwise returns ``false``.

An empty rectangle has a :sip:ref:`~PyQt6.QtCore.QRect.left` > :sip:ref:`~PyQt6.QtCore.QRect.right` or :sip:ref:`~PyQt6.QtCore.QRect.top` > :sip:ref:`~PyQt6.QtCore.QRect.bottom`. An empty rectangle is not valid (i.e.,  == !\ :sip:ref:`~PyQt6.QtCore.QRect.isValid`).

Use the :sip:ref:`~PyQt6.QtCore.QRect.normalized` function to retrieve a rectangle where the corners are swapped.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRect.isNull`, :sip:ref:`~PyQt6.QtCore.QRect.isValid`, :sip:ref:`~PyQt6.QtCore.QRect.normalized`.
