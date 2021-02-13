.. sip:method-description::
    :status: todo
    :pysig: 21270d7746ad5b3b259692ac37694dd4
    :realsig: (QWidget*,int,int,int,int,Qt::Alignment)
    :digest: 1c8a7aa66db3da79c8501fbca4b1f086

This is an overloaded function.

This version adds the given *widget* to the cell grid, spanning multiple rows/columns. The cell will start at *fromRow*, *fromColumn* spanning *rowSpan* rows and *columnSpan* columns. The *widget* will have the given *alignment*.

If *rowSpan* and/or *columnSpan* is -1, then the widget will extend to the bottom and/or right edge, respectively.
