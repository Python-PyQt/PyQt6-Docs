.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: b7dee7aa35ebd0bd434afe400475074a

Sets the stretch factor of column *column* to *stretch*. The first column is number 0.

The stretch factor is relative to the other columns in this grid. Columns with a higher stretch factor take more of the available space.

The default stretch factor is 0. If the stretch factor is 0 and no other column in this table can grow at all, the column may still grow.

An alternative approach is to add spacing using :sip:ref:`~PyQt6.QtWidgets.QGridLayout.addItem` with a :sip:ref:`~PyQt6.QtWidgets.QSpacerItem`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGridLayout.columnStretch`, :sip:ref:`~PyQt6.QtWidgets.QGridLayout.setRowStretch`.
