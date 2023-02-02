.. sip:method-description::
    :status: todo
    :pysig: 33a0aaa2712e8d6fce1fd50bb3422d8f
    :realsig: (const QImage&) const
    :digest: fd888dcbc7e7186c9d8c2b87a939b9c4

Creates a ``HICON`` equivalent of the :sip:ref:`~PyQt6.QtGui.QPixmap`, applying the mask *mask*.

If *mask* is not null, it needs to be of format :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_Mono`. Returns the ``HICON`` handle.

It is the caller's responsibility to free the ``HICON`` data after use.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.fromHICON`.
