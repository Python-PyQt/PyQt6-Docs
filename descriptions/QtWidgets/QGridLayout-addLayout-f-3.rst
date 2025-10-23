.. sip:method-description::
    :status: todo
    :pysig: 50f41ce41f125d9ca5694d7186ec5fde
    :realsig: (QLayout*,int,int,int,int,Qt::Alignment)
    :digest: 4447bdb273416c5f95a5237938a1279a

This version adds the layout *layout* to the cell grid, spanning multiple rows/columns. The cell will start at *row*, *column* spanning *rowSpan* rows and *columnSpan* columns.

If *rowSpan* and/or *columnSpan* is -1, then the layout will extend to the bottom and/or right edge, respectively.
