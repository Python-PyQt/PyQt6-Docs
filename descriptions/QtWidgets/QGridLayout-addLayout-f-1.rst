.. sip:method-description::
    :status: todo
    :pysig: 410cfc1cb544e4d279c72ce1b582d39f
    :realsig: (QLayout*,int,int,int,int,Qt::Alignment)
    :digest: ad02ca3b569ecdd4995a3ecb66a3192d

This is an overloaded function.

This version adds the layout *layout* to the cell grid, spanning multiple rows/columns. The cell will start at *row*, *column* spanning *rowSpan* rows and *columnSpan* columns.

If *rowSpan* and/or *columnSpan* is -1, then the layout will extend to the bottom and/or right edge, respectively.
