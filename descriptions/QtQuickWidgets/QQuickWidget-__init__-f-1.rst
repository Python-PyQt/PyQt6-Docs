.. sip:method-description::
    :status: todo
    :pysig: 64f9a31892f540c568d5dff157bd70de
    :realsig: (QQmlEngine*,QWidget*)
    :digest: cb399f9a28d44d65842e3ce7fc6b82ea

Constructs a :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` with the given QML *engine* as a child of *parent*.

**Note:** The :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` does not take ownership of the given *engine* object; it is the caller's responsibility to destroy the engine. If the *engine* is deleted before the view, :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.status` will return :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.Status.Error`.
