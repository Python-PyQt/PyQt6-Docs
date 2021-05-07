.. sip:method-description::
    :status: todo
    :pysig: dc5579a7aea5f8967486b7963f8a5116
    :realsig: (const QList<QDockWidget*>&,const QList<int>&,Qt::Orientation)
    :digest: a6b1e1c12693ae48039417d4985e234e

Resizes the dock widgets in the list *docks* to the corresponding size in pixels from the list *sizes*. If *orientation* is :sip:ref:`~PyQt6.QtCore.Qt.Orientation.Horizontal`, adjusts the width, otherwise adjusts the height of the dock widgets. The sizes will be adjusted such that the maximum and the minimum sizes are respected and the :sip:ref:`~PyQt6.QtWidgets.QMainWindow` itself will not be resized. Any additional/missing space is distributed amongst the widgets according to the relative weight of the sizes.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_widgets_widgets_qmainwindow.py
    :lines: 59-59

If the blue and the yellow widget are nested on the same level they will be resized such that the yellowWidget is twice as big as the blueWidget

If some widgets are grouped in tabs, only one widget per group should be specified. Widgets not in the list might be changed to repect the constraints.
