using System.Threading;
using System.Windows.Automation;
using TestStack.White.UIItems;
using TestStack.White.UIItems.Actions;
using TestStack.White.UIItems.Finders;
using TestStack.White.UIItems.MenuItems;
using TestStack.White.UIItems.WindowItems;

namespace Paint.Framework.Views
{
    public static class PictureView
    {
        private static string pictureName = "Penguins";
        private static Window GetPictureWindow()
        {
            return BaseView.Application.GetWindow($"{pictureName} - Paint");
        }

        public static Button GetButtonByText(string name)
        {
            return GetPictureWindow().Get<Button>(SearchCriteria.ByText(name));
        }

        public static Button GetButtonById(string id)
        {
            return GetPictureWindow().Get<Button>(SearchCriteria.ByAutomationId(id));
        }
        
        private static AutomationElement MainPane => GetPictureWindow().AutomationElement.FindFirst(TreeScope.Descendants,
            new PropertyCondition(AutomationElement.ClassNameProperty, "NetUIHWND"));

        public static Button SelectButton
        {
            get
            {
                var selectButton = MainPane.FindAll(TreeScope.Descendants,
                    new PropertyCondition(AutomationElement.NameProperty, "Select"));
                return new Button(selectButton[2], new NullActionListener());
            }
        }

        /*public static void SelectAllIfEnabled()
        {
            WhiteExtensions.WaitsExtensions.ClickIfElementPresented(
                $"{AppFactory.Instance.ReadConfigParam("Picture")} - Paint", SearchCriteria.ByText("Select all"));
        }*/

        public static Menu SelectAll => GetPictureWindow().Get<Menu>(SearchCriteria.ByText("Select all"));

        public static void ClickSelectAll()
        {
            GetPictureWindow().Mouse.Location = SelectAll.Location;
            Thread.Sleep(500);
            GetPictureWindow().Mouse.Click();
        }
    }
}
