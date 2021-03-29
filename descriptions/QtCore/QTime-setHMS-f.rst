.. sip:method-description::
    :status: todo
    :pysig: 1485beeb4c487fcde616ad689705aeda
    :realsig: (int,int,int,int)
    :digest: 953212dbdaabde9a78d149cc9bda9292

Sets the time to hour *h*, minute *m*, seconds *s* and milliseconds *ms*.

*h* must be in the range 0 to 23, *m* and *s* must be in the range 0 to 59, and *ms* must be in the range 0 to 999. Returns ``true`` if the set time is valid; otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTime.isValid`.
