.. sip:method-description::
    :status: todo
    :pysig: 85af3f41efc41da1204b00787996bd1e
    :realsig: (const QPoint&,QAction*)
    :digest: 821a68699bcbeb51198fbc2308e41801

Displays the menu so that the action *atAction* will be at the specified *global* position *p*. To translate a widget's local coordinates into global coordinates, use :sip:ref:`~PyQt6.QtWidgets.QWidget.mapToGlobal`.

When positioning a menu with :sip:ref:`~PyQt6.QtWidgets.QMenu.exec` or , bear in mind that you cannot rely on the menu's current size(). For performance reasons, the menu adapts its size only when necessary, so in many cases, the size before and after the show is different. Instead, use :sip:ref:`~PyQt6.QtWidgets.QMenu.sizeHint` which calculates the proper size depending on the menu's current contents.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.mapToGlobal`, :sip:ref:`~PyQt6.QtWidgets.QMenu.exec`.
