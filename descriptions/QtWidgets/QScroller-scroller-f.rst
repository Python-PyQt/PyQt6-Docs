.. sip:method-description::
    :status: todo
    :pysig: 94609e1e31c8287aad7442e1775fdd9e
    :realsig: (QObject*)
    :digest: 4b71fffe2c030916e53163af8182774d

Returns the scroller for the given *target*. As long as the object exists this function will always return the same :sip:ref:`~PyQt6.QtWidgets.QScroller` instance. If no :sip:ref:`~PyQt6.QtWidgets.QScroller` exists for the *target*, one will implicitly be created. At no point more than one :sip:ref:`~PyQt6.QtWidgets.QScroller` will be active on an object.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QScroller.hasScroller`, :sip:ref:`~PyQt6.QtWidgets.QScroller.target`.
