.. sip:method-description::
    :status: todo
    :pysig: c381db626f71aea012c0e3288bf7b829
    :realsig: (QLayout*,int,int,Qt::Alignment)
    :digest: 6532506b6f76a59d272b7202a28f014b

Places the *layout* at position (\ *row*, *column*) in the grid. The top-left position is (0, 0).

The alignment is specified by *alignment*. The default alignment is 0, which means that the widget fills the entire cell.

A non-zero alignment indicates that the layout should not grow to fill the available space but should be sized according to :sip:ref:`~PyQt6.QtWidgets.QGridLayout.sizeHint`.

*layout* becomes a child of the grid layout.
