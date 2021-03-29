.. sip:method-description::
    :status: todo
    :pysig: 64f9a31892f540c568d5dff157bd70de
    :realsig: (QQmlEngine*,QWidget*)
    :digest: 29274148089b930ff7607c2e656e9271

Constructs a :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` with the given QML *engine* and *parent*.

Note: In this case, the :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget` does not own the given *engine* object; it is the caller's responsibility to destroy the engine. If the *engine* is deleted before the view, :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.status` will return :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.Status.Error`.

.. seealso:: :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.Status.Status`, :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.status`, :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget.errors`.
