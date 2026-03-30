.. sip:method-description::
    :status: todo
    :pysig: 124460b4d67fea429700376c82073a32
    :realsig: (QQmlEngine*, QAnyStringView, QAnyStringView, QQmlComponent::CompilationMode, QObject*)
    :digest: 8cf59242aeb43ae685dd878be811e442

Create a :sip:ref:`~PyQt6.QtQml.QQmlComponent` from the given *uri* and *typeName* and give it the specified *parent* and *engine*. If *mode* is :sip:ref:`~PyQt6.QtQml.QQmlComponent.CompilationMode.Asynchronous`, the component will be loaded and compiled asynchronously.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent.loadFromModule`.
