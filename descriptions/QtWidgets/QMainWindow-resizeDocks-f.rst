.. sip:method-description::
    :status: todo
    :pysig: 7a3840e67513333f6a2a8d575b30e835
    :realsig: (const QList<QDockWidget*>&,const QList<int>&,Qt::Orientation)
    :digest: 811783281be4fb44da3d4a3a47a3d6b5

Resizes the dock widgets in the list *docks* to the corresponding size in pixels from the list *sizes*. If *orientation* is :sip:ref:`~PyQt6.QtCore.Qt.Orientation.Horizontal`, adjusts the width, otherwise adjusts the height of the dock widgets. The sizes will be adjusted such that the maximum and the minimum sizes are respected and the :sip:ref:`~PyQt6.QtWidgets.QMainWindow` itself will not be resized. Any additional/missing space is distributed amongst the widgets according to the relative weight of the sizes.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_widgets_widgets_qmainwindow.py
    :lines: 59-59

If the blue and the yellow widget are nested on the same level they will be resized such that the yellowWidget is twice as big as the blueWidget

If some widgets are grouped in tabs, only one widget per group should be specified. Widgets not in the list might be changed to respect the constraints.
