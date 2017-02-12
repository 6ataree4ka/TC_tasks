using Microsoft.VisualStudio.TestTools.UnitTesting;
using Calculator;
using Calculator.Screens;

namespace CalculatorTests
{
    [TestClass]
    public class ClaculatorTests
    {
        private static string firstNumber = AppFactory.Instance.ReadConfigParam("firstNumberValue");
        private static string secondNumber = AppFactory.Instance.ReadConfigParam("secondNumberValue");
        private static string thirdNumber = AppFactory.Instance.ReadConfigParam("thirdNumberValue");

        [TestInitialize]
        public void TestInitialize()
        {
            AppFactory.Instance.LaunchApplication();
        }

        [TestMethod]
        public void TestSimpleCalculator()
        {
            SimpleViewScreen simpleViewScreen = new SimpleViewScreen();
            simpleViewScreen.SelectTargetView();
            simpleViewScreen.EnterNumber(firstNumber);
            simpleViewScreen.ClickButton(simpleViewScreen.AddButton());

            simpleViewScreen.EnterNumber(secondNumber);
            simpleViewScreen.ClickButton(simpleViewScreen.EqualsButton());
            simpleViewScreen.ClickButton(simpleViewScreen.MemoryAdd());

            simpleViewScreen.EnterNumber(thirdNumber);
            simpleViewScreen.ClickButton(simpleViewScreen.AddButton());
            simpleViewScreen.ClickButton(simpleViewScreen.MemoryRecall());
            simpleViewScreen.ClickButton(simpleViewScreen.EqualsButton());
            Assert.AreEqual(simpleViewScreen.GetExpectedResult(), simpleViewScreen.GetResult());
        }

        [TestMethod]
        public void TestSientificCalculator()
        {
            ScientificViewScreen sientificViewSceen = new ScientificViewScreen();
            sientificViewSceen.SelectTargetView();

            sientificViewSceen.EnterNumber(firstNumber);
            sientificViewSceen.ClickButton(sientificViewSceen.AddButton());

            sientificViewSceen.EnterNumber(secondNumber);
            sientificViewSceen.ClickButton(sientificViewSceen.EqualsButton());
            sientificViewSceen.ClickButton(sientificViewSceen.MemoryAdd());

            sientificViewSceen.EnterNumber(thirdNumber);
            sientificViewSceen.ClickButton(sientificViewSceen.AddButton());
            sientificViewSceen.ClickButton(sientificViewSceen.MemoryRecall());
            sientificViewSceen.ClickButton(sientificViewSceen.EqualsButton());
            Assert.AreEqual(sientificViewSceen.GetExpectedResult(), sientificViewSceen.GetResult());
        }

        [TestCleanup]
        public void TestCleanup()
        {
            AppFactory.Instance.CloseApplication();
        }
    }
}

