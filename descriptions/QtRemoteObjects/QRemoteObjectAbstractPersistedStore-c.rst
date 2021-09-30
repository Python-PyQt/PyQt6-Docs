.. sip:class-description::
    :status: todo
    :brief: A class which provides the methods for setting PROP values of a replica to value they had the last time the replica was used
    :digest: 921f43dd51dfae59711176b03943c887

A class which provides the methods for setting PROP values of a replica to value they had the last time the replica was used.

This can be used to provide a "reasonable" value to be displayed until the connection to the source is established and current values are available.

This class must be overridden to provide an implementation for saving (\ :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectAbstractPersistedStore.saveProperties`) and restoring (\ :sip:ref:`~PyQt6.QtRemoteObjects.QRemoteObjectAbstractPersistedStore.restoreProperties`) PROP values. The derived type can then be set for a node, and any replica acquired from that node will then automatically store PERSISTED properties when the replica destructor is called, and retrieve the values when the replica is instantiated.
