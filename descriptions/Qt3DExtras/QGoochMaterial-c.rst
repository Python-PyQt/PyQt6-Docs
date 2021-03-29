.. sip:class-description::
    :status: todo
    :brief: Material that implements the Gooch shading model, popular in CAD and CAM applications
    :realname: Qt3DExtras::QGoochMaterial
    :digest: f16422e433c3a49b2aabbb6c22102783

The :sip:ref:`~PyQt6.Qt3DExtras.QGoochMaterial` provides a material that implements the Gooch shading model, popular in CAD and CAM applications.

The Gooch lighting model uses both color and brightness to help show the curvature of 3D surfaces. This is often better than models such as Phong that rely purely upon changes in brightness. In situations such as in CAD and CAM applications where photorealism is not a goal, the Gooch shading model in conjunction with some kind of silhouette edge inking is a popular solution.

The Gooch lighting model is explained fully in the `original Gooch paper <https://doc.qt.io/qt-6/http://www.cs.northwestern.edu/~ago820/SIG98/abstract.html>`_. The Gooch model mixes a diffuse object color with a user-provided cool color and warm color to produce the end points of a color ramp that is used to shade the object based upon the cosine of the angle between the vector from the fragment to the light source and the fragment's normal vector. Optionally, a specular highlight can be added on top. The relative contributions to the cool and warm colors by the diffuse color are controlled by the alpha and beta properties respecitvely.

This material uses an effect with a single render pass approach and performs per fragment lighting. Techniques are provided for OpenGL 2, OpenGL 3 or above as well as OpenGL ES 2.
