.. sip:method-description::
    :status: todo
    :pysig: 9da0344d7c88a9bd28d7e8bd0869a63c
    :realsig: (QAction*,const QString&)
    :digest: d008a383e3649977dd4ae860cf0b1b5d

This convenience function creates a new title action, i.e. an action with :sip:ref:`~PyQt6.QtGui.QAction.isSeparator` returning true but also having *text* hint. The function inserts the newly created action into this menu's list of actions before action *before* and returns it.

The rendering of the hint is style and platform dependent. Widget styles can use the text information in the rendering for sections, or can choose to ignore it and render sections like simple separators.

:sip:ref:`~PyQt6.QtWidgets.QMenu` takes ownership of the returned :sip:ref:`~PyQt6.QtGui.QAction`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.insertAction`, :sip:ref:`~PyQt6.QtWidgets.QMenu.addSection`.
