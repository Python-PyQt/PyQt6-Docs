.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 15e2c7ab95bdaf7c41474fe0c6ae4806

readRssi() reads RSSI (received signal strength indicator) for a connected remote device. If the read was successful, the RSSI is then reported by :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.rssiRead` signal.

**Note:** Prior to calling readRssi(), this controller must be connected to a peripheral. This controller must be created using :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.createCentral`.

**Note:** In case Bluetooth backend you are using does not support reading RSSI, the :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.errorOccurred` signal is emitted with an error code :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.Error.RssiReadError`. At the moment platforms supporting reading RSSI include Android, iOS and macOS.

.. seealso:: :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.rssiRead`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.connectToDevice`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.state`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.createCentral`, :sip:ref:`~PyQt6.QtBluetooth.QLowEnergyController.errorOccurred`.
