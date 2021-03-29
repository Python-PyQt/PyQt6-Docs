.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 87490b93e957424580ccf59523b600c8

:sip:ref:`~PyQt6.QtWidgets.QFocusFrame` will track changes to *widget* and resize itself automatically. If the monitored widget's parent changes, :sip:ref:`~PyQt6.QtWidgets.QFocusFrame` will follow the widget and place itself around the widget automatically. If the monitored widget is deleted, :sip:ref:`~PyQt6.QtWidgets.QFocusFrame` will set it to zero.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFocusFrame.widget`.
