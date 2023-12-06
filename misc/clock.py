import time
import objc
import AppKit
from PyObjCTools import AppHelper
import pyautogui

class FloatingClock(AppKit.NSObject):
    window = None
    clock_text = None
    timer = None

    @classmethod
    def alloc(cls):
        return cls

    @classmethod
    def init(cls):
        self = cls
        if self.window is not None:
            return self

        # Set initial position and font for the clock
        self.position = (100, 100)
        self.font = AppKit.NSFont.systemFontOfSize_(20)

        # Create a transparent window
        self.window = AppKit.NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            ((0, 0), (200, 50)),
            AppKit.NSBorderlessWindowMask,
            AppKit.NSBackingStoreBuffered,
            False
        )

        # Set window attributes
        self.window.setLevel_(AppKit.NSStatusWindowLevel)
        self.window.setBackgroundColor_(AppKit.NSColor.clearColor())
        self.window.setOpaque_(False)
        self.window.setHasShadow_(False)

        # Create a text field for the clock
        self.clock_text = AppKit.NSTextField.alloc().initWithFrame_(((0, 0), (200, 50)))
        self.clock_text.setEditable_(False)
        self.clock_text.setBordered_(False)
        self.clock_text.setDrawsBackground_(False)
        self.clock_text.setFont_(self.font)
        self.clock_text.setAlignment_(AppKit.NSCenterTextAlignment)

        # Add the text field to the window
        self.window.contentView().addSubview_(self.clock_text)

        # Set up a timer to update the clock every second
        self.timer = AppKit.NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
            1.0,
            self,
            objc.selector(self.updateClock_, signature='v@:@'),
            None,
            True
        )

        return self

    @classmethod
    def updateClock_(cls, timer):
        # Get the current time and update the clock text
        current_time = time.strftime("%H:%M:%S")
        cls.clock_text.setStringValue_(current_time)

    @classmethod
    def show(cls):
        # Show the window and set its initial position
        cls.window.makeKeyAndOrderFront_(None)
        cls.window.setFrameTopLeftPoint_((cls.position[0], cls.position[1]))

        # Move the window to the top level
        AppKit.NSApp.activateIgnoringOtherApps_(True)

        # Move the window to the initial position
        pyautogui.moveTo(cls.position[0], cls.position[1])

        # Start the main application loop
        AppHelper.runEventLoop()

if __name__ == "__main__":
    # Start the application
    app = AppKit.NSApplication.sharedApplication()
    delegate = FloatingClock.alloc().init()
    app.setDelegate_(delegate)
    delegate.show()
