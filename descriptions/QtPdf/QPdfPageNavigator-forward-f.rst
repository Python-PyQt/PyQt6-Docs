.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: aa6df1ca83a3c14e1a24d2de766733fe

Goes back to the page, location and zoom level that was being viewed before :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator.back` was called, and then emits the :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator.jumped` signal.

If a new destination was pushed since the last time :sip:ref:`~PyQt6.QtPdf.QPdfPageNavigator.back` was called, the forward() function does nothing, because there is a branch in the timeline which causes the "future" to be lost.
