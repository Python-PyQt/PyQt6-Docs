.. sip:method-description::
    :status: todo
    :pysig: 6be1d7e061e89802c88c7650a4436b6c
    :realsig: (const QByteArray&, const QUrl&)
    :digest: ed044e9a4afdde01ba0b695be802c361

Sets the :sip:ref:`~PyQt6.QtQml.QQmlComponent` to use the given QML *data*. If *url* is provided, it is used to set the component name and to provide a base path for items resolved by this component.

**Warning:** The new component will shadow any existing component of the same URL. You should not pass a URL of an existing component.
