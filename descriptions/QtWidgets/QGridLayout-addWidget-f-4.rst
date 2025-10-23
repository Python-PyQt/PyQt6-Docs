.. sip:method-description::
    :status: todo
    :pysig: 206acfb8cf0ff1a419c5539c71414cef
    :realsig: (QWidget*,int,int,int,int,Qt::Alignment)
    :digest: 5834e4f69c9fd97a03a7d8f887e564af

This version adds the given *widget* to the cell grid, spanning multiple rows/columns. The cell will start at *fromRow*, *fromColumn* spanning *rowSpan* rows and *columnSpan* columns. The *widget* will have the given *alignment*.

If *rowSpan* and/or *columnSpan* is -1, then the widget will extend to the bottom and/or right edge, respectively.
