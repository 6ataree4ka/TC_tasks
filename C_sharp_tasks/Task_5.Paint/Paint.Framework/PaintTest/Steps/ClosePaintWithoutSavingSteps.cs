using System.Threading;
using NUnit.Framework;
using Paint.Framework;
using Paint.Framework.Views;
using TechTalk.SpecFlow;

namespace PaintTest.Steps
{
    [Binding]
    public class ClosePaintWithoutSavingSteps
    {
        [Given(@"Main Paint window opened")]
        public void OpenApplicationMainWindow()
        {
            AppFactory.Instance.LaunchApplication();
        }

        [When(@"I open '(.*)' folder, select picture '(.*)'")]
        public void OpenTargetPicture(string path, string picture)
        {
            BaseMenu.FileButton.Click();
            BaseMenu.ClickMenuOpen();
            BaseMenu.OpenTargetPicture(FileUtil.DataController.ReadParam(path), FileUtil.DataController.ReadParam(picture));
        }

        [When(@"I click Select menu item")]
        public void ClickSelectMenuItem()
        {
            PictureView.SelectButton.Click();
        }

        [When(@"I click Select all button")]
        public void ClickSelectAllButton()
        {
            PictureView.ClickSelectAll();
            //PictureView.SelectAllIfEnabled();
        }

        [When(@"I click '(.*)'")]
        public void ClickButton(string button)
        {
            PictureView.GetButtonByText(FileUtil.DataController.ReadParam(button)).Click();
        }

        [When(@"I click '(.*)' application")]
        public void CloseApplication(string button)
        {
            PictureView.GetButtonById(FileUtil.DataController.ReadParam(button)).Click();
        }
        
        [Then(@"Paint is closed")]
        public void CheckThatApplicationClosed()
        {
            Assert.False(AppState.IsProcessOpen(FileUtil.DataController.ReadParam("appName")));
        }
    }
}
