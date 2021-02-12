.. sip:class-description::
    :status: todo
    :brief: Contains a lightweight representation of a version number with two 8-bit segments, major and minor, either of which can be unknown
    :digest: 4a1b454c96b6438f9bc56a58386d3d42

The :sip:ref:`~PyQt6.QtCore.QTypeRevision` class contains a lightweight representation of a version number with two 8-bit segments, major and minor, either of which can be unknown.

Use this class to describe revisions of a type. Compatible revisions can be expressed as increments of the minor version. Breaking changes can be expressed as increments of the major version. The return values of QMetaMethod::revision() and QMetaProperty::revision() can be passed to QTypeRevision::fromEncodedVersion(). The resulting major and minor versions specify in which Qt versions the properties and methods were added.

.. seealso:: QMetaMethod::revision(), QMetaProperty::revision().
