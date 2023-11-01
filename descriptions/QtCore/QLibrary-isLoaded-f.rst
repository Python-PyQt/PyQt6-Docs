.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 8943231d9e74bbcae2484c46fcaa6874

Returns ``true`` if :sip:ref:`~PyQt6.QtCore.QLibrary.load` succeeded; otherwise returns ``false``.

**Note:** Prior to Qt 6.6, this function would return ``true`` even without a call to :sip:ref:`~PyQt6.QtCore.QLibrary.load` if another :sip:ref:`~PyQt6.QtCore.QLibrary` object on the same library had caused it to be loaded.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLibrary.load`.
