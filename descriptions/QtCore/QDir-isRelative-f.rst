.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: c3128d7f10808f95be961c1f634bf230

Returns ``true`` if the directory path is relative; otherwise returns false. (Under Unix a path is relative if it does not start with a "/").

**Note:** Paths starting with a colon (\ *:*) are always considered absolute, as they denote a :sip:ref:`~PyQt6.QtCore.QResource`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.makeAbsolute`, :sip:ref:`~PyQt6.QtCore.QDir.isAbsolute`, :sip:ref:`~PyQt6.QtCore.QDir.isAbsolutePath`, :sip:ref:`~PyQt6.QtCore.QDir.cleanPath`.
