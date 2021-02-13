.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: 7a2ab878d008a755cdecc24e8389d277

Sets the progress bar's minimum and maximum values to *minimum* and *maximum* respectively.

If *maximum* is smaller than *minimum*, *minimum* becomes the only legal value.

If the current value falls outside the new range, the progress bar is reset with :sip:ref:`~PyQt6.QtWidgets.QProgressBar.reset`.

The :sip:ref:`~PyQt6.QtWidgets.QProgressBar` can be set to undetermined state by using (0, 0).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QProgressBar.minimum`, :sip:ref:`~PyQt6.QtWidgets.QProgressBar.maximum`.
