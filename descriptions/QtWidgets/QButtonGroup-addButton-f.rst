.. sip:method-description::
    :status: todo
    :pysig: 19dd2267f659977a0b460ec7ebadc6fd
    :realsig: (QAbstractButton*,int)
    :digest: b0dea7e1507a7cc665a318839a402922

Adds the given *button* to the button group. If *id* is -1, an id will be assigned to the button. Automatically assigned ids are guaranteed to be negative, starting with -2. If you are assigning your own ids, use positive values to avoid conflicts.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QButtonGroup.removeButton`, :sip:ref:`~PyQt6.QtWidgets.QButtonGroup.buttons`.
