.. sip:enum-description::
    :status: todo
    :digest: 01dd0fc09e816935a1630b8085c868cb

This enum is used to specify whether a Node will accept a url with an unrecognized schema for the hostUrl. By default only urls with known schemas are accepted, but using ``AllowExternalRegistration`` will enable the `Registry <https://doc.qt.io/qt-6/qtremoteobjects-registry.html#registry>`_ to pass your external (to QtRO) url to client Nodes.

.. seealso:: :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost`.
