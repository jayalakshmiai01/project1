# # import wxPython
# import wx
 
# app = wx.App()
 
# # create frame using Frame() constructor
# frame = wx.Frame(None, id = 10, title ="Frame", 
#                       pos = wx.DefaultPosition,
#                          size = wx.DefaultSize, 
#                 style = wx.DEFAULT_FRAME_STYLE,
#                                name = "frame")
 
# # show frame
# frame.Show(True)
 
# app.MainLoop()

# import wx
# import wx.aui as aui


# text = """\
# Hello!

# Welcome to this little demo of draggable tabs using the aui module.

# To try it out, drag a tab from the top of the window all the way to the bottom.  After releasing the mouse, the tab will dock at the hinted position.  Then try it again with the remaining tabs in various other positions.  Finally, try dragging a tab to an existing tab ctrl.  You'll soon see that very complex tab layouts may be achieved.
# """

# #----------------------------------------------------------------------

# class TestPanel(wx.Panel):
#     def __init__(self, parent, log):
#         self.log = log
#         wx.Panel.__init__(self, parent, -1)

#         self.nb = aui.AuiNotebook(self)
#         page = wx.TextCtrl(self.nb, -1, text, style=wx.TE_MULTILINE)
#         self.nb.AddPage(page, "Welcome")

#         for num in range(1, 5):
#             page = wx.TextCtrl(self.nb, -1, "This is page %d" % num ,
#                                style=wx.TE_MULTILINE)
#             self.nb.AddPage(page, "Tab Number %d" % num)

#         sizer = wx.BoxSizer()
#         sizer.Add(self.nb, 1, wx.EXPAND)
#         self.SetSizer(sizer)
#         wx.CallAfter(self.nb.SendSizeEvent)

# #----------------------------------------------------------------------

# def runTest(frame, nb, log):
#     win = TestPanel(nb, log)
#     return win

# #----------------------------------------------------------------------



# overview = """<html><body>
# <h2><center>Say something nice here</center></h2>

# </body></html>
# """



# if __name__ == '__main__':
#     import sys,os
#     import run
#     run.main(['', os.path.basename(sys.argv[0])] + sys.argv[1:])
#!/usr/bin/env python

#----------------------------------------------------------------------------
# Name:         run.py
# Purpose:      Simple framework for running individual demos
#
# Author:       Robin Dunn
#
# Created:      6-March-2000
# Copyright:    (c) 2000-2020 by Total Control Software
# Licence:      wxWindows license
#----------------------------------------------------------------------------

"""
This program will load and run one of the individual demos in this
directory within its own frame window.  Just specify the module name
on the command line.
"""

import wx
import wx.lib.inspection
import wx.lib.mixins.inspection
import sys, os

# stuff for debugging
print("Python %s" % sys.version)
print("wx.version: %s" % wx.version())
##print("pid: %s" % os.getpid()); input("Press Enter...")

assertMode = wx.APP_ASSERT_DIALOG
##assertMode = wx.APP_ASSERT_EXCEPTION


#----------------------------------------------------------------------------

class Log:
    def WriteText(self, text):
        if text[-1:] == '\n':
            text = text[:-1]
        wx.LogMessage(text)
    write = WriteText


class RunDemoApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):
    def __init__(self, name, module, useShell):
        self.name = name
        self.demoModule = module
        self.useShell = useShell
        wx.App.__init__(self, redirect=False)


    def OnInit(self):
        wx.Log.SetActiveTarget(wx.LogStderr())

        self.SetAssertMode(assertMode)
        self.InitInspection()  # for the InspectionMixin base class

        frame = wx.Frame(None, -1, "RunDemo: " + self.name, size=(200,100),
                        style=wx.DEFAULT_FRAME_STYLE, name="run a sample")
        frame.CreateStatusBar()

        menuBar = wx.MenuBar()
        menu = wx.Menu()
        item = menu.Append(-1, "&Widget Inspector\tF6", "Show the wxPython Widget Inspection Tool")
        self.Bind(wx.EVT_MENU, self.OnWidgetInspector, item)
        item = menu.Append(wx.ID_EXIT, "E&xit\tCtrl-Q", "Exit demo")
        self.Bind(wx.EVT_MENU, self.OnExitApp, item)
        menuBar.Append(menu, "&File")

        ns = {}
        ns['wx'] = wx
        ns['app'] = self
        ns['module'] = self.demoModule
        ns['frame'] = frame

        frame.SetMenuBar(menuBar)
        frame.Show(True)
        frame.Bind(wx.EVT_CLOSE, self.OnCloseFrame)

        win = self.demoModule.runTest(frame, frame, Log())

        # a window will be returned if the demo does not create
        # its own top-level window
        if win:
            # so set the frame to a good size for showing stuff
            frame.SetSize((800, 600))
            win.SetFocus()
            self.window = win
            ns['win'] = win
            frect = frame.GetRect()

        else:
            # It was probably a dialog or something that is already
            # gone, so we're done.
            frame.Destroy()
            return True

        self.SetTopWindow(frame)
        self.frame = frame
        #wx.Log.SetActiveTarget(wx.LogStderr())
        #wx.Log.SetTraceMask(wx.TraceMessages)

        if self.useShell:
            # Make a PyShell window, and position it below our test window
            from wx import py
            shell = py.shell.ShellFrame(None, locals=ns)
            frect.OffsetXY(0, frect.height)
            frect.height = 400
            shell.SetRect(frect)
            shell.Show()

            # Hook the close event of the test window so that we close
            # the shell at the same time
            def CloseShell(evt):
                if shell:
                    shell.Close()
                evt.Skip()
            frame.Bind(wx.EVT_CLOSE, CloseShell)

        return True


    def OnExitApp(self, evt):
        self.frame.Close(True)


    def OnCloseFrame(self, evt):
        if hasattr(self, "window") and hasattr(self.window, "ShutdownDemo"):
            self.window.ShutdownDemo()
        evt.Skip()

    def OnWidgetInspector(self, evt):
        wx.lib.inspection.InspectionTool().Show()


#----------------------------------------------------------------------------


def main(argv):
    useShell = False
    for x in range(len(sys.argv)):
        if sys.argv[x] in ['--shell', '-shell', '-s']:
            useShell = True
            del sys.argv[x]
            break

    if len(argv) < 2:
        print("Please specify a demo module name on the command-line")
        raise SystemExit

    # ensure the CWD is the demo folder
    demoFolder = os.path.realpath(os.path.dirname(__file__))
    os.chdir(demoFolder)

    sys.path.insert(0, os.path.join(demoFolder, 'agw'))
    sys.path.insert(0, '.')

    name, ext  = os.path.splitext(argv[1])
    module = __import__(name)


    app = RunDemoApp(name, module, useShell)
    locale = wx.Locale(wx.LANGUAGE_DEFAULT)
    app.MainLoop()



if __name__ == "__main__":
    main(sys.argv)