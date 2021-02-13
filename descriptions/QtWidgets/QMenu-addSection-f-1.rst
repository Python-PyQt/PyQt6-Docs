.. sip:method-description::
    :status: todo
    :pysig: 65b843fe7974663e1081ec586fd7da95
    :realsig: (const QIcon&,const QString&)
    :digest: b1f15b1ead91ce6abbabf6a0f21cd877

This convenience function creates a new section action, i.e. an action with :sip:ref:`~PyQt6.QtGui.QAction.isSeparator` returning true but also having *text* and *icon* hints, and adds the new action to this menu's list of actions. It returns the newly created action.

The rendering of the hints is style and platform dependent. Widget styles can use the text and icon information in the rendering for sections, or can choose to ignore them and render sections like simple separators.

:sip:ref:`~PyQt6.QtWidgets.QMenu` takes ownership of the returned :sip:ref:`~PyQt6.QtGui.QAction`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.addAction`.
