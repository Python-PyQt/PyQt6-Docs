.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: 92b92aa4f4af306c153c1cc4b58ca98e

Sets the progress dialog's minimum and maximum values to *minimum* and *maximum*, respectively.

If *maximum* is smaller than *minimum*, *minimum* becomes the only legal value.

If the current value falls outside the new range, the progress dialog is reset with :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.reset`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.minimum`, :sip:ref:`~PyQt6.QtWidgets.QProgressDialog.maximum`.
