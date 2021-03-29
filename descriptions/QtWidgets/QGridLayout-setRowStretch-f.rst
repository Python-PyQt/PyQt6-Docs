.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: fa25642cff382d290e2ad305498c4c19

Sets the stretch factor of row *row* to *stretch*. The first row is number 0.

The stretch factor is relative to the other rows in this grid. Rows with a higher stretch factor take more of the available space.

The default stretch factor is 0. If the stretch factor is 0 and no other row in this table can grow at all, the row may still grow.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGridLayout.rowStretch`, :sip:ref:`~PyQt6.QtWidgets.QGridLayout.setRowMinimumHeight`, :sip:ref:`~PyQt6.QtWidgets.QGridLayout.setColumnStretch`.
