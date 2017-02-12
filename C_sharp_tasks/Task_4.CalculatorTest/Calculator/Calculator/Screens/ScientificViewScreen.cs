using TestStack.White.UIItems;
using TestStack.White.UIItems.MenuItems;

namespace Calculator.Screens
{
    public class ScientificViewScreen : BaseScreen
    {
        private string menuItemName = AppFactory.Instance.ReadConfigParam("menuItemName");
        private string calculatorTypeName = AppFactory.Instance.ReadConfigParam("scientificViewName");

        private string equalsButton = AppFactory.Instance.ReadConfigParam("equalsButtonName");
        private string addButton = AppFactory.Instance.ReadConfigParam("addButtonName");
        private string memoryAddButton = AppFactory.Instance.ReadConfigParam("memoryAddButtonName");
        private string memoryRecallButton = AppFactory.Instance.ReadConfigParam("memoryRecallButtonName");
        private string sientificCalculatorTestResultValue = AppFactory.Instance.ReadConfigParam("sientificCalculatorTestResult");

        public override void SelectTargetView()
        {
            Menu mainMenu = GetMenu(menuItemName);
            mainMenu.Click();

            Menu calculatorType = GetMenu(calculatorTypeName);
            calculatorType.Click();

            Logger.Log.Info($"'{calculatorTypeName}' mode is selected.");
        }

        public Button AddButton()
        {
            return GetButton(addButton);
        }

        public Button EqualsButton()
        {
            return GetButton(equalsButton);
        }

        public Button MemoryAdd()
        {
            return GetButton(memoryAddButton);
        }

        public Button MemoryRecall()
        {
            return GetButton(memoryRecallButton);
        }

        public string GetExpectedResult()
        {
            return sientificCalculatorTestResultValue;
        }
    }
}
