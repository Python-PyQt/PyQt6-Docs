.. sip:method-description::
    :status: todo
    :pysig: 57c31379e44a8005d567ac33ae06f4ab
    :realsig: (int,int,int,int)
    :digest: eb611d3afda5524b4ffae498aea2bfe9

Constructs a time with hour *h*, minute *m*, seconds *s* and milliseconds *ms*.

*h* must be in the range 0 to 23, *m* and *s* must be in the range 0 to 59, and *ms* must be in the range 0 to 999.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTime.isValid`.
