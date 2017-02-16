using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Windows.Automation;
using TestStack.White.InputDevices;
using TestStack.White.UIItems;
using TestStack.White.UIItems.Actions;
using TestStack.White.UIItems.Finders;
using TestStack.White.UIItems.MenuItems;
using TestStack.White.UIItems.WindowItems;
using TestStack.White.UIItems.WindowStripControls;
using TestStack.White.WindowsAPI;

namespace Paint.Framework.Views
{
    public static class BaseMenu
    {
        private static AutomationElement MainPane
        {
            get
            {
                return BaseView.GetDefaultAppWindow().AutomationElement.FindFirst(TreeScope.Descendants,
                        new PropertyCondition(AutomationElement.ClassNameProperty, "NetUIHWND"));
            }
        }

        public static Button FileButton
        {
            get
            {
                var fileButton = MainPane.FindFirst(TreeScope.Descendants,
                    new PropertyCondition(AutomationElement.NameProperty, "Application menu"));
                return new Button(fileButton, new NullActionListener());
            }
        }

        private static Menu MenuOpen => BaseView.GetDefaultAppWindow().Get<Menu>(SearchCriteria.ByText("Open"));

        public static void ClickMenuOpen()
        {
            BaseView.GetDefaultAppWindow().Mouse.Location = MenuOpen.Location;
            Thread.Sleep(500);
            BaseView.GetDefaultAppWindow().Mouse.Click();
        }

        public static void OpenTargetPicture(string path, string picture)
        {
            List<Window> myWindows = BaseView.Application.GetWindows();
            Window openDialog = myWindows.First(n => n.Name == "Open");

            var addressElement = openDialog.Get<ToolStrip>(SearchCriteria.ByAutomationId("1001"));
            addressElement.Click();

            var adress = openDialog.Get<TextBox>(SearchCriteria.ByAutomationId("41477"));
            adress.Text = path;
            AttachedKeyboard keyboard = openDialog.Keyboard;
            keyboard.PressSpecialKey(KeyboardInput.SpecialKeys.RETURN);

            var fileName = openDialog.Get<TextBox>(SearchCriteria.ByControlType(ControlType.Edit).AndByText("File name:"));
            fileName.Text = picture;
            keyboard.PressSpecialKey(KeyboardInput.SpecialKeys.RETURN);
        }
    }
}
