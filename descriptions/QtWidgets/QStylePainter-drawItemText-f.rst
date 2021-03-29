.. sip:method-description::
    :status: todo
    :pysig: fdb09dee0b796cdd6e0c9520da876a3c
    :realsig: (const QRect&,int,const QPalette&,bool,const QString&,QPalette::ColorRole)
    :digest: 711846878af79e095baa04857c4aab51

Draws the *text* in rectangle *rect* and palette *pal*. The text is aligned and wrapped according to *flags*.

The pen color is specified with *textRole*. The *enabled* bool indicates whether or not the item is enabled; when reimplementing this bool should influence how the item is drawn.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyle.drawItemText`, Qt::Alignment.
