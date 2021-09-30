.. sip:method-description::
    :status: todo
    :pysig: 6a1bb6ed41f44b60e7bd83b0e9945aa7
    :realsig: (double,double)
    :digest: e13f45de0deb529d378c5b1cedd6f5e2

Sets the range in which the connection interval should be. The actual value will be decided by the controller. Both *minimum* and *maximum* are given in milliseconds. If *maximum* is smaller than *minimum*, it will be set to the value of *minimum*. The smallest possible connection interval is 7.5 milliseconds, the largest one is 4000 milliseconds.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.minimumInterval`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyConnectionParameters.maximumInterval`.
