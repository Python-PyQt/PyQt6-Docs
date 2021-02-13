.. sip:method-description::
    :status: todo
    :pysig: b9fbe4eb00606498ddee228d4c1d581b
    :realsig: (int,int,const QRect&,QRegion*)
    :digest: 0c06324f2b9e59b5837c50f25dd1c45c

Scrolls the area *rect* of this pixmap by (\ *dx*, *dy*). The exposed region is left unchanged. You can optionally pass a pointer to an empty :sip:ref:`~PyQt6.QtGui.QRegion` to get the region that is *exposed* by the scroll operation.

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qpixmap.py
    :lines: 70-72

You cannot scroll while there is an active painter on the pixmap.

.. seealso:: QWidget::scroll()QGraphicsItem::scroll().
