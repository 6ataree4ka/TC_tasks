using System.Diagnostics;
using TestStack.White;
using TestStack.White.UIItems.WindowItems;

namespace Paint.Framework.Views
{
    public static class BaseView
    {
        public static readonly Application Application = AppFactory.Instance.LaunchApplication();

        public static Window GetDefaultAppWindow()
        {
            Window window = Application.GetWindow("Untitled - Paint");
            window.DisplayState = DisplayState.Maximized;
            return window;
        }
    }

    public static class AppState
    {
        public static bool IsProcessOpen(string name)
        {
            foreach (Process process in Process.GetProcesses())
            {
                if (process.ProcessName.Contains(name))
                {
                    return true;
                }
            }
            return false;
        }
    }
}
