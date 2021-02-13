.. sip:method-description::
    :status: todo
    :pysig: 81c1901572c29dc53b5ea73e79e346d2
    :realsig: (QIODevice*,QWidget*)
    :digest: 3bfe0a15ac091e5dea410f497be7064d

Saves an XML representation of the given *widget* to the specified *device* in the standard UI file format.

**Note:** Unlike when saving a form in Qt Designer, all property values are written. This is because, the state of whether a property value was modified or not isn't stored in the Qt property system. The widget that is being saved, could have been created dynamically, not loaded via :sip:ref:`~PyQt6.QtDesigner.QAbstractFormBuilder.load`, so in this case the form builder isn't aware of the list of changed properties. Also, there's no generic way to do this for widgets that were created dynamically.

Therefore, you should remove properties that are not required from your resulting XML files, before loading them. Alternatively, if you already know which properties you want to save when you call this method, you can overload ``computeProperties()`` and return a filtered list of required properties. Otherwise, unexpected behavior may occur as some of these properties may depend on each other.

.. seealso:: :sip:ref:`~PyQt6.QtDesigner.QAbstractFormBuilder.load`.
