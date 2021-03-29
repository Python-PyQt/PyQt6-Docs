.. sip:method-description::
    :status: todo
    :pysig: e6b4bb609965cdae52b42e37d1e795ea
    :realsig: (QAction*,const QIcon&,const QString&)
    :digest: 2832d98c166f8bbde0600b70fcc0fe5c

This convenience function creates a new title action, i.e. an action with :sip:ref:`~PyQt6.QtGui.QAction.isSeparator` returning true but also having *text* and *icon* hints. The function inserts the newly created action into this menu's list of actions before action *before* and returns it.

The rendering of the hints is style and platform dependent. Widget styles can use the text and icon information in the rendering for sections, or can choose to ignore them and render sections like simple separators.

:sip:ref:`~PyQt6.QtWidgets.QMenu` takes ownership of the returned :sip:ref:`~PyQt6.QtGui.QAction`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.insertAction`, :sip:ref:`~PyQt6.QtWidgets.QMenu.addSection`.
