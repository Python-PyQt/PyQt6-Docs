.. sip:enum-description::
    :status: todo
    :digest: 737dea1ed782f7d6cbd31ad9575d43e8

This enum defines if and when :sip:ref:`~PyQt6.QtCore.QRangeModel` auto-connects changed-signals for properties to the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dataChanged` signal of the model. Only properties that match one of the :sip:ref:`~PyQt6.QtCore.QRangeModel.roleNames` are connected.

The memory overhead of making automatic connections can be substantial. A Full auto-connection does not require any book-keeping in addition to the connection itself, but each connection takes memory, and connecting all properties of all objects can be very costly, especially if only a few properties of a subset of objects will ever change.

The OnRead connection policy will not connect to objects or properties that are never read from (for instance, never rendered in a view), but remembering which connections have been made requires some book-keeping overhead, and unpredictable memory growth over time. For instance, scrolling down a long list of items can easily result in thousands of new connections being made.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRangeModel.autoConnectPolicy`, :sip:ref:`~PyQt6.QtCore.QRangeModel.roleNames`.
