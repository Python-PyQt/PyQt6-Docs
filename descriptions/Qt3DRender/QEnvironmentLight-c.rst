.. sip:class-description::
    :status: todo
    :brief: Encapsulate an environment light object in a Qt 3D scene
    :realname: Qt3DRender::QEnvironmentLight
    :digest: 407081b5a061983e560b0848b3adc33e

Encapsulate an environment light object in a Qt 3D scene.

:sip:ref:`~PyQt6.Qt3DRender.QEnvironmentLight` uses cubemaps to implement image-based lighting (IBL), a technique often used in conjunction with physically-based rendering (PBR). The cubemaps are typically expected be based on high dynamic range (HDR) images, with a suitable OpenGL format (such as RGBA16F) that can handle the increased range of values.

There are a variety of tools that can be used to produce the cubemaps needed by :sip:ref:`~PyQt6.Qt3DRender.QEnvironmentLight`. Some examples include

* `cmftStudio <https://github.com/dariomanesku/cmftStudio>`_

* `IBLBaker <https://github.com/derkreature/IBLBaker>`_

* `Lys <https://www.knaldtech.com/lys/>`_

`HDRI Haven <https://hdrihaven.com/hdris/>`_ provides many CC0-licensed HDR images that can be used as source material for the above tools.
