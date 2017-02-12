using TestStack.White;
using TestStack.White.UIItems;
using TestStack.White.UIItems.Finders;
using TestStack.White.UIItems.MenuItems;
using TestStack.White.UIItems.WindowItems;

namespace Calculator.Screens
{
    public abstract class BaseScreen
    {
        private Application _application = AppFactory.Instance.LaunchApplication();
        private string windowName = AppFactory.Instance.ReadConfigParam("windowName");
        private string _resultLabelIdName = AppFactory.Instance.ReadConfigParam("resultLabeleID");

        public abstract void SelectTargetView();

        public string GetResult()
        {
            return GetWindow().Get<Label>(SearchCriteria.ByAutomationId(_resultLabelIdName)).Text;
        }

        private Window GetWindow()
        {
            return _application.GetWindow(windowName);
        }

        protected Button GetButton(string name)
        {
            return GetWindow().Get<Button>(SearchCriteria.ByText(name));
        }

        protected Menu GetMenu(string menuName)
        {
            return GetWindow().Get<Menu>(SearchCriteria.ByText(menuName));
        }

        public void EnterNumber(string number)
        {
            foreach (char letter in number)
            {
                ClickButton(GetButton(letter.ToString()));
            }
        }

        public void ClickButton(Button buttonName)
        {
            buttonName.Click();
            Logger.Log.Info($"Button '{buttonName.Name}' clicked.");
        }
    }

}
