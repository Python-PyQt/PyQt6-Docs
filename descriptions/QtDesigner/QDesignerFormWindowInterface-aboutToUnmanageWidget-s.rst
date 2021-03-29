.. sip:signal-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 1c9067dac0693eaccda3b60354878f2f

This signal is emitted whenever a widget on the form is about to become unmanaged. When this signal is emitted, the specified *widget* is still managed, and a :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.widgetUnmanaged` signal will follow, indicating when it is no longer managed.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.unmanageWidget`, :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.isManaged`.
