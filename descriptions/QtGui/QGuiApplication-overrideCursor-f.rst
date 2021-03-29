.. sip:method-description::
    :status: todo
    :pysig: ec290be3758758056f5f01855c8df70a
    :realsig: ()
    :digest: 4727eb78907e4d9cf875b6e60e87ef6f

Returns the active application override cursor.

This function returns ``nullptr`` if no application cursor has been defined (i.e. the internal cursor stack is empty).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.setOverrideCursor`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.restoreOverrideCursor`.
