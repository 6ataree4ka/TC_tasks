using System.Diagnostics;
using Paint.Framework;
using TechTalk.SpecFlow;

namespace PaintTest.Hooks
{
    [Binding]
    public sealed class BeforeScenario
    {
        [BeforeScenario]
        public static void CloseAllInstances()
        {
            foreach (Process process in Process.GetProcesses())
            {
                if (process.ProcessName.Contains(FileUtil.DataController.ReadParam("appName")))
                {
                    process.Kill();
                }
            }
        }

        [AfterScenario]
        public static void AfterScenarion()
        {
            AppFactory.Instance.CloseApplication();
        }
    }
}
