.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 7c3e416d34ed7297215cc0432dae02cd

This function notifies the effect framework when the effect's bounding rectangle has changed. As a custom effect author, you must call this function whenever you change any parameters that will cause the virtual :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.boundingRectFor` function to return a different value.

This function will call :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.update` if this is necessary.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.boundingRectFor`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.boundingRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsEffect.sourceBoundingRect`.
