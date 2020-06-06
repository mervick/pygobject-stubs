# encoding: utf-8
# module gi.repository.Cogl
# from /usr/lib64/girepository-1.0/Cogl-1.0.typelib
# by generator 1.147
"""
An object which wraps an introspection typelib.

    This wrapping creates a python module like representation of the typelib
    using gi repository as a foundation. Accessing attributes of the module
    will dynamically pull them in and create wrappers for the members.
    These members are then cached on this introspection module.
"""

# imports
import gi as __gi
import gobject as __gobject


class GLES2Vtable(__gi.Struct):
    """
    :Constructors:
    
    ::
    
        GLES2Vtable()
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        """ Default dir() implementation. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, *args, **kwargs): # real signature unknown
        """ Default object formatter. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init_subclass__(self, *args, **kwargs): # real signature unknown
        """
        This method is called when a class is subclassed.
        
        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __subclasshook__(self, *args, **kwargs): # real signature unknown
        """
        Abstract classes can override this to customize issubclass().
        
        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass

    def __weakref__(self, *args, **kwargs): # real signature unknown
        pass

    glActiveTexture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glAttachShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glBindAttribLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glBindBuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glBindFramebuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glBindRenderbuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glBindTexture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glBlendColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glBlendEquation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glBlendEquationSeparate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glBlendFunc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glBlendFuncSeparate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glBufferData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glBufferSubData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glCheckFramebufferStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glClear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glClearColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glClearDepthf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glClearStencil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glColorMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glCompileShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glCompressedTexImage2D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glCompressedTexSubImage2D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glCopyTexImage2D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glCopyTexSubImage2D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glCreateProgram = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glCreateShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glCullFace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glDeleteBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glDeleteFramebuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glDeleteProgram = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glDeleteRenderbuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glDeleteShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glDeleteTextures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glDepthFunc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glDepthMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glDepthRangef = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glDetachShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glDisable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glDisableVertexAttribArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glDrawArrays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glDrawElements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glEnableVertexAttribArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glFinish = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glFlush = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glFramebufferRenderbuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glFramebufferTexture2D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glFrontFace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGenBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGenerateMipmap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGenFramebuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGenRenderbuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGenTextures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetActiveAttrib = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetActiveUniform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetAttachedShaders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetAttribLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetBooleanv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetBufferParameteriv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetFloatv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetFramebufferAttachmentParameteriv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetIntegerv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetProgramInfoLog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetProgramiv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetRenderbufferParameteriv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetShaderInfoLog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetShaderiv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetShaderPrecisionFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetShaderSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetTexParameterfv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetTexParameteriv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetUniformfv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetUniformiv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetUniformLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetVertexAttribfv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetVertexAttribiv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glGetVertexAttribPointerv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glIsBuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glIsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glIsFramebuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glIsProgram = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glIsRenderbuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glIsShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glIsTexture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glLineWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glLinkProgram = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glPixelStorei = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glPolygonOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glReadPixels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glReleaseShaderCompiler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glRenderbufferStorage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glSampleCoverage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glScissor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glShaderBinary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glShaderSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glStencilFunc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glStencilFuncSeparate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glStencilMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glStencilMaskSeparate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glStencilOp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glStencilOpSeparate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glTexImage2D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glTexParameterf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glTexParameterfv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glTexParameteri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glTexParameteriv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glTexSubImage2D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform1f = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform1fv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform1i = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform1iv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform2f = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform2fv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform2i = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform2iv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform3f = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform3fv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform3i = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform3iv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform4f = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform4fv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform4i = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniform4iv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniformMatrix2fv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniformMatrix3fv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUniformMatrix4fv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glUseProgram = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glValidateProgram = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glVertexAttrib1f = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glVertexAttrib1fv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glVertexAttrib2f = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glVertexAttrib2fv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glVertexAttrib3f = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glVertexAttrib3fv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glVertexAttrib4f = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glVertexAttrib4fv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glVertexAttribPointer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    glViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __class__ = None # (!) real value is "<class 'gi.types.StructMeta'>"
    __dict__ = None # (!) real value is "mappingproxy({'__info__': StructInfo(GLES2Vtable), '__module__': 'gi.repository.Cogl', '__gtype__': <GType void (4)>, '__dict__': <attribute '__dict__' of 'GLES2Vtable' objects>, '__weakref__': <attribute '__weakref__' of 'GLES2Vtable' objects>, '__doc__': None, 'glBindTexture': <property object at 0x7fba890277c0>, 'glBlendFunc': <property object at 0x7fba890278b0>, 'glClear': <property object at 0x7fba890279a0>, 'glClearColor': <property object at 0x7fba89027a90>, 'glClearStencil': <property object at 0x7fba89027b80>, 'glColorMask': <property object at 0x7fba89027c70>, 'glCopyTexSubImage2D': <property object at 0x7fba89027db0>, 'glDeleteTextures': <property object at 0x7fba89027ef0>, 'glDepthFunc': <property object at 0x7fba8902a040>, 'glDepthMask': <property object at 0x7fba8902a130>, 'glDisable': <property object at 0x7fba8902a220>, 'glDrawArrays': <property object at 0x7fba8902a310>, 'glDrawElements': <property object at 0x7fba8902a400>, 'glEnable': <property object at 0x7fba8902a4f0>, 'glFinish': <property object at 0x7fba8902a5e0>, 'glFlush': <property object at 0x7fba8902a6d0>, 'glFrontFace': <property object at 0x7fba8902a7c0>, 'glCullFace': <property object at 0x7fba8902a8b0>, 'glGenTextures': <property object at 0x7fba8902a9a0>, 'glGetError': <property object at 0x7fba8902aa90>, 'glGetIntegerv': <property object at 0x7fba8902ab80>, 'glGetBooleanv': <property object at 0x7fba8902ac70>, 'glGetFloatv': <property object at 0x7fba8902ad60>, 'glGetString': <property object at 0x7fba8902ae50>, 'glHint': <property object at 0x7fba8902af40>, 'glIsTexture': <property object at 0x7fba8902b090>, 'glPixelStorei': <property object at 0x7fba8902b180>, 'glReadPixels': <property object at 0x7fba8902b220>, 'glScissor': <property object at 0x7fba8902b310>, 'glStencilFunc': <property object at 0x7fba8902b400>, 'glStencilMask': <property object at 0x7fba8902b4f0>, 'glStencilOp': <property object at 0x7fba8902b5e0>, 'glTexImage2D': <property object at 0x7fba8902b6d0>, 'glTexParameterf': <property object at 0x7fba8902b7c0>, 'glTexParameterfv': <property object at 0x7fba8902b900>, 'glTexParameteri': <property object at 0x7fba8902b9f0>, 'glTexParameteriv': <property object at 0x7fba8902bb30>, 'glGetTexParameterfv': <property object at 0x7fba8902bc70>, 'glGetTexParameteriv': <property object at 0x7fba8902bdb0>, 'glTexSubImage2D': <property object at 0x7fba8902bea0>, 'glCopyTexImage2D': <property object at 0x7fba8902c040>, 'glViewport': <property object at 0x7fba8902c0e0>, 'glIsEnabled': <property object at 0x7fba8902c1d0>, 'glLineWidth': <property object at 0x7fba8902c2c0>, 'glPolygonOffset': <property object at 0x7fba8902c3b0>, 'glDepthRangef': <property object at 0x7fba8902c4a0>, 'glClearDepthf': <property object at 0x7fba8902c590>, 'glCompressedTexImage2D': <property object at 0x7fba8902c6d0>, 'glCompressedTexSubImage2D': <property object at 0x7fba8902c810>, 'glSampleCoverage': <property object at 0x7fba8902c950>, 'glGetBufferParameteriv': <property object at 0x7fba8902ca90>, 'glGenBuffers': <property object at 0x7fba8902cb80>, 'glBindBuffer': <property object at 0x7fba8902cc70>, 'glBufferData': <property object at 0x7fba8902cd60>, 'glBufferSubData': <property object at 0x7fba8902ce50>, 'glDeleteBuffers': <property object at 0x7fba8902cf40>, 'glIsBuffer': <property object at 0x7fba8902d090>, 'glActiveTexture': <property object at 0x7fba8902d180>, 'glGenRenderbuffers': <property object at 0x7fba8902d2c0>, 'glDeleteRenderbuffers': <property object at 0x7fba8902d400>, 'glBindRenderbuffer': <property object at 0x7fba8902d540>, 'glRenderbufferStorage': <property object at 0x7fba8902d680>, 'glGenFramebuffers': <property object at 0x7fba8902d7c0>, 'glBindFramebuffer': <property object at 0x7fba8902d900>, 'glFramebufferTexture2D': <property object at 0x7fba8902da40>, 'glFramebufferRenderbuffer': <property object at 0x7fba8902db80>, 'glIsRenderbuffer': <property object at 0x7fba8902dcc0>, 'glCheckFramebufferStatus': <property object at 0x7fba8902de00>, 'glDeleteFramebuffers': <property object at 0x7fba8902df40>, 'glGenerateMipmap': <property object at 0x7fba8902e0e0>, 'glGetFramebufferAttachmentParameteriv': <property object at 0x7fba8902e1d0>, 'glGetRenderbufferParameteriv': <property object at 0x7fba8902e310>, 'glIsFramebuffer': <property object at 0x7fba8902e400>, 'glBlendEquation': <property object at 0x7fba8902e4f0>, 'glBlendColor': <property object at 0x7fba8902e5e0>, 'glBlendFuncSeparate': <property object at 0x7fba8902e720>, 'glBlendEquationSeparate': <property object at 0x7fba8902e860>, 'glReleaseShaderCompiler': <property object at 0x7fba8902e9a0>, 'glGetShaderPrecisionFormat': <property object at 0x7fba8902eae0>, 'glShaderBinary': <property object at 0x7fba8902ebd0>, 'glStencilFuncSeparate': <property object at 0x7fba8902ed10>, 'glStencilMaskSeparate': <property object at 0x7fba8902ee50>, 'glStencilOpSeparate': <property object at 0x7fba8902ef90>, 'glCreateProgram': <property object at 0x7fba8902f0e0>, 'glCreateShader': <property object at 0x7fba8902f1d0>, 'glDeleteShader': <property object at 0x7fba8902f2c0>, 'glAttachShader': <property object at 0x7fba8902f3b0>, 'glUseProgram': <property object at 0x7fba8902f4a0>, 'glDeleteProgram': <property object at 0x7fba8902f590>, 'glGetShaderInfoLog': <property object at 0x7fba8902f6d0>, 'glGetProgramInfoLog': <property object at 0x7fba8902f810>, 'glGetShaderiv': <property object at 0x7fba8902f900>, 'glGetProgramiv': <property object at 0x7fba8902f9f0>, 'glDetachShader': <property object at 0x7fba8902fae0>, 'glGetAttachedShaders': <property object at 0x7fba8902fc20>, 'glIsShader': <property object at 0x7fba8902fd10>, 'glIsProgram': <property object at 0x7fba8902fe00>, 'glShaderSource': <property object at 0x7fba8902fef0>, 'glCompileShader': <property object at 0x7fba89030040>, 'glLinkProgram': <property object at 0x7fba89030130>, 'glGetUniformLocation': <property object at 0x7fba89030270>, 'glUniform1f': <property object at 0x7fba89030360>, 'glUniform2f': <property object at 0x7fba89030450>, 'glUniform3f': <property object at 0x7fba89030540>, 'glUniform4f': <property object at 0x7fba89030630>, 'glUniform1fv': <property object at 0x7fba89030720>, 'glUniform2fv': <property object at 0x7fba89030810>, 'glUniform3fv': <property object at 0x7fba89030900>, 'glUniform4fv': <property object at 0x7fba890309f0>, 'glUniform1i': <property object at 0x7fba89030ae0>, 'glUniform2i': <property object at 0x7fba89030bd0>, 'glUniform3i': <property object at 0x7fba89030cc0>, 'glUniform4i': <property object at 0x7fba89030db0>, 'glUniform1iv': <property object at 0x7fba89030ea0>, 'glUniform2iv': <property object at 0x7fba89030f90>, 'glUniform3iv': <property object at 0x7fba890320e0>, 'glUniform4iv': <property object at 0x7fba890321d0>, 'glUniformMatrix2fv': <property object at 0x7fba89032310>, 'glUniformMatrix3fv': <property object at 0x7fba89032450>, 'glUniformMatrix4fv': <property object at 0x7fba89032590>, 'glGetUniformfv': <property object at 0x7fba89032680>, 'glGetUniformiv': <property object at 0x7fba89032770>, 'glGetActiveUniform': <property object at 0x7fba890328b0>, 'glGetShaderSource': <property object at 0x7fba890329f0>, 'glValidateProgram': <property object at 0x7fba89032b30>, 'glVertexAttribPointer': <property object at 0x7fba89032c70>, 'glEnableVertexAttribArray': <property object at 0x7fba89032db0>, 'glDisableVertexAttribArray': <property object at 0x7fba89032ef0>, 'glVertexAttrib1f': <property object at 0x7fba89033090>, 'glVertexAttrib1fv': <property object at 0x7fba890331d0>, 'glVertexAttrib2f': <property object at 0x7fba89033310>, 'glVertexAttrib2fv': <property object at 0x7fba89033450>, 'glVertexAttrib3f': <property object at 0x7fba89033590>, 'glVertexAttrib3fv': <property object at 0x7fba890336d0>, 'glVertexAttrib4f': <property object at 0x7fba89033810>, 'glVertexAttrib4fv': <property object at 0x7fba89033950>, 'glGetVertexAttribfv': <property object at 0x7fba89033a90>, 'glGetVertexAttribiv': <property object at 0x7fba89033bd0>, 'glGetVertexAttribPointerv': <property object at 0x7fba89033d10>, 'glGetAttribLocation': <property object at 0x7fba89033e50>, 'glBindAttribLocation': <property object at 0x7fba89033f90>, 'glGetActiveAttrib': <property object at 0x7fba89034130>})"
    __gtype__ = None # (!) real value is '<GType void (4)>'
    __info__ = StructInfo(GLES2Vtable)


