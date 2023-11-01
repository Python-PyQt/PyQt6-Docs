:orphan:

.. sip:class:: PyQt6.Qt3DRender.QGraphicsApiFilter
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: Qt3DRender/QGraphicsApiFilter-c.rst

    .. sip:enum:: PyQt6.Qt3DRender.QGraphicsApiFilter.Api
        :description: Qt3DRender/QGraphicsApiFilter-Api-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QGraphicsApiFilter.Api.DirectX
            :description: Qt3DRender/QGraphicsApiFilter-Api-DirectX-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QGraphicsApiFilter.Api.OpenGL
            :description: Qt3DRender/QGraphicsApiFilter-Api-OpenGL-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QGraphicsApiFilter.Api.OpenGLES
            :description: Qt3DRender/QGraphicsApiFilter-Api-OpenGLES-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QGraphicsApiFilter.Api.RHI
            :description: Qt3DRender/QGraphicsApiFilter-Api-RHI-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QGraphicsApiFilter.Api.Vulkan
            :description: Qt3DRender/QGraphicsApiFilter-Api-Vulkan-v.rst

    .. sip:enum:: PyQt6.Qt3DRender.QGraphicsApiFilter.OpenGLProfile
        :description: Qt3DRender/QGraphicsApiFilter-OpenGLProfile-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QGraphicsApiFilter.OpenGLProfile.CompatibilityProfile
            :description: Qt3DRender/QGraphicsApiFilter-OpenGLProfile-CompatibilityProfile-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QGraphicsApiFilter.OpenGLProfile.CoreProfile
            :description: Qt3DRender/QGraphicsApiFilter-OpenGLProfile-CoreProfile-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QGraphicsApiFilter.OpenGLProfile.NoProfile
            :description: Qt3DRender/QGraphicsApiFilter-OpenGLProfile-NoProfile-v.rst

    .. sip:method:: PyQt6.Qt3DRender.QGraphicsApiFilter.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: Qt3DRender/QGraphicsApiFilter-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QGraphicsApiFilter.api
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QGraphicsApiFilter.Api`
        :description: Qt3DRender/QGraphicsApiFilter-api-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QGraphicsApiFilter.extensions
        :returns:
            List[str]
        :description: Qt3DRender/QGraphicsApiFilter-extensions-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QGraphicsApiFilter.majorVersion
        :returns:
            int
        :description: Qt3DRender/QGraphicsApiFilter-majorVersion-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QGraphicsApiFilter.minorVersion
        :returns:
            int
        :description: Qt3DRender/QGraphicsApiFilter-minorVersion-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QGraphicsApiFilter.profile
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QGraphicsApiFilter.OpenGLProfile`
        :description: Qt3DRender/QGraphicsApiFilter-profile-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QGraphicsApiFilter.setApi
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QGraphicsApiFilter.Api`
        :description: Qt3DRender/QGraphicsApiFilter-setApi-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QGraphicsApiFilter.setExtensions
        :args:
            Iterable[Optional[str]]
        :description: Qt3DRender/QGraphicsApiFilter-setExtensions-f-1.rst

    .. sip:method:: PyQt6.Qt3DRender.QGraphicsApiFilter.setMajorVersion
        :args:
            int
        :description: Qt3DRender/QGraphicsApiFilter-setMajorVersion-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QGraphicsApiFilter.setMinorVersion
        :args:
            int
        :description: Qt3DRender/QGraphicsApiFilter-setMinorVersion-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QGraphicsApiFilter.setProfile
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QGraphicsApiFilter.OpenGLProfile`
        :description: Qt3DRender/QGraphicsApiFilter-setProfile-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QGraphicsApiFilter.setVendor
        :args:
            Optional[str]
        :description: Qt3DRender/QGraphicsApiFilter-setVendor-f-1.rst

    .. sip:method:: PyQt6.Qt3DRender.QGraphicsApiFilter.vendor
        :returns:
            str
        :description: Qt3DRender/QGraphicsApiFilter-vendor-f.rst

    .. sip:signal:: PyQt6.Qt3DRender.QGraphicsApiFilter.apiChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QGraphicsApiFilter.Api`
        :description: Qt3DRender/QGraphicsApiFilter-apiChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QGraphicsApiFilter.extensionsChanged
        :args:
            Iterable[Optional[str]]
        :description: Qt3DRender/QGraphicsApiFilter-extensionsChanged-s-1.rst

    .. sip:signal:: PyQt6.Qt3DRender.QGraphicsApiFilter.graphicsApiFilterChanged
        :description: Qt3DRender/QGraphicsApiFilter-graphicsApiFilterChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QGraphicsApiFilter.majorVersionChanged
        :args:
            int
        :description: Qt3DRender/QGraphicsApiFilter-majorVersionChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QGraphicsApiFilter.minorVersionChanged
        :args:
            int
        :description: Qt3DRender/QGraphicsApiFilter-minorVersionChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QGraphicsApiFilter.profileChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QGraphicsApiFilter.OpenGLProfile`
        :description: Qt3DRender/QGraphicsApiFilter-profileChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QGraphicsApiFilter.vendorChanged
        :args:
            Optional[str]
        :description: Qt3DRender/QGraphicsApiFilter-vendorChanged-s-1.rst
