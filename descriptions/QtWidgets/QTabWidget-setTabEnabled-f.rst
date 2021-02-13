.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (int,bool)
    :digest: a66c52e9b23ae1090dd34c069d18d391

If *enable* is true, the page at position *index* is enabled; otherwise the page at position *index* is disabled. The page's tab is redrawn appropriately.

:sip:ref:`~PyQt6.QtWidgets.QTabWidget` uses :sip:ref:`~PyQt6.QtWidgets.QWidget.setEnabled` internally, rather than keeping a separate flag.

Note that even a disabled tab/page may be visible. If the page is visible already, :sip:ref:`~PyQt6.QtWidgets.QTabWidget` will not hide it; if all the pages are disabled, :sip:ref:`~PyQt6.QtWidgets.QTabWidget` will show one of them.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTabWidget.isTabEnabled`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setEnabled`.
