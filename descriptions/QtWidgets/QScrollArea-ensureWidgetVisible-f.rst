.. sip:method-description::
    :status: todo
    :pysig: 6f7bfeb9a0f1f00a039b86b30c30bc00
    :realsig: (QWidget*,int,int)
    :digest: 4407ce630373113dcd3611befb53c686

Scrolls the contents of the scroll area so that the *childWidget* of :sip:ref:`~PyQt6.QtWidgets.QScrollArea.widget` is visible inside the viewport with margins specified in pixels by *xmargin* and *ymargin*. If the specified point cannot be reached, the contents are scrolled to the nearest valid position. The default value for both margins is 50 pixels.
