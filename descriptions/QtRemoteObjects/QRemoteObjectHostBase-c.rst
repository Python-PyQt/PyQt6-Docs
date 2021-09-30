.. sip:class-description::
    :status: todo
    :brief: Base functionality common to Host and RegistryHost classes
    :digest: 795783d90af85359c9320dd42905b96c

The :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHostBase` class provides base functionality common to :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost` and :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistryHost` classes.

:sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHostBase` is a base class that cannot be instantiated directly. It provides the :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHostBase.enableRemoting` and :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHostBase.disableRemoting` functionality shared by all host nodes (\ :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectHost` and :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectRegistryHost`) as well as the logic required to expose `Source <https://doc.qt.io/qt-6/qtremoteobjects-source.html#source>`_ objects on the Remote Objects network.
