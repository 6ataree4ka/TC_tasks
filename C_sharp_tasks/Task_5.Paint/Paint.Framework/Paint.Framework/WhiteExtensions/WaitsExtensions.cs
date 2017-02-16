using System;
using System.Threading;
using Paint.Framework.Views;
using TestStack.White.UIItems;
using TestStack.White.UIItems.Finders;
using TestStack.White.UIItems.MenuItems;
using TestStack.White.Utility;

namespace Paint.Framework.WhiteExtensions
{
    class WaitsExtensions
    {
        /*public static void ClickIfElementPresented(string windowName, SearchCriteria criteria)
        {
            var loaded = Retry.For(() => BaseView.Application.GetWindow(windowName).Exists<Menu>(criteria),
                TimeSpan.FromSeconds(5));
            if (loaded)
            {
                BaseView.Application.GetWindow(windowName).Get<Menu>(criteria).Click();
            }

            int timeout = 30;
            for (int i = 0; i < timeout; i++)
            {
                if (BaseView.Application.GetWindow(windowName).Exists(criteria))
                {
                    Thread.Sleep(1);
                    BaseView.Application.GetWindow(windowName).Get(criteria).Click();
                    return;
                }
                else
                {
                    Thread.Sleep(1);
                }
            }
        }*/

        public static bool ElemEnabled(UIItem element)
        {
            if (element.Enabled)
                {
                    return true;
                }
            return false;
        }
    }
}
