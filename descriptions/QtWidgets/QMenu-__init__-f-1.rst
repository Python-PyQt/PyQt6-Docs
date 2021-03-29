.. sip:method-description::
    :status: todo
    :pysig: 06d15b181bc8d5276663d0a2f1f36f35
    :realsig: (const QString&,QWidget*)
    :digest: dcb264d2522edc52d3d124abe82a4d70

Constructs a menu with a *title* and a *parent*.

Although a popup menu is always a top-level widget, if a parent is passed the popup menu will be deleted when that parent is destroyed (as with any other :sip:ref:`~PyQt6.QtCore.QObject`).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMenu.title`.
