.. sip:method-description::
    :status: todo
    :pysig: a81259cef8e959c624df1d456e5d3297
    :realsig: ()
    :digest: fc70f032e71d3970c1789e87ca049cfb

Function that can be used to sync Qt state with the Window Systems state.

This function will first empty Qts events by calling :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents`, then the platform plugin will sync up with the windowsystem, and finally Qts events will be delived by another call to :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents`;

This function is timeconsuming and its use is discouraged.
