.. sip:method-description::
    :status: todo
    :pysig: b1b9bd588bc5178793bc3d194b600fda
    :realsig: (Qt::WindowStates)
    :digest: babec253a1a19f052922434375440450

The function sets the window state on child widgets similar to :sip:ref:`~PyQt6.QtWidgets.QWidget.setWindowState`. The difference is that the window state changed event has the isOverride() flag set. It exists mainly to keep QWorkspace working.
