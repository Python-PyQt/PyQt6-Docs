.. sip:class-description::
    :status: todo
    :brief: Abstract base class for building advanced transformations on QGraphicsItems
    :digest: de09fa96df67e49cf03984ef5d00e7e8

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform` class is an abstract base class for building advanced transformations on QGraphicsItems.

As an alternative to :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform` lets you create and control advanced transformations that can be configured independently using specialized properties.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` allows you to assign any number of :sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform` instances to one :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`. Each :sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform` is applied in order, one at a time, to the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` it's assigned to.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform` is particularly useful for animations. Whereas :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransform` lets you assign any transform directly to an item, there is no direct way to interpolate between two different transformations (e.g., when transitioning between two states, each for which the item has a different arbitrary transform assigned). Using :sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform` you can interpolate the property values of each independent transformation. The resulting operation is then combined into a single transform which is applied to :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`.

Transformations are computed in true 3D space using :sip:ref:`~PyQt6.QtGui.QMatrix4x4`. When the transformation is applied to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`, it will be projected back to a 2D :sip:ref:`~PyQt6.QtGui.QTransform`. When multiple :sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform` objects are applied to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`, all of the transformations are computed in true 3D space, with the projection back to 2D only occurring after the last :sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform` is applied. The exception to this is :sip:ref:`~PyQt6.QtWidgets.QGraphicsRotation`, which projects back to 2D after each rotation to preserve the perspective effect around the X and Y axes.

If you want to create your own configurable transformation, you can create a subclass of :sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform` (or any or the existing subclasses), and reimplement the pure virtual :sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform.applyTo` function, which takes a pointer to a :sip:ref:`~PyQt6.QtGui.QMatrix4x4`. Each operation you would like to apply should be exposed as properties (e.g., customTransform->setVerticalShear(2.5)). Inside you reimplementation of :sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform.applyTo`, you can modify the provided transform respectively.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsTransform` can be used together with :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setRotation`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setScale`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.transform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScale`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsRotation`.
