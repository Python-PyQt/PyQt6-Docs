.. sip:method-description::
    :status: todo
    :pysig: 44f1458879e73bc3603faa0801291cfa
    :realsig: (QQmlEngine*,QWindow*)
    :digest: 470a85d2aff546a0cec28996af86b1d2

Constructs a :sip:ref:`~PyQt6.QtQuick.QQuickView` with the given QML *engine* and *parent*.

Note: In this case, the :sip:ref:`~PyQt6.QtQuick.QQuickView` does not own the given *engine* object; it is the caller's responsibility to destroy the engine. If the *engine* is deleted before the view, :sip:ref:`~PyQt6.QtQuick.QQuickView.status` will return :sip:ref:`~PyQt6.QtQuick.QQuickView.Status.Error`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickView.Status.Status`, :sip:ref:`~PyQt6.QtQuick.QQuickView.status`, :sip:ref:`~PyQt6.QtQuick.QQuickView.errors`.
